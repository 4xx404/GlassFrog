#!/usr/bin/python3
import sys
sys.dont_write_bytecode = True

from Core.Styling.Banners import sd
from Core.Styling.Colors import bc

from Core.Config import CoreConfig
from Core.Commands import Command
from Core.Database import DBManager
from Core.Error import ErrorHandler

class SetupGlassFrog:
	def __init__(self):
		self.Config = CoreConfig()
		self.Cmd = Command()
		self.Error = ErrorHandler()

	def DependencyInstall(self):
		print(f"{bc.BC} Running GlassFrog setup...\n Installing Dependencies...\n")
		
		if(self.Cmd.InstallPythonDependencies()):
			print(f"{sd.sBan} Dependencies Installed")
		else:
			self.Cmd.Quit(self.Error.Throw("dependency_install_failed", self.Config.RequirementsFilePath))
	
	def MoveUIFiles(self):
		MovedOK = self.Cmd.MoveFile(self.Config.UIFilePath, self.Config.WebServerPath)

		if(MovedOK == True):
			print(f"{sd.sBan} Moved {bc.GC}{self.Config.UIFilePath}/{bc.BC} to {bc.GC}{self.Config.WebServerPath}{bc.BC}")
		elif(MovedOK == None):
			print(f"\n{sd.iBan.replace(' ERROR:', '')} {bc.GC}{self.Config.UIFilePath}/{bc.BC} has already been moved to {bc.GC}{self.Config.WebServerPath}{bc.BC}\n")
		else:
			self.Cmd.Quit(self.Error.Throw("ui_file_move_failed", [self.Config.UIFilePath, self.Config.WebServerPath]))
	
	def CreateDatabaseTables(self):
		self.Database = DBManager()
		self.TableCreation = self.Database.CreateTables()

		if(self.TableCreation["status"]):
			for self.Table in self.TableCreation["data"]:
				print(self.Table)
			self.SetupStatus = f"{sd.sBan} Setup successful"
		elif(self.TableCreation["status"] == None):
			for self.Table in self.TableCreation["data"]:
				print(self.Table)
			self.SetupStatus = f"{sd.iBan} {self.Config.AppName} Setup has already been executed previously"
		else:
			for self.Error in self.TableCreation["errors"]:
				print(self.Error)
			self.SetupStatus = None

		if(self.SetupStatus != None):
			print(f"\n{self.SetupStatus}\n\n{sd.iBan} Run {self.Config.AppName}: {bc.GC}sudo python3 glassFrog.py{bc.BC}")
			print(f"{sd.iBan} Run {self.Config.UIFilePath} Web Server: {bc.GC}sudo python3 server.py{bc.BC}")
		else:
			print(f"{sd.eBan} Setup failed")
		
		quit()

if(__name__ == "__main__"):
	def Initiate():
		Run = SetupGlassFrog()

		try:
			Run.DependencyInstall()
			Run.MoveUIFiles()
			Run.CreateDatabaseTables()
		except KeyboardInterrupt:
			print(f"{bc.RC} Setup Aborted\n")
			quit()

	Command().Clear()
	Initiate()
