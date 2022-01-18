#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = True

from tld import get_tld
from sqlite3 import Error
from bs4 import BeautifulSoup
import requests

from .Styling.Banners import sd
from .Styling.Colors import bc

from .Config import CoreConfig
from .Commands import Command
from .Database import DBManager
from .Validity import Validation
from .Requester import RequestHandler
from .Scanner import ContentScanner

class CollectionManager:
	def __init__(self):
		self.Config = CoreConfig()
		self.Cmd = Command()
		self.Database = DBManager()
		self.Validator = Validation()
		self.Request = RequestHandler()
		self.Scanner = ContentScanner()

		self.Branches: list = []
		self.TotalKeywordFound = 0
		self.TotalBranchCount = 0

	def ThrowError(self, ErrorType: str, ErrorData: str or list = None):
		self.ErrorType: str = ErrorType.lower() # Error Type to set Error Message
		self.ErrorData: str = ErrorData # Data to pass into the Error Message

		self.DefinedErrors = [
			#  Error Tags
			"",
		]

		# Defined Error Type
		if(self.ErrorType in self.DefinedErrors):
			#  Error Messages
			if(self.ErrorType == ""):
				return f"{sd.eBan}  {bc.RC}{self.ErrorData}{bc.BC}"

			# Undefined Error Message
			else:
				return f"{sd.eBan} Error Type {bc.RC}{self.ErrorType}{bc.BC} thrown without an error message defined"
		# Undefined Error Type
		else:
			return f"{sd.eBan} Undefined Database Error Type {bc.RC}{self.ErrorType}{bc.BC}"

	def PrintBranchResults(self, BaseURL: str, TotalBranchCount: int, Keyword: str, TotalKeywordFound: int, BranchSetKey: str):
		self.BaseURL: str = BaseURL
		self.BranchCount: int = TotalBranchCount
		self.Keyword: str = Keyword.replace(" ", "")
		self.KeywordCount: int = TotalKeywordFound
		self.BranchSetKey: str = BranchSetKey

		self.Cmd.Clear()
		print(f"{sd.sBan} Base URL: {bc.GC}{self.BaseURL}{bc.BC}")
		print(f"{sd.sBan} Branch Set Key: {bc.GC}{self.BranchSetKey}{bc.BC}")
		print(f"{sd.sBan} Links Checked: {bc.GC}{self.BranchCount}{bc.BC}\n")

		if(self.KeywordCount == 0):
			self.ShouldPrint, self.KeywordCountPlaceholder = False, f"{sd.eBan.replace(' ERROR:', '')} {bc.RC}{self.Keyword}{bc.BC} found {bc.RC}{self.KeywordCount} times{bc.BC} on {bc.GC}{self.BaseURL}{bc.BC}"
		elif(self.KeywordCount == 1):
			self.ShouldPrint, self.KeywordCountPlaceholder = True, f"{sd.sBan} {bc.GC}{self.Keyword}{bc.BC} found {bc.GC}{self.KeywordCount} time{bc.BC} on {bc.GC}{self.BaseURL}{bc.BC} in Branch:"
		else:
			self.ShouldPrint, self.KeywordCountPlaceholder = True, f"{sd.sBan} {bc.GC}{self.Keyword}{bc.BC} found {bc.GC}{self.KeywordCount} times{bc.BC} on {bc.GC}{self.BaseURL}{bc.BC} in Branches:"

		self.BranchResponsePack = self.Database.Select("branches", Where={"base_url": f"{self.BaseURL}", "include_keyword_found": True, "keyword_found": "True", "branch_set_key": self.BranchSetKey})
		if(self.ShouldPrint):
			print(self.KeywordCountPlaceholder)
			for self.Row in self.BranchResponsePack["rows"]:
				print(f"\t{bc.GC}{self.Row}{bc.BC}")
		else:
			print(self.KeywordCountPlaceholder)

	def GetBranches(self, BaseURL: str, Keyword: str):
		self.BaseURL: str = BaseURL
		self.DomainName: str = str(get_tld(self.BaseURL, as_object=True).domain)
		self.Keyword: str = Keyword
		self.BranchSetKey = self.Config.CreateKey(10)

		self.Soup = BeautifulSoup(requests.get(self.BaseURL, headers=self.Config.Headers).content, "html.parser")

		print(f"{sd.sBan} Base URL: {bc.GC}{self.BaseURL}{bc.BC}")
		print(f"{sd.sBan} Keyword: {bc.GC}{self.Keyword.replace(' ', '')}{bc.BC}\n")
		print(f"{sd.iBan} Searching for Keyword...\n")

		for self.AnchorTag in self.Soup.find_all("a", href=True):
			try:
				self.Link = str(self.AnchorTag["href"])

				if(self.Validator.NotEmpty(self.Link)):
					if(self.Validator.HasProtocol(self.Link)):
						self.Link = self.Link
					elif(self.Link.startswith("/") or self.Link.startswith("#")):
						if(self.Link == "/" or self.Link == "#"):
							self.Link = None
						else:
							self.Link = f"{self.BaseURL[:-1]}{self.Link}"						
					else:
						self.Link = None

					if(not self.Link in self.Branches and self.Link != None):
						self.RequestResponse = self.Request.GetPageData("text", self.Link)
						if(self.RequestResponse):
							self.PageText = self.RequestResponse["data"]
						else:
							print(self.RequestResponse["error"])
							continue

						self.TotalBranchCount += 1
						if(self.Keyword in self.PageText):
							self.KeywordFound = True
							self.TotalKeywordFound += 1
							print(f"{sd.sBan} {bc.GC}KEYWORD FOUND: {bc.BC}{self.Link}")
						else:
							self.KeywordFound = False
							self.TotalKeywordFound += 0
							print(f"{sd.eBan.replace('ERROR:', 'KEYWORD NOT FOUND: ')}{bc.BC}{self.Link}")

						self.BranchPack = {
							"fld": self.DomainName,
							"base_url": self.BaseURL,
							"branch_url": self.Link,
							"branch_set_key": self.BranchSetKey,
							"keyword": self.Keyword,
							"keyword_found": self.KeywordFound
						}

						self.Storage = self.Database.Insert("branches", Data=self.BranchPack)
						if(self.Storage["status"]):
							for self.BranchURL in self.Storage["rows"]:
								#print("Storage: " + self.BranchURL)
								self.Branches.append(self.BranchURL)
							# Search for Other Data on found Branch
#							self.Scanner.SearchData(self.Link, self.BranchSetKey)
						else:
							self.Cmd.Debug(self.Storage["error"])
					else:
						continue
				else:
					continue
			except KeyboardInterrupt:
				pass

		if(len(self.Branches) > 0):
			self.PrintBranchResults(self.BaseURL, self.TotalBranchCount, self.Keyword, self.TotalKeywordFound, self.BranchSetKey)
			return self.Branches, self.BranchSetKey
		else:
			return None, None