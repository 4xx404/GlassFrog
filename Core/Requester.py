from ctypes import LittleEndianStructure
from math import fabs
import re
import requests

from .Styling.Banners import sd
from .Styling.Colors import bc

from .Config import CoreConfig

class RequestHandler:
    def __init__(self):
        self.Config = CoreConfig()

    def ThrowError(self, ErrorType: str, ErrorData: str or list = None):
        self.ErrorType: str = ErrorType.lower() # Error Type to set Error Message
        self.ErrorData: str = ErrorData # Data to pass into the Error Message

        self.DefinedErrors = [
            "link_not_live",
            "no_response",
            "get_webpage_text_failed",
        ]

        # Defined Error Type
        if(self.ErrorType in self.DefinedErrors):
            #  Error Messages
            if(self.ErrorType == "link_not_live"):
                return f"{sd.eBan} URL {bc.RC}{self.ErrorData}{bc.BC} is not live"
            elif(self.ErrorType == "no_response"):
                return f"{sd.eBan} Got no response from {bc.RC}{self.ErrorData}{bc.BC}"

            elif(self.ErrorType == "get_webpage_text_failed"):
                return f"{sd.eBan} Failed to get webpage text from {bc.RC}{self.ErrorData}{bc.BC}"
    
            # Undefined Error Message
            else:
                return f"{sd.eBan} Error Type {bc.RC}{self.ErrorType}{bc.BC} thrown without an error message defined"
        # Undefined Error Type
        else:
            return f"{sd.eBan} Undefined Database Error Type {bc.RC}{self.ErrorType}{bc.BC}"

    def IsLive(self, Link: str):
        self.Link: str = Link

        try:
            self.Request = requests.get(self.Link, headers=self.Config.Headers)

            if(self.Request.status_code == 200):
                return True, self.Link
            else:
                return False, self.ThrowError("link_not_live", self.Link)
        except Exception:
            return False, self.ThrowError("link_no_response", self.Link)

    def GetPageData(self, ResponseType: str = "content", Link: str = ""):
        self.Type: str = ResponseType.lower()
        self.Link: str = Link

        self.ResponsePack = {
            "status": False,
            "data": "",
            "error": ""
        }

        self.LiveStatus, self.LiveStatusData = self.IsLive(self.Link)
        if(self.LiveStatus):
            try:
                self.Request = requests.get(self.LiveStatusData, headers=self.Config.Headers)

                if(self.Type == "content"):
                    self.ResponsePack["status"], self.ResponsePack["error"] = True, ""
                    self.ResponsePack["data"] = self.Request.content.decode()
                elif(self.Type == "text"):
                    self.ResponsePack["status"], self.ResponsePack["error"] = True, ""
                    self.ResponsePack["data"] = str(self.Request.text)
            except Exception:
                self.ResponsePack["status"], self.ResponsePack["data"] = False, ""
                self.ResponsePack["error"] = self.ThrowError("get_webpage_text_failed", self.Link)
        else:
            self.ResponsePack["status"], self.ResponsePack["data"] = self.LiveStatus, ""
            self.ResponsePack["error"] = self.LiveStatusData

        return self.ResponsePack