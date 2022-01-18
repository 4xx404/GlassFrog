#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = True

from Core.Styling.Banners import sd
from Core.Styling.Colors import bc

from Core.Config import CoreConfig
from Core.Commands import Command
from Core.Database import DBManager
from Core.Validity import Validation
from Core.Collector import CollectionManager
from Core.Scanner import ContentScanner

class GlassFrog:
	def __init__(self):
		self.Config = CoreConfig()
		self.Cmd = Command()
		self.Database = DBManager()
		self.Validator = Validation()
		self.Collector = CollectionManager()

	def PrintHelpMenu(self):
		print(f"{sd.iBan} Include {bc.GC}http://{bc.BC} or {bc.GC}https://{bc.BC} in URL")
		print(f"\t{sd.eBan} {bc.RC}example.com{bc.BC}")
		print(f"\t{sd.eBan} {bc.RC}www.example.com{bc.BC}")
		print(f"\t{sd.sBan} {bc.GC}https://example.com{bc.BC}")
		print(f"\t{sd.sBan} {bc.GC}https://www.example.com\n{bc.BC}")

	def SetBaseURL(self):
		self.PrintHelpMenu()
		self.BaseURL = str(input(f"{bc.BC} Base URL: {bc.GC}"))
		if(self.Validator.NotEmpty(self.BaseURL)):
			if(self.BaseURL.endswith("/")):
				self.BaseURL = self.BaseURL
			else:
				self.BaseURL = f"{self.BaseURL}/"
			
			if(self.Validator.HasProtocol(self.BaseURL)):
				return self.BaseURL
			else:
				self.Cmd.Clear()
				print(f"{sd.eBan} Base URL must start with {bc.GC}http://{bc.BC} or {bc.GC}https://{bc.BC}\n")
				Initiate()
		else:
			self.Cmd.Clear()
			print(f"{sd.eBan} Base URL value cannot be empty\n")
			self.SetBaseURL()

	def SetKeyword(self):
		self.Keyword: str = str(input(f"{bc.BC} Keyword: {bc.GC}"))

		if(self.Validator.NotEmpty(self.Keyword)):
			return self.Keyword
		else:
			self.Cmd.Clear()
			print(f"{sd.eBan} Keyword value cannot be empty\n")
			self.SetKeyword()

	def SetExtend(self):
		self.Extend: str = str(input(f"\n{bc.BC} Extend to Branches[{bc.GC}y{bc.BC}/{bc.GC}n{bc.BC}]: {bc.GC}")).lower()

		self.Cmd.Clear()
		if(self.Validator.NotEmpty(self.Extend)):
			if(self.Extend == "y"):
				return "y"
			else:
				return "n"
		else:
			return "n"

	def StartSearch(self, BaseURL: str, Keyword: str):
		self.BaseURL: str = BaseURL
		self.Keyword: str = Keyword

		self.Cmd.Clear()

		self.Branches, self.BranchSetKey = self.Collector.GetBranches(self.BaseURL, self.Keyword)
		if(self.Branches != None):
			return self.Branches, self.BranchSetKey
		else:
			return None, None

if(__name__ == "__main__"):
	def Initiate():
		try:
			Frog = GlassFrog()

			BaseURL = Frog.SetBaseURL()
			Keyword = f" {Frog.SetKeyword()} "

			Branches, BranchSetKey = Frog.StartSearch(BaseURL, Keyword)
			if(Branches != None and BranchSetKey != None):
				ContentScanner().SearchData(BaseURL=BaseURL, BranchList=Branches, BranchSetKey=BranchSetKey)
			else:
				quit()

			# Remove any duplicated data from DataAnalysis/UNKNOWN_TYPE_DATA.txt
			Command().RemoveDuplicateFileContent(CoreConfig().UnknownDataAnalysisFilePath)

			ShouldExtend = Frog.SetExtend()
			if(ShouldExtend == "y"):
				print(f" [{bc.GC} * * * {bc.BC}] EXTENDER COMING SOON! [{bc.GC} * * * {bc.BC}]\n")

				# Frog.StartSearch(Branches)
			else:
				print(f"{bc.BC} Returned to {CoreConfig().AppName}...\n")

			Initiate()

		except KeyboardInterrupt:
			quit()

	Command().Clear()
	Initiate()
