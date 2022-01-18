import requests

from .Config import CoreConfig
from .Error import ErrorHandler

class RequestHandler:
    def __init__(self):
        self.Config = CoreConfig()
        self.Error = ErrorHandler()

    def IsLive(self, Link: str):
        self.Link: str = Link

        try:
            self.Request = requests.get(self.Link, headers=self.Config.Headers)

            if(self.Request.status_code == 200):
                return True, self.Link
            else:
                return False, self.Error.Throw("link_not_live", self.Link)
        except Exception:
            return False, self.Error.Throw("link_no_response", self.Link)

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
                self.ResponsePack["error"] = self.Error.Throw("get_webpage_text_failed", self.Link)
        else:
            self.ResponsePack["status"], self.ResponsePack["data"] = self.LiveStatus, ""
            self.ResponsePack["error"] = self.LiveStatusData

        return self.ResponsePack
