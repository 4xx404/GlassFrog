#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time, string, random
from datetime import datetime
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup
import requests
from modules.connectDB import database
from tld import get_fld

class bc:
	GC = '\033[1;39m'
	BC = '\033[1;34m'
	RC = '\033[1;31m'

iBan = bc.BC + " [" + bc.GC + "?" + bc.BC + "]"
sBan = bc.BC + " [" + bc.GC + u'\u2713' + bc.BC + "]"
eBan = bc.BC + " [" + bc.RC + u'\u2717' + bc.BC + "]"

author = bc.BC + "\n Author: " + bc.RC + "4" + bc.GC + "x" + bc.BC + "x" + bc.RC + "4" + bc.GC + "0" + bc.BC + "4\n"
version = bc.BC + " Version: " + bc.RC + "2" + bc.GC + "." + bc.BC + "0\n"
github = bc.BC + " Github: " + bc.RC + "h" + bc.GC + "t" + bc.BC + "t" + bc.RC + "p" + bc.GC + "s" + bc.BC + ":" + bc.RC + "/" + bc.GC + "/" + bc.BC + "g" + bc.RC + "i" + bc.GC + "t" + bc.BC + "h" + bc.RC + "u" + bc.GC + "b" + bc.BC + "." + bc.RC + "c" + bc.GC + "o" + bc.BC + "m" + bc.RC + "/" + bc.GC + "4" + bc.BC + "x" + bc.RC + "x" + bc.GC + "4" + bc.BC + "0" + bc.RC + "4\n"

banner = bc.RC + '''
''' + bc.GC + '''   ___  __      __    ___  ___  ____  ____  _____  ___     _   _   
''' + bc.BC + '''  / __)(  )    /__\  / __)/ __)( ___)(  _ \(  _  )/ __)   (.)_(.)  
''' + bc.RC + ''' ( (_-. )(__  /(__)\ \__ \\\__ \ )__)  )   / )(_)(( (_-.  (   _   ) 
''' + bc.GC + '''  \___/(____)(__)(__)(___/(___/(__)  (_)\_)(_____)\___/  /`-----'\ 
''' + author + version + github

