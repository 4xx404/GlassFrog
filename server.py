#!/usr/bin/python3
import subprocess, sys
sys.dont_write_bytecode = True

from Core.Styling.Banners import sd
from Core.Styling.Colors import bc

from Core.Config import CoreConfig
from Core.Commands import Command

class GlassFrogServer:
	def __init__(self):
		self.Config = CoreConfig()
		self.Cmd = Command()

	def ThrowError(self, ErrorType: str, ErrorData: str or list = None):
		self.ErrorType: str = ErrorType.lower()
		self.ErrorData: str = ErrorData

		self.DefinedErrors = [
			"server_connect_failed",
			"change_directory_failed",
		]

		if(self.ErrorType in self.DefinedErrors):
			if(self.ErrorType == "server_connect_failed"):
				return f"{sd.eBan} Failed to connect to the {bc.RC}{self.ErrorData}{bc.BC} server"
			elif(self.ErrorType == "change_directory_failed"):
				return f"\n{sd.eBan} Failed to change directory to {bc.RC}{self.ErrorData}{bc.BC}"
			else:
				return f"{sd.eBan} Error Type {bc.RC}{self.ErrorType}{bc.BC} thrown without an error message defined"
		else:
			return f"{sd.eBan} Undefined Error Type {bc.RC}{self.ErrorType}{bc.BC}"

	def CreateProcess(self):
		print(f"\n{sd.iBan} Press {bc.GC}CTRL + C{bc.BC} to stop the server\n")
		if(self.Cmd.ChangeDirectory(self.Config.WebServerPath)):
			try:
				subprocess.call(["php", "-S", f"{self.Config.ServerHost}:{self.Config.ServerPort}"])
			except Exception:
				self.Cmd.Clear()
				print(self.ThrowError("server_connect_failed", self.Config.AppName))
				quit()
		else:
			self.Cmd.Clear()
			print(self.ThrowError("change_directory_failed", self.Config.WebServerPath))
			quit()

if(__name__ == '__main__'):
	def Initiate():
		Server = GlassFrogServer()

		try:
			print(f"{bc.BC} Interface URL: {bc.GC}{CoreConfig().ServerLink}{bc.BC}")
			Server.CreateProcess()
		except KeyboardInterrupt:
			Command().Clear()
			print(f"{sd.sBan} Server Stopped")
			quit()

	Command().Clear()
	Initiate()
