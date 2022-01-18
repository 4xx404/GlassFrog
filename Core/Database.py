#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3

from .Styling.Banners import sd
from .Styling.Colors import bc

from .Config import CoreConfig
from .Commands import Command
from .Error import ErrorHandler

class DBManager:
	def __init__(self):
		self.Config = CoreConfig()
		self.Cmd = Command()
		self.Error = ErrorHandler()

		try:
			self.Database = sqlite3.connect(self.Config.AbsoluteDatabasePath)
			self.Cursor = self.Database.cursor()
		except Exception:
			self.Database = None
			self.Cursor = None
	
	def CreateTables(self):
		# All Tables that should be created running setup.py
		self.Tables = {
			"branches": """CREATE TABLE branches(
				id					INTEGER		PRIMARY KEY		AUTOINCREMENT	NOT NULL,
				fld					TEXT							NOT NULL,
				base_url				TEXT							NOT NULL,
				branch_url				TEXT							NOT NULL,
				branch_set_key				TEXT							NOT NULL,
				keyword					TEXT							NOT NULL,
				keyword_found				TEXT							NOT NULL,
				branch_date				DATETIME,
				UNIQUE(branch_url)
			);""",
			
			"branch_data": """CREATE TABLE branch_data(
				id					INTEGER		PRIMARY KEY		AUTOINCREMENT	NOT NULL,
				content_id				TEXT							NOT NULL,
				datatype				TEXT							NOT NULL,
				branch_url				TEXT							NOT NULL,
				branch_set_key				TEXT							NOT NULL,
				data					TEXT							NOT NULL,
				data_date				DATETIME,
				UNIQUE(data)
			);""",

			"portscanner_results": """CREATE TABLE portscanner_results(
				id					INTEGER		PRIMARY KEY		AUTOINCREMENT	NOT NULL,
				scan_id					TEXT							NOT NULL,
				host					TEXT							NOT NULL,
				port					TEXT							NOT NULL,
				port_status				TEXT							NOT NULL,
				port_service				TEXT							NOT NULL,
				scan_date				DATETIME,
				delete_date				DATETIME
			);""",
			
			"website_tools": """CREATE TABLE website_tools(
				id					INTEGER		PRIMARY KEY		AUTOINCREMENT	NOT NULL,
				name					TEXT							NOT NULL
			);""",
		}

		self.Response = {
			"status": False,
			"data": [],
			"errors": []
		}

		# Check Database Connection
		if(self.Database != None):
			# Database Connected
			for self.Table, self.SQL in self.Tables.items():
				try:
					self.Database.execute(self.SQL)

					# Table Created
					self.Response["status"] = True
					self.Response["data"].append(f"{sd.sBan} Created Database table:{bc.GC} {self.Table}{bc.BC}")
				except Exception as e:
					if("exists" in str(e)):
						# Table already exists (Ran setup.py previously)
						self.Response["status"] = None
						self.Response["data"].append(f"{sd.eBan.replace(' ERROR:', '')} Database table {bc.GC}{self.Table}{bc.BC} already exists")
					else:
						# Table does not exist & could not create table
						self.Response["status"] = False
						self.Response["errors"].append(self.Error.Throw("create_table_failed", self.Table))

			for self.Tool in self.Config.WebsiteToolList:
				self.Insert("website_tools", {"name": self.Tool})
		else:
			# No Database Connection
			self.Response["status"] = False
			self.Response["errors"].append(self.Error.Throw("database_connect_failed", self.Config.AbsoluteDatabasePath))

		return self.Response

	def Select(self, Table: str, Where: dict = {}):
		self.Table: str = Table.lower()
		self.Where: dict = Where

		self.ResponsePack: dict = {
			"status": False,
			"rows": [],
			"data_index": None,
			"error": ""
		}

		# Build SQL based on the Table name
		if(self.Table == "branches"):
			self.BaseURL = self.Where["base_url"]
			self.BranchSetKey = self.Where["branch_set_key"]

			self.IncludeKeyword = self.Where["include_keyword_found"]
			if(self.IncludeKeyword == True):
				self.KeywordFound = f"AND keyword_found='" + self.Where["keyword_found"] + "'"
			else:
				self.KeywordFound = None

			if(self.KeywordFound == None):
				self.SQL = f"SELECT * FROM {self.Table} WHERE base_url='{self.BaseURL}' AND branch_set_key='{self.BranchSetKey}'"
			else:
				self.SQL = f"SELECT * FROM {self.Table} WHERE base_url='{self.BaseURL}' AND branch_set_key='{self.BranchSetKey}' {self.KeywordFound}"
			self.DataIndex = 3 # Return Value database index when SQL is executed
		elif(self.Table == "branch_data"):
			self.ContentID = self.Where["content_id"]
			self.BranchSetKey = self.Where["branch_set_key"]

			self.DataIndex = 5 # Return Value database index when SQL is executed
			self.SQL = f"SELECT * FROM {self.Table} WHERE content_id='{self.ContentID}' AND branch_set_key='{self.Config.BranchSetKey}'"
		elif(self.Table == "website_tools"):
			self.DataIndex = 1 # Return Value database index when SQL is executed
			self.SQL = f"SELECT * FROM {self.Table} WHERE name!=''"
		else:
			# Table isn't defined so SQL Query cannot be defined
			self.SQL = None

		# Check Database Connection
		if(self.Database != None):
			if(self.SQL != None):
				try:
					# SQL Query was built successfully
					self.Cursor.execute(self.SQL)

					# SQL Query execution successful
					self.Rows = self.Cursor.fetchall()
					for self.Row in self.Rows:
						if(not self.Row[self.DataIndex] in self.ResponsePack["rows"]):
							self.ResponsePack["rows"].append(self.Row[self.DataIndex])
						else:
							continue

					self.ResponsePack["status"], self.ResponsePack["error"] = True, ""
				except Exception as e:
					# SQL Query execution failed
					self.ResponsePack["status"], self.ResponsePack["rows"] = False, []
					self.ResponsePack["error"] = self.Error.Throw("execute_select_failed", f"{self.Table}\n{e}")
			else:
				# Undefined Database Table
				self.Cmd.Quit(self.Error.Throw("undefined_table_select", self.Table))
		else:
			# No Database Connection
			self.ResponsePack["status"] = False
			self.ResponsePack["error"] = self.Error.Throw("database_connect_failed", self.Config.AbsoluteDatabasePath)

		return self.ResponsePack

	def Insert(self, Table: str, Data: dict = {}):
		self.Table: str = Table.lower()
		self.Data: dict = Data

		self.ResponsePack: dict = {
			"status": False,
			"rows": [],
			"error": ""
		}

		# Set Database Fields based on the Table name
		if(self.Table == "branches"):
			self.Fld = self.Data["fld"]
			self.BaseURL = self.Data["base_url"]
			self.BranchURL = self.Data["branch_url"]
			self.BranchSetKey = self.Data["branch_set_key"]
			self.Keyword = str(self.Data["keyword"]).replace(" ", "")
			self.KeywordFound = str(self.Data["keyword_found"])
			self.BranchDate = self.Config.GetDateTime()

			self.ReturnValue = self.Data["branch_url"]

			self.SQL = f"INSERT OR IGNORE INTO {self.Table}(fld, base_url, branch_url, branch_set_key, keyword, keyword_found, branch_date) VALUES ('{self.Fld}', '{self.BaseURL}', '{self.BranchURL}', '{self.BranchSetKey}', '{self.Keyword}', '{self.KeywordFound}', '{self.BranchDate}')"
		elif(self.Table == "branch_data"):
			self.ContentID = self.Data["content_id"]
			self.DataType = self.Data["datatype"]
			self.BranchURL = self.Data["branch_url"]
			self.BranchSetKey = self.Data["branch_set_key"]
			self.Data = self.Data["dat"]
			self.DataDate = self.Config.GetDateTime()

			self.ReturnValue = self.Data

			self.SQL = f"INSERT OR IGNORE INTO {self.Table}(content_id, datatype, branch_url, branch_set_key, data, data_date) VALUES('{self.ContentID}', '{self.DataType}', '{self.BranchURL}', '{self.BranchSetKey}', '{self.Data}', '{self.DataDate}')"
		elif(self.Table == "website_tools"):
			self.ToolName = str(self.Data["name"]).lower()

			self.ReturnValue = str(self.Data["name"]).lower()

			self.SQL = f"INSERT OR IGNORE INTO {self.Table}(name) VALUES('{self.ToolName}')"
		else:
			# Table isn't defined so SQL cannot be defined
			self.SQL = None

		if(self.Database != None and self.Cursor != None):
			if(self.SQL != None):
				try:
					# SQL Query was built successfully
					self.Cursor.execute(self.SQL)
					self.Database.commit()

					# SQL Query execution successful
					self.ResponsePack["status"] = True
					self.ResponsePack["rows"].append(self.ReturnValue)
					self.ResponsePack["error"] = ""
				except Exception as e:
					# SQL Query execution failed
					self.ResponsePack["status"] = False
					self.ResponsePack["rows"] = []
					self.ResponsePack["error"] = self.Error.Throw("execute_insert_failed", f"{self.Table}\n{e}")
			else:
				# Undefined Database Table
				self.Cmd.Quit(self.Error.Throw("undefined_table_insert", self.Table))
		else:
			# No Database Connection
			self.ResponsePack["status"] = False
			self.ResponsePack["error"] = self.Error.Throw("database_connect_failed", self.Config.AbsoluteDatabasePath)

		return self.ResponsePack
