#!/usr/bin/python3
# -*- coding: utf-8 -*-
from lib2to3.pytree import Base
import sys, requests
sys.dont_write_bytecode = True

from .Styling.Banners import sd
from .Styling.Colors import bc

from sqlite3 import Error
from bs4 import BeautifulSoup
from tld import get_fld

from .Config import CoreConfig
from .Commands import Command
from .Database import DBManager
from .Validity import Validation
from .Requester import RequestHandler
from .BluePrint import BluePrinter

class ContentScanner:
	def __init__(self):
		self.Config = CoreConfig()
		self.Cmd = Command()
		self.Database = DBManager()
		self.Validator = Validation()
		self.Request = RequestHandler()
		self.BluePrint = BluePrinter()

		self.DuplicateScanned = [] # Scanner.py
		self.AnalysisDuplicates = [] # Scanner.py
		self.NoPrint = [] # Scanner.py

	def ThrowError(self, ErrorType: str, ErrorData: str or list = None):
		self.ErrorType: str = ErrorType.lower() # Error Type to set Error Message
		self.ErrorData: str = ErrorData # Data to pass into the Error Message

		self.DefinedErrors = [
			# Storage Error Tags
			"storage_database_invalid_type",
		]

		# Defined Error Type
		if(self.ErrorType in self.DefinedErrors):
			#  Error Messages
			if(self.ErrorType == "storage_database_invalid_type"):
				return f"{sd.eBan} Storage Type {bc.RC}{self.ErrorData}{bc.BC} is invalid"

			# Undefined Error Message
			else:
				return f"{sd.eBan} Error Type {bc.RC}{self.ErrorType}{bc.BC} thrown without an error message defined"
		# Undefined Error Type
		else:
			return f"{sd.eBan} Undefined Database Error Type {bc.RC}{self.ErrorType}{bc.BC}"

	def CreateBusinessEmailDomain(self, BranchLink: str):
		self.BranchLink: str = BranchLink
		self.Config.EmailDomains.append(f"@{get_fld(self.BranchLink)}")

	def HasNoPrint(self, Data: str, DataType: str):
		self.Data: str = Data
		self.DataType: str = DataType.lower()

		if(not self.Data in self.NoPrint and self.DataType != "unknown_data_type" and self.DataType != "single_alphabet_value"):
			return True
		else:
			return False

	def ShouldStore(self, HasStorage: bool, StorageType: str, Data: dict):
		self.HasStorage: bool = HasStorage
		self.StorageType: str = StorageType.lower()
		self.Data: dict = Data

		if(self.HasStorage):
			if(self.StorageType == "text_file"):
				self.DataToStore = self.Data["data"]

				if(not self.DataToStore in self.AnalysisDuplicates):
					try:
						self.xFile = open(self.Config.UnknownDataAnalysisFilePath, "a+")
						self.xFile.write(f"{self.DataToStore}\n")
						self.xFile.close()
					except Exception:
						return False

					return True
				else:
					# Dont return an error because we can ignore this & continue onto the next piece of data in SearchData()
					return False
			else:
				print(self.ThrowError("storage_textfile_invalid_type", self.StorageType))
				return False
		else:
			if(self.StorageType == "database"):
				self.BaseURL = self.Data["base_url"]
				self.ContentID = self.Data["content_id"]
				self.DataType = self.Data["type"]
				self.Branch = self.Data["branch_url"]
				self.BranchSetKey = self.Data["branch_set_key"]
				self.DataToStore = self.Data["data"]

				if(self.HasNoPrint(self.DataToStore, self.DataType)):
					print(f"{sd.sBan} [{bc.GC}{self.DataType.upper()}{bc.BC}] Found {bc.GC}{self.DataToStore}{bc.BC} on {bc.GC}{self.BaseURL}{bc.BC}") # Print Found Scanner Content
					self.NoPrint.append(self.DataToStore)

				self.DataPack = {
					"content_id": self.ContentID,
					"datatype": self.DataType,
					"dat": self.DataToStore,
					"branch_url": self.Branch,
					"branch_set_key": self.BranchSetKey,
					"data_date": self.Config.GetDateTime()
				}

				self.StorageResponse = self.Database.Insert("branch_data", Data=self.DataPack)
				if(self.StorageResponse["status"] == True):
					return True
				else:
					print(self.StorageResponse["error"])
					return False
			else:
				print(self.ThrowError("storage_database_invalid_type", self.StorageType))
				return False

	def SearchData(self, BaseURL: str, BranchList: list, BranchSetKey: str):
		self.BaseURL: str = BaseURL
		self.BranchList: list = BranchList
		self.BranchSetKey: str = BranchSetKey
		self.ContentID: str = BranchSetKey

		self.ContentWordList: list = []

		print(f"\n{sd.iBan} Searching for other data types, this may take a minute...\n")
		for self.Branch in self.BranchList:
			try:
				self.Req = requests.get(self.Branch, headers=self.Config.Headers)
				self.Soup = BeautifulSoup(self.Req.content, "html.parser")
			except Exception:
				continue
			except KeyboardInterrupt:
				continue
		
			try:
				for self.HTMLTag in self.Soup.find_all(self.Config.HTMLTags):
					self.WordsString = self.HTMLTag.text.replace("\n", "").replace("\t", "").replace("\n ", "")
					self.Words = self.WordsString.split()

					if(len(self.Words) > 0):
						for self.Word in self.Words:
#							print(" Word TEST: " + self.Word, f"Wordlist Length: {len(self.Words)}")
							
							self.ProtoType: dict = self.BluePrint.SetFormat(self.Word, self.Branch)
							# self.ProtoType keys: 'analysis', 'storage', 'type', 'data', 'branch'
							if(not self.ProtoType["data"] in self.DuplicateScanned or not self.ProtoType["data"] in self.AnalysisDuplicates):
								if(self.ProtoType["analysis"] == True and self.ProtoType["storage"] == False):
									# Database Storage Criteria:
									# 		ProtoType["type"] IS NOT "UNKNOWN_DATA_TYPE"
									# 		ProtoType["analysis"] IS True
									# 		ProtoType["storage"] IS False
									if(self.ShouldStore(HasStorage=False, StorageType="database", Data={"base_url": self.BaseURL, "content_id": self.ContentID, "type": self.ProtoType["type"], "data": self.ProtoType["data"], "branch_url": self.Branch, "branch_set_key": self.BranchSetKey})):
										self.DuplicateScanned.append(self.ProtoType["data"])
									else:
										continue
								else:
									if(self.ShouldStore(HasStorage=True, StorageType="text_file", Data={"data": self.ProtoType["data"]})):
										self.AnalysisDuplicates.append(self.ProtoType["data"])
									else:
										continue
							else:
								continue
					else:
						continue
			except KeyboardInterrupt:
				continue
			
			##add more tags to collect from that cant be interated over from htmlTags list
			#for self.img in self.soup.find_all('img', src=True):
			#	print(' Found an image: ' + str(self.img["src"]))