class scanContent:
	def __init__(self, branch, branch_key):
		self.branchDB = database()
		self.branch = branch
		self.branch_set_key = branch_key
		self.content_date = datetime.now()
		self.content_date = self.content_date.strftime("%d/%m/%Y %H:%M:%S")
		self.content_id = self.branch_set_key
		self.headers = {'Accept-Language': 'en-US,en;q=0.5', 'Cache-Control': 'no-cache', 'User-Agent': 'GlassFrog.V2'}

		self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		self.removeChars = ['.', '..', '...', ',', '<', '>', '?', '？', ':', ';', '"', "'", '~', '[', ']', '{', '}', '|', '`', '!', '%', '^', '&', '*', '(', ')', '((', '))' '-', '©', '‘', '’', '“', '”', '„', '†', '‡', '‰', '‹' ,'›' ,'♠' ,'♣' ,'♥' ,'♦' ,'‾', '_', '–', '←', '↑', '→', '↓', '™', '"', '&', '¡', '¢', '¤', '¥', '¦', '§', '¨', '¨', 'ª', '«', '»', '¬', '®', '¯', '°', '±', '¹', '²', '³', '´', 'µ', '¶', '·', '¸', 'º', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ', 'ÿ', '👊', '😍', '😍', '❤️', '❤', '❤️❤']
		self.domains = ['.com', '.net', '.edu', '.org', '.gov', '.int', '.mil', '.aero', '.cat', '.asia', '.mobi', '.coop', '.travel', '.tel', '.jobs', '.pro', '.biz', '.info', '.store', '.me', '.co', '.online', '.xyz', '.site', '.club', '.shop', '.app', '.live', '.ac', '.ad', '.ae', '.af', '.ag', '.ai', '.al', '.am', '.an', '.ao', '.aq', '.ar', '.as', '.at', '.au', '.aw', '.ax', '.az', '.ba', '.bb', '.bd', '.be', '.bf', '.bg', '.bh', '.bi', '.bj', '.bl', '.bm', '.bn', '.bo', '.br', '.bq', '.bs', '.bt', '.bv', '.bw', '.by', '.bz', '.ca', '.cc', '.cd', '.cf', '.cg', '.ch', '.ci', '.ck', '.cl', '.cm', '.cn', '.co', '.cr', '.cs', '.cu', '.cv', '.cw', '.cx', '.cy', '.cz', '.dd', '.de', '.dj', '.dk', '.dm', '.do', '.dz', '.ec', '.ee', '.eg', '.eh', '.er', '.es', '.et', '.eu', '.fi', '.fj', '.fk', '.fm', '.fo', '.fr', '.ga', '.gb', '.gd', '.ge', '.gf', '.gg', '.gh', '.gi', '.gl', '.gm', '.gn', '.gp', '.gq', '.gr', '.gs', '.gt', '.gu', '.gw', '.gy', '.hk', '.hm', '.hn', '.hr', '.ht', '.hu', '.id', '.ie', '.il', '.im', '.in', '.io', '.iq', '.ir', '.is', '.it', '.je', '.jm', '.jo', '.jp', '.ke', '.kg', '.kh', '.ki', '.km', '.kn', '.kp', '.kr', '.kw', '.ky', '.kz', '.la', '.lb', '.lc', '.li', '.lk', '.lr', '.ls', '.lt', '.lu', '.lv', '.ly', '.ma', '.mc', '.me', '.mf', '.mg', '.mh', '.mk', '.ml', '.mm', '.mn', '.mo', '.mp', '.mq', '.mr', '.ms', '.mt', '.mu', '.mv', '.mw', '.mx', '.my', '.mz', '.na', '.nc', '.ne', '.nf', '.ng', '.ni', '.nl', '.no', '.np', '.nr', '.nu', '.nz', '.om', '.pa', '.pe', '.pf', '.pg', '.ph', '.pk', '.pm', '.pn', '.pr', '.ps', '.pt', '.pw', '.qa', '.re', '.ro', '.rs', '.ru', '.rw', '.sa', '.sb', '.sc', '.sd', '.se', '.sg', '.si', '.sj', '.sk', '.sl', '.sm', '.sn', '.so', '.sr', '.ss', '.st', '.su', '.sv', '.sx', '.sy', '.sz', '.tc', '.td', '.tf', '.tg', '.th', '.tj', '.tk', '.tl', '.tm', '.tn', '.to', '.tp', '.tr', '.tt', '.tv', '.tw', '.tz', '.ua', '.ug', '.uk', '.um', '.us', '.uy', '.uz', '.va', '.vc', '.ve', '.vg', '.vi', '.vn', '.vu', '.wf', '.ws', '.ye', '.yt', '.yu', '.za', '.zm', '.zr', '.zw']
		self.htmlTags = ['a', 'p', 'q', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
		
		## EMAILS ## work on
		self.emailDomains = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@aol.com', '@hotmail.co.uk', '@hotmail.fr', '@msn.com', '@yahoo.fr', '@wanadoo.fr', '@orange.fr', '@comcast.net', '@yahoo.co.uk', '@yahoo.com.br', '@yahoo.co.in', '@live.com', '@rediffmail.com', '@free.fr', '@gmx.de', '@web.de', '@yandex.ru', '@ymail.com', '@libero.it', '@outlook.com', '@uol.com.br', '@bol.com.br', '@mail.ru', '@cox.net', '@hotmail.it', '@sbcglobal.net', '@sfr.fr', '@live.fr', '@verizon.net', '@live.co.uk', '@googlemail.com', '@yahoo.es', '@ig.com.br', '@protonmail.com', '@live.nl', '@bigpond.com', '@terra.com.br', '@yahoo.it', '@neuf.fr', '@yahoo.de', '@alice.it', '@rocketmail.com', '@att.net', '@laposte.net', '@facebook.com', '@fb.com', '@bellsouth.net', '@yahoo.in', '@hotmail.es', '@charter.net', '@yahoo.ca', '@yahoo.com.au', '@rambler.ru', '@hotmail.de', '@tiscali.it', '@shaw.ca', '@yahoo.co.jp', '@sky.com', '@earthlink.net', '@optonline.net', '@freenet.de', '@t-online.de', '@aliceadsl.fr', '@virgilio.it', '@home.nl', '@qq.com', '@telenet.be', '@me.com', '@yahoo.com.ar', '@tiscali.co.uk', '@yahoo.com.mx', '@voila.fr', '@gmx.net', '@mail.com', '@planet.nl', '@tin.it', '@live.it', '@ntlworld.com', '@arcor.de', '@yahoo.co.id', '@frontiernet.net', '@hetnet.nl', '@live.com.au', '@yahoo.com.sg', '@club-internet.fr', '@optusnet.com.au', '@blueyonder.co.uk', '@bluewin.ch', '@skynet.be', '@sympatico.ca', '@windstream.net', '@mac.com', '@centurytel.net', '@chello.nl', '@live.ca', '@aim.com', '@bigpond.net.au', '.tv']
		
		#Phone Codes are more difficult to format, this will be added soon
		self.phoneCodes = ['+1', '+1 340', '+1-340', '+1 670', '+1-670', '+1 787', '+1-787', '+1 868', '+1-868', '+20', '+212', '+213', '+216', '+218', '+220', '+221', '+222', '+223', '+224', '+225', '+226', '+227', '+228', '+229', '+230', '+231', '+232', '+233', '+234', '+235', '+236', '+237', '+238', '+239', '+240', '+241', '+242', '+243', '+244', '+245', '+246', '+247', '+248', '+249', '+250', '+251', '+252', '+253', '+254', '+255', '+256', '+257', '+258', '+260', '+261', '+262', '+263', '+264', '+265', '+266', '+267', '+268', '+269', '+27', '+284', '+290', '+291', '+297', '+298', '+299', '+30', '+31', '+32', '+33', '+34', '+345', '+350', '+351', '+352', '+353', '+354', '+355', '+356', '+357', '+358', '+359', '+36', '+370', '+371', '+372', '+373', '+374', '+375', '+376', '+378', '+380', '+381', '+385', '+386', '+387', '+389', '+39', '+40', '+41', '+420', '+421', '+423', '+43', '+44', '+45', '+46', '+47', '+473', '+48', '+49', '+500', '+501', '+502', '+503', '+504', '+505', '+506', '+507', '+508', '+509', '+51', '+52', '+53', '+54', '+55', '+56', '+57', '+58', '+591', '+592', '+593', '+594', '+595', '+596', '+597', '+598', '+599', '+60', '+61', '+62', '+63', '+64', '+65', '+66', '+670', '+671', '+672', '+673', '+674', '+675', '+676', '+677', '+678', '+679', '+680', '+681', '+682', '+683', '+684', '+685', '+686', '+687', '+688', '+689', '+690', '+691', '+692', '+7', '+767', '+809', '+81', '+82', '+84', '+850', '+852', '+853', '+855', '+856', '+86', '+869', '+876', '+880', '+886', '+90', '+91', '+92', '+93', '+94', '+95', '+960', '+961', '+962', '+963', '+964', '+965', '+966', '+967', '+968', '+971', '+972', '+973', '+974', '+975', '+976', '+977', '+98', '+993', '+994', '+995', '+996']
		self.createEmailDomain = '@' + get_fld(self.branch)
		self.emailDomains.append(self.createEmailDomain)

	def searchData(self):
		self.duplicateScanned = []
		self.analysisDuplicates = []
		self.noPrint = []
		try:
			self.res = requests.get(self.branch, self.headers)
			self.soup = BeautifulSoup(self.res.content, 'html.parser')
			if(self.res.status_code == 200):
				for self.result in self.soup.find_all(self.htmlTags):
					self.words = str(self.result.text.replace('\n', '').replace('\t', '').replace('\n ', '').lower()).split()
					for self.word in self.words:
						if(self.word != ''):
							if(self.word.startswith(tuple(self.removeChars))):
								self.word = self.word[0:]
							elif(self.word.endswith(tuple(self.removeChars))):
								self.word = self.word[:-1]
							else:
								self.word = self.word

							if(self.word in self.alphabet):
								self.no_analysis = True
								self.ignoreStorage = True
								self.dataType = 'SINGLE_ALPHABET_VALUE'
								self.dat = self.word
								self.url = self.branch
							elif(self.word.startswith('@') and self.word != '@'):
								self.no_analysis = True
								self.ignoreStorage = False
								self.dataType = 'USERNAME_HANDLE'
								self.dat = self.word
								self.url = self.branch
								self.printOnce = False
							elif('@' in self.word and self.word.endswith(tuple(self.emailDomains))):
								if(self.word != '@'):
									if(self.word.startswith('mailto:')):
										self.word = self.word.replace('mailto:', '')
									else:
										self.word = self.word

									self.no_analysis = True
									self.ignoreStorage = False
									self.dataType = 'EMAIL'
									self.dat = self.word
									self.url = self.branch
								else:
									continue
							elif(self.word.endswith(tuple(self.domains))):
								if(not self.word.startswith(tuple(self.domains))):
									self.no_analysis = True
									self.ignoreStorage = False
									self.dataType = 'DOMAIN'
									self.dat = self.word
									self.url = self.branch
								else:
									continue
							elif(self.word.startswith(tuple(self.phoneCodes)) or self.word.startswith('tel:')):
								if(len(self.word) > 10 and len(self.word) < 15):
									self.no_analysis = True
									self.ignoreStorage = False
									self.dataType = 'PHONE_NUMBER'
									self.dat = self.word
									self.url = self.branch
								else:
									continue
							elif(self.word.startswith('1')):
								if(len(self.word) >= 25 and len(self.word) <= 34):
									self.no_analysis = True
									self.ignoreStorage = False
									self.dataType = 'BITCOIN_ADDRESS'
									self.dat = self.word
									self.url = self.branch
								else:
									continue
								
							else:
								self.no_analysis = False
								self.ignoreStorage = False
								self.dataType = 'UNKNOWN_DATA_TYPE'
								self.dat = self.word
								self.url = self.branch

							if(self.dat not in self.duplicateScanned):
								if(self.no_analysis == True and self.ignoreStorage == False):
									if(self.dat.startswith(tuple(self.removeChars))):
										self.dat = self.word[0:] 
									elif(self.dat.endswith(tuple(self.removeChars))):
										self.dat = self.word[:-1]
									else:
										self.dat = self.word
										
									if(self.dat not in self.noPrint and self.dataType != 'UNKNOWN_DATA_TYPE' and self.dataType != 'SINGLE_ALPHABET_VALUE'):
										print(sBan + ' ' + self.dataType + ': ' + bc.GC + self.dat)
										self.noPrint.append(self.dat)

									self.branchDB.db.execute("INSERT OR IGNORE INTO branch_data(CONTENT_ID, DATATYPE, BRANCH_URL, BRANCH_SET_KEY, DATA, DATA_DATE) VALUES ('" + self.content_id + "', '" + self.dataType + "', '" + self.url + "', '" + self.branch_set_key + "', '" + self.dat + "', '" + self.content_date + "')")
									self.branchDB.db.commit()
									self.duplicateScanned.append(self.dat)
								else:
									if(self.dat not in self.analysisDuplicates):
										self.xFile = open('data-analysis/UNKNOWN-TYPE-DATA.txt', 'a+')
										self.xFile.write(self.dat + '\n')
										self.xFile.close()
										self.analysisDuplicates.append(self.dat)
									else:
										continue
							else:
								continue
						else:
							continue
			else:
				pass
		except Exception:
			pass
			##add more tags to collect from that cant be interated over from htmlTags list
			#for self.img in self.soup.find_all('img', src=True):
			#	print(' Found an image: ' + str(self.img["src"]))
