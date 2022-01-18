#!/usr/bin/python3
import subprocess, sys
sys.dont_write_bytecode = True

from Core.Styling.Banners import sd
from Core.Styling.Colors import bc

from Core.Config import CoreConfig
from Core.Commands import Command
from Core.Error import ErrorHandler

class GlassFrogServer:
	def __init__(self):
		self.Config = CoreConfig()
		self.Cmd = Command()
		self.Error = ErrorHandler()

	def CreateProcess(self):
		print(f"\n{sd.iBan} Press {bc.GC}CTRL + C{bc.BC} to stop the server\n")
		if(self.Cmd.ChangeDirectory(self.Config.WebServerPath)):
			try:
				subprocess.call(["php", "-S", f"{self.Config.ServerHost}:{self.Config.ServerPort}"])
			except Exception:
				self.Cmd.Clear()
				print(self.Error.Throw("server_connect_failed", self.Config.AppName))
				quit()
		else:
			self.Cmd.Clear()
			print(self.Error.Throw("change_directory_failed", self.Config.WebServerPath))
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
