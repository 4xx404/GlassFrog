from .Styling.Banners import sd

from .Config import CoreConfig

class BluePrinter:
    def __init__(self):
        self.Config = CoreConfig()

    def Content(self, Analysis: bool, Storage: bool, DataType: str, Data: str, BranchURL: str):
        return {
            "analysis": Analysis,
            "storage": Storage,
            "type": DataType,
            "data": Data,
            "branch": BranchURL
        }

    def MatchesSingleAlphabetType(self, Object: str):
        self.Object: str = Object

        if(self.Object in self.Config.Alphabet):
            return True
        else:
            return False

    def MatchesUsernameType(self, Object: str):
        self.Object: str = Object

        if(self.Object.startswith("@") and len(self.Word) > 1):
            return True
        else:
            return False

    def MatchesEmailType(self, Object: str):
        self.Object: str = Object

        if("@" in self.Word and len(self.Word) > 1):
            if(self.Word.startswith("mailto:") or self.Word.startswith("mailto: ")):
                return True    
            elif(self.Word.endswith(tuple(self.Config.EmailDomains)) or self.Word.endswith(tuple(self.Config.DomainExtensions))):
                return True
            else:
                return False
        else:
            return False

    def MatchesDomainType(self, Object: str):
        self.Object: str = Object

        if(self.Object.endswith(tuple(self.Config.DomainExtensions))):
            if(not self.Object.startswith(tuple(self.Config.DomainExtensions))):
                return True
            else:
                return False
        else:
            return False

    def MatchesPhoneCodeType(self, Object: str):
        self.Object: str = Object

        if(self.Object.startswith(tuple(self.Config.PhoneCodes)) or self.Object.startswith("tel:") or self.Object.startswith("tel: ")):
            if(len(self.Word) > 10 and len(self.Word) < 15):
                return True
            else:
                return False
        else:
            return False
    
    def MatchesBitcoinAddress(self, Object: str):
        self.Object: str = Object

        if(self.Object.startswith("1")):
            if(len(self.Object) >= 25 and len(self.Object) <= 34):
                return True
            else:
                return False
        else:
            return False

    def SetFormat(self, Word: str, Branch: str):
        self.Word: str = Word
        self.Branch: str = Branch 

        if(self.MatchesSingleAlphabetType(self.Word)):
            self.ProtoType: dict = self.Content(Analysis=True, Storage=True, DataType="SINGLE_ALPHABET_VALUE", Data=self.Word, BranchURL=self.Branch)
        elif(self.MatchesUsernameType(self.Word)):
            self.ProtoType: dict = self.Content(Analysis=True, Storage=False, DataType="USERNAME_HANDLE", Data=self.Word, BranchURL=self.Branch)
        elif(self.MatchesEmailType(self.Word)):
            self.ProtoType: dict = self.Content(Analysis=True, Storage=False, DataType="EMAIL", Data=self.Word.replace("mailto:", "").replace("mailto: ", ""), BranchURL=self.Branch)
        elif(self.MatchesDomainType(self.Word)):
            self.ProtoType: dict = self.Content(Analysis=True, Storage=False, DataType="DOMAIN", Data=self.Word, BranchURL=self.Branch)
        elif(self.MatchesPhoneCodeType(self.Word)):
            self.ProtoType: dict = self.Content(Analysis=True, Storage=False, DataType="PHONE_NUMBER", Data=self.Word, BranchURL=self.Branch)
        elif(self.MatchesBitcoinAddress(self.Word)):
            self.ProtoType: dict = self.Content(Analysis=True, Storage=False, DataType="BITCOIN_ADDRESS", Data=self.Word, BranchURL=self.Branch)
        else:
            self.ProtoType: dict = self.Content(Analysis=False, Storage=False, DataType="UNKNOWN_DATA_TYPE", Data=self.Word, BranchURL=self.Branch)

#        print(f"{sd.sBan}{self.ProtoType['data']}")
        return self.ProtoType