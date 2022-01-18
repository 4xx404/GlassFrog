import os, shutil

from .Styling.Banners import sd
from .Styling.Colors import bc

from .Config import CoreConfig

class Command:
    def __init__(self):
        self.Config = CoreConfig()

#   DEBUGGER USAGE
#   self.Cmd.Debug(ShouldQuit=False, DebugFile="FileName.py", DebugLine=100, DebugData=self.ProtoType)
    def Debug(self, ShouldQuit: bool = False, DebugFile = "", DebugLine = 0, DebugData: str or list or dict = None):
        self.ShouldQuit: bool = ShouldQuit
        self.DebugFile: str = DebugFile
        self.DebugLine: int = DebugLine
        self.DebugData: str or list or dict = DebugData

        if(type(self.DebugData) == str):
            self.TrueDebugString: str = self.DebugData
        elif(type(self.DebugData) == list):
            self.TrueDebugString: list = self.DebugData
        elif(type(self.DebugData) == dict):
            self.TrueDebugString: dict = self.DebugData

        if(self.ShouldQuit):
            self.Quit(self.TrueDebugString, Debugger=True)
        else:
            if(self.DebugFile != "" and self.DebugLine != 0):
                print(f"\n{sd.sBan} Debugger Started...\n @File: {bc.GC}{self.DebugFile}{bc.BC} | @Line: {bc.GC}{self.DebugLine}{bc.BC}")
            else:
                print(f"{sd.sBan} Debugger Started...\n")

            if(type(self.TrueDebugString) == str):
                print(f" DEBUGGER: {self.TrueDebugString}")
            elif(type(self.TrueDebugString) == list):    
                for self.ErrorItem in self.TrueDebugString:
                    print(f"{sd.eBan.replace(' ERROR:', '')} {self.ErrorItem}")
            elif(type(self.TrueDebugString) == dict):
                for self.Key, self.Value in self.TrueDebugString.items():
                    print(f"{sd.eBan.replace(' ERROR:', '')} {self.Key} : {self.Value}")

            print(f" @File: {bc.GC}{self.DebugFile}{bc.BC} | @Line: {bc.GC}{self.DebugLine}{bc.BC}\n{sd.sBan} Debugger Finished...\n")

    def InstallPythonDependencies(self):
        try:
            os.system(f"python3 -m pip install -r {self.Config.RequirementsFilePath}")
        except Exception:
            self.Clear()
            return False

        self.Clear()
        return True

    def Clear(self, Message: str = None):
        self.Message: str = Message

        os.system("clear")
        print(sd.Logo)

        if(self.Message != None):
            print(self.Message)

    def Quit(self, ErrorMessage: str or list or dict = None, Debugger: bool = False):
        self.ErrorMessage: str or list or dict = ErrorMessage
        self.Debugger: bool = Debugger

        self.Clear()
        if(self.ErrorMessage != None and self.Debugger == False):
            if(type(self.ErrorMessage) == str):
                print(f"{self.ErrorMessage}")
            elif(type(self.ErrorMessage) == list):
                for self.ErrorItem in self.ErrorMessage:
                    print(f"{sd.eBan} {self.ErrorItem}")
            elif(type(self.ErrorMessage) == dict):
                for self.Key, self.Value in self.ErrorMessage.items():
                    print(f"{sd.eBan} {self.Key} : {self.Value}")
        elif(self.ErrorMessage != None and self.Debugger == True):
            print(f"{sd.iBan} Debugger Data Type: {bc.GC}" + str(type(self.ErrorMessage)).replace("<class '", "").replace("'>", "").upper() + f"\n{bc.BC}")
            if(type(self.ErrorMessage) == str):
                print(f"{sd.eBan.replace(' ERROR:', ' DEBUGGER:')} {self.ErrorMessage}")
            elif(type(self.ErrorMessage) == list):
                for self.ErrorItem in self.ErrorMessage:
                    print(f"{sd.eBan.replace(' ERROR:', ' DEBUGGER:')} {self.ErrorItem}")
            elif(type(self.ErrorMessage) == dict):
                for self.Key, self.Value in self.ErrorMessage.items():
                    print(f"{sd.eBan.replace(' ERROR:', ' DEBUGGER:')} {self.Key} : {self.Value}")
        else:
            print(f" Closed {self.Config.AppName}")

        print(f"\n Closed {self.Config.AppName}")    
        quit()

    def ChangeDirectory(self, Location: str):
        self.Location: str = Location

        try:
            os.chdir(self.Location)
        except Exception:
            return False

        return True

    def MoveFile(self, FileToMove: str, Destination: str):
        self.FileToMove: str = FileToMove
        self.Destination: str = Destination

        try:
            shutil.move(self.FileToMove, self.Destination)
        except Exception as e:
            if("exists" in str(e).lower()):
                return None
            else:
                return False
        
        return True

    def RemoveDuplicateFileContent(self, FileName: str):
        self.FileName: str =  FileName

        try:
            os.system(f"sort {self.FileName} | uniq -d >> {self.FileName}")
        except Exception:
            return False
        
        return True