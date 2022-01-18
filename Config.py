import datetime, random, string
import re

class CoreConfig:
    def __init__(self):
        self.AppName = "GlassFrog"
        self.Version = "V3"

        self.Headers = {
            "Accept-Language": "en-US,en;q=0.5",
            "Cache-Control": "no-cache",
            "User-Agent": f"{self.AppName}.{self.Version}"
        }

        self.UnknownDataAnalysisFilePath = "DataAnalysis/UNKNOWN-TYPE-DATA.txt"
        self.RequirementsFilePath = "Core/requirements.txt"

        self.WebServerPath = "/var/www/html/"
        self.UIFilePath = f"{self.AppName}-UI"
        self.DatabasePath = f"db/{self.AppName}.db"

        self.AbsoluteUIFilePath = f"{self.WebServerPath}{self.UIFilePath}"
        self.AbsoluteDatabasePath = f"{self.AbsoluteUIFilePath}/{self.DatabasePath}"

        # Server Config
        self.ServerHost = "localhost"
        self.ServerPort = 80 
        self.ServerLink = f"http://{self.ServerHost}:{self.ServerPort}/{self.UIFilePath}/{self.AppName}.php"

        # Default Manipulation Strings
        self.HTMLTags = ["a", "p", "q", "span", "h1", "h2", "h3", "h4", "h5", "h6", "span", "strong"]
        self.Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.RemovableChars = [".", "..", "...", ",", "?", "？", ":", ";", "\"", "'", "~", "[", "]", "{", "}", "|", "`", "!", "%", "^", "&", "*", "(", ")", "((", "))", "-", "©", "‘", "’", "“", "”", "„", "†", "‡", "‰", "‹", "›", "♠", "♣", "♥", "♦", "‾", "_", "–", "←", "↑", "→", "↓", "™", "\"", "&", "¡", "¢", "¤", "¥", "¦", "§", "¨", "¨", "ª", "«", "»", "¬", "®", "¯", "°", "±", "¹", "²", "³", "´", "µ", "¶", "·", "¸", "º", "¼", "½", "¾", "¿", "À", "Á", "Â", "Ã", "Ä", "Å", "Æ", "Ç", "È", "É", "Ê", "Ë", "Ì", "Í", "Î", "Ï", "Ð", "Ñ", "Ò", "Ó", "Ô", "Õ", "Ö", "×", "Ø", "Ù", "Ú", "Û", "Ü", "Ý", "Þ", "ß", "à", "á", "â", "ã", "ä", "å", "æ", "ç", "è", "é", "ê", "ë", "ì", "í", "î", "ï", "ð", "ñ", "ò", "ó", "ô", "õ", "ö", "÷", "ø", "ù", "ú", "û", "ü", "ý", "þ", "ÿ", "👊", "😍", "😍", "❤️", "❤", "❤️❤"]
        self.DomainExtensions = [".com", ".net", ".edu", ".org", ".gov", ".int", ".mil", ".aero", ".cat", ".asia", ".mobi", ".coop", ".travel", ".tel", ".jobs", ".pro", ".biz", ".info", ".store", ".me", ".co", ".co.uk", ".online", ".xyz", ".site", ".club", ".shop", ".app", ".live", ".ac", ".ad", ".ae", ".af", ".ag", ".ai", ".al", ".am", ".an", ".ao", ".aq", ".ar", ".as", ".at", ".au", ".aw", ".ax", ".az", ".ba", ".bb", ".bd", ".be", ".bf", ".bg", ".bh", ".bi", ".bj", ".bl", ".bm", ".bn", ".bo", ".br", ".bq", ".bs", ".bt", ".bv", ".bw", ".by", ".bz", ".ca", ".cc", ".cd", ".cf", ".cg", ".ch", ".ci", ".ck", ".cl", ".cm", ".cn", ".co", ".cr", ".cs", ".cu", ".cv", ".cw", ".cx", ".cy", ".cz", ".dd", ".de", ".dj", ".dk", ".dm", ".do", ".dz", ".ec", ".ee", ".eg", ".eh", ".er", ".es", ".et", ".eu", ".fi", ".fj", ".fk", ".fm", ".fo", ".fr", ".ga", ".gb", ".gd", ".ge", ".gf", ".gg", ".gh", ".gi", ".gl", ".gm", ".gn", ".gp", ".gq", ".gr", ".gs", ".gt", ".gu", ".gw", ".gy", ".hk", ".hm", ".hn", ".hr", ".ht", ".hu", ".id", ".ie", ".il", ".im", ".in", ".io", ".iq", ".ir", ".is", ".it", ".je", ".jm", ".jo", ".jp", ".ke", ".kg", ".kh", ".ki", ".km", ".kn", ".kp", ".kr", ".kw", ".ky", ".kz", ".la", ".lb", ".lc", ".li", ".lk", ".lr", ".ls", ".lt", ".lu", ".lv", ".ly", ".ma", ".mc", ".me", ".mf", ".mg", ".mh", ".mk", ".ml", ".mm", ".mn", ".mo", ".mp", ".mq", ".mr", ".ms", ".mt", ".mu", ".mv", ".mw", ".mx", ".my", ".mz", ".na", ".nc", ".ne", ".nf", ".ng", ".ni", ".nl", ".no", ".np", ".nr", ".nu", ".nz", ".om", ".pa", ".pe", ".pf", ".pg", ".ph", ".pk", ".pm", ".pn", ".pr", ".ps", ".pt", ".pw", ".qa", ".re", ".ro", ".rs", ".ru", ".rw", ".sa", ".sb", ".sc", ".sd", ".se", ".sg", ".si", ".sj", ".sk", ".sl", ".sm", ".sn", ".so", ".sr", ".ss", ".st", ".su", ".sv", ".sx", ".sy", ".sz", ".tc", ".td", ".tf", ".tg", ".th", ".tj", ".tk", ".tl", ".tm", ".tn", ".to", ".tp", ".tr", ".tt", ".tv", ".tw", ".tz", ".ua", ".ug", ".uk", ".um", ".us", ".uy", ".uz", ".va", ".vc", ".ve", ".vg", ".vi", ".vn", ".vu", ".wf", ".ws", ".ye", ".yt", ".yu", ".za", ".zm", ".zr", ".zw"]
        self.EmailDomains = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@aol.com", "@hotmail.co.uk", "@hotmail.fr", "@msn.com", "@yahoo.fr", "@wanadoo.fr", "@orange.fr", "@comcast.net", "@yahoo.co.uk", "@yahoo.com.br", "@yahoo.co.in", "@live.com", "@rediffmail.com", "@free.fr", "@gmx.de", "@web.de", "@yandex.ru", "@ymail.com", "@libero.it", "@outlook.com", "@uol.com.br", "@bol.com.br", "@mail.ru", "@cox.net", "@hotmail.it", "@sbcglobal.net", "@sfr.fr", "@live.fr", "@verizon.net", "@live.co.uk", "@googlemail.com", "@yahoo.es", "@ig.com.br", "@protonmail.com", "@live.nl", "@bigpond.com", "@terra.com.br", "@yahoo.it", "@neuf.fr", "@yahoo.de", "@alice.it", "@rocketmail.com", "@att.net", "@laposte.net", "@facebook.com", "@fb.com", "@bellsouth.net", "@yahoo.in", "@hotmail.es", "@charter.net", "@yahoo.ca", "@yahoo.com.au", "@rambler.ru", "@hotmail.de", "@tiscali.it", "@shaw.ca", "@yahoo.co.jp", "@sky.com", "@earthlink.net", "@optonline.net", "@freenet.de", "@t-online.de", "@aliceadsl.fr", "@virgilio.it", "@home.nl", "@qq.com", "@telenet.be", "@me.com", "@yahoo.com.ar", "@tiscali.co.uk", "@yahoo.com.mx", "@voila.fr", "@gmx.net", "@mail.com", "@planet.nl", "@tin.it", "@live.it", "@ntlworld.com", "@arcor.de", "@yahoo.co.id", "@frontiernet.net", "@hetnet.nl", "@live.com.au", "@yahoo.com.sg", "@club-internet.fr", "@optusnet.com.au", "@blueyonder.co.uk", "@bluewin.ch", "@skynet.be", "@sympatico.ca", "@windstream.net", "@mac.com", "@centurytel.net", "@chello.nl", "@live.ca", "@aim.com", "@bigpond.net.au"]
        self.PhoneCodes = ["+1", "+1 340", "+1-340", "+1 670", "+1-670", "+1 787", "+1-787", "+1 868", "+1-868", "+20", "+212", "+213", "+216", "+218", "+220", "+221", "+222", "+223", "+224", "+225", "+226", "+227", "+228", "+229", "+230", "+231", "+232", "+233", "+234", "+235", "+236", "+237", "+238", "+239", "+240", "+241", "+242", "+243", "+244", "+245", "+246", "+247", "+248", "+249", "+250", "+251", "+252", "+253", "+254", "+255", "+256", "+257", "+258", "+260", "+261", "+262", "+263", "+264", "+265", "+266", "+267", "+268", "+269", "+27", "+284", "+290", "+291", "+297", "+298", "+299", "+30", "+31", "+32", "+33", "+34", "+345", "+350", "+351", "+352", "+353", "+354", "+355", "+356", "+357", "+358", "+359", "+36", "+370", "+371", "+372", "+373", "+374", "+375", "+376", "+378", "+380", "+381", "+385", "+386", "+387", "+389", "+39", "+40", "+41", "+420", "+421", "+423", "+43", "+44", "+45", "+46", "+47", "+473", "+48", "+49", "+500", "+501", "+502", "+503", "+504", "+505", "+506", "+507", "+508", "+509", "+51", "+52", "+53", "+54", "+55", "+56", "+57", "+58", "+591", "+592", "+593", "+594", "+595", "+596", "+597", "+598", "+599", "+60", "+61", "+62", "+63", "+64", "+65", "+66", "+670", "+671", "+672", "+673", "+674", "+675", "+676", "+677", "+678", "+679", "+680", "+681", "+682", "+683", "+684", "+685", "+686", "+687", "+688", "+689", "+690", "+691", "+692", "+7", "+767", "+809", "+81", "+82", "+84", "+850", "+852", "+853", "+855", "+856", "+86", "+869", "+876", "+880", "+886", "+90", "+91", "+92", "+93", "+94", "+95", "+960", "+961", "+962", "+963", "+964", "+965", "+966", "+967", "+968", "+971", "+972", "+973", "+974", "+975", "+976", "+977", "+98", "+993", "+994", "+995", "+996"]

        self.KnownSocialMediaWebsites = ["facebook.com", "instagram.com", "twitter.com", "snapchat.com", "linkedin.com", "youtube.com"]

        self.BranchSetKey = None

        self.WebsiteToolList = [
            "portscanner",
            "whois",
            "web_history"
        ]
        
    def GetDateTime(self):
        return str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def CreateKey(self, Length: int or str = 10):
        self.BranchSetKey = ''.join(random.choices(string.ascii_lowercase + string.digits, k = int(Length)))
        return self.BranchSetKey
    
    def GetKey(self, Length: int or str = 0):
        self.Length: int = int(Length)

        if(self.BranchSetKey != None and len(self.BranchSetKey) == self.Length):
            return self.BranchSetKey
        elif(self.Length != 0):
            return self.CreateKey(self.Length)