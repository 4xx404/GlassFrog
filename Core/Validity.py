class Validation:
    def __init__(self):
        self.Error = None

    def NotEmpty(self, Object: str or list or dict):
        self.Object: str or list or dict = Object

        if(type(self.Object) == str):
            if(self.Object != "" or self.Object != " "):
                return True
            else:
                return False
        elif(type(self.Object) == list):
            if(len(self.Object) > 0):
                return True
            else:
                return False
        elif(type(self.Object) == dict):
            if(len(self.Object.keys()) > 0):
                return True
            else:
                return False

    def HasProtocol(self, Link: str):
        self.Link: str = Link

        if(self.Link.startswith("http://") or self.Link.startswith("https://")):
            return True
        else:
            return False