#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time, string, random
from datetime import datetime
import sqlite3
from tld import get_fld
from sqlite3 import Error
from bs4 import BeautifulSoup
import requests
from modules.connectDB import database
from modules.scanContent import scanContent

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

class collector:
	def __init__(self):
		self.branchDB = database()
		self.headers = {'Accept-Language': 'en-US,en;q=0.5', 'Cache-Control': 'no-cache', 'User-Agent': 'GlassFrog.V2'}

	def addBranches(self, base_url, keyword):
		self.base_url = base_url
		self.fld = get_fld(self.base_url)
		self.keyword = keyword
		self.datetime = datetime.now()
		self.datetime = self.datetime.strftime("%d/%m/%Y %H:%M:%S")
		self.N = 10
		self.branchSetKey = ''.join(random.choices(string.ascii_uppercase + string.digits, k = self.N))
		self.page = requests.get(self.base_url)
		self.soup = BeautifulSoup(self.page.content, 'html.parser')
		
		os.system('clear')
		print(banner)
		print(bc.BC + ' Base URL: ' + bc.GC + self.base_url)
		print(bc.BC + ' Keyword: ' + bc.GC + self.keyword.replace(' ', '') + '\n')
		print(bc.BC + ' Searching for Keyword...\n')
		self.branches = []
		self.duplicates = []

		self.totalBranchCount = 0
		self.totalKeywordFound = 0
		for self.x in self.soup.find_all('a', href=True):
			self.link = str(self.x["href"])
			try:
				if(self.link != ''):
					if(self.link == '#'):
						continue
					elif(self.link == '/'):
						continue
					elif(self.link.startswith('http://') or self.link.startswith('https://')):
						self.link = self.link
					elif(self.link.startswith('/')):
						self.link = self.base_url[:-1] + self.link
					elif(self.link.startswith('#')):
						self.link = self.base_url[:-1] + self.link
					else:
						self.link = None

					if(self.link not in self.duplicates and self.link != None):
						try:
							self.r = requests.get(self.link, self.headers)
						except Exception:
							continue
						if(self.r.status_code == 200):
							self.totalBranchCount += 1
							if(self.keyword in self.r.text):
								self.keywordFound = 'true'
								self.branchStatus = sBan + ' ' + bc.GC + self.link
								self.totalKeywordFound += 1
							else:
								self.keywordFound = 'false'
								self.branchStatus = eBan + ' ' + bc.RC + self.link
								self.totalKeywordFound += 0
						
							self.branches.append(self.link)
							self.duplicates.append(self.link)
							self.branchDB.db.execute("INSERT OR IGNORE INTO branches(FLD, BASE_URL, BRANCH_URL, BRANCH_SET_KEY, KEYWORD, KEYWORD_FOUND, BRANCH_DATE) VALUES ('" + str(self.fld) + "', '" + self.base_url + "', '" + self.link + "', '" + self.branchSetKey + "','" + self.keyword.replace(' ', '').title() + "', '" + self.keywordFound.title() + "', '" + self.datetime + "')")
							self.branchDB.db.commit()
							print(self.branchStatus)
							print(bc.BC + ' Searching for other data types...')
							dataCheck = scanContent(self.link, self.branchSetKey)
							dataCheck.searchData()
						else:
							continue
					else:
						continue
				else:
					continue
			except KeyboardInterrupt:
				pass
				
		os.system('clear')
		print(banner)
		print(bc.BC + ' Base URL: ' + bc.GC + self.base_url)
		print(bc.BC + ' Branch Set Key: ' + bc.GC + self.branchSetKey)
		print(bc.BC + ' Links Checked: ' + bc.GC + str(self.totalBranchCount) + '\n')

		print(bc.BC + ' "' + bc.GC + self.keyword.replace(' ', '') + bc.BC + '" found in pages:')
		self.branchOutput = self.branchDB.db.execute("SELECT * FROM branches WHERE BASE_URL='"+self.base_url+"' AND KEYWORD_FOUND='True' AND BRANCH_SET_KEY='"+self.branchSetKey+"'")
		for self.row in self.branchOutput:
			print('\t' + sBan + ' ' + bc.GC + self.row[3])
		if(self.totalKeywordFound == 0):
			print('\t' + eBan + bc.RC + ' None\n')		
		elif(self.totalKeywordFound == 1):
			print(bc.BC + '\n Keyword Found: ' + bc.GC + str(self.totalKeywordFound) + ' Time\n')
		else:
			print(bc.BC + '\n Keyword Found: ' + bc.GC + str(self.totalKeywordFound) + ' Times\n')

		self.dbOutput = self.branchDB.db.execute("SELECT * FROM branch_data WHERE BRANCH_SET_KEY='"+self.branchSetKey+"' AND CONTENT_ID='"+self.branchSetKey+"'")
		self.outputDuplicates = []
		print(bc.BC + ' Other Data Found:')
		for self.out in self.dbOutput:
			if(self.out[5] not in self.outputDuplicates):
				if(self.out[2] == 'DOMAIN'):
					print('\t' + sBan + ' Domain: ' + bc.GC + self.out[5])
				
				if(self.out[2] == 'EMAIL'):
					print('\t' + sBan + ' Email: ' + bc.GC + self.out[5])
				elif(self.out[2] == 'USERNAME_HANDLE'):
					print('\t' + sBan + ' Username/Handle: ' + bc.GC + self.out[5])
				elif(self.out[2] == 'PHONE_NUMBER'):
					print('\t' + sBan + ' Phone Number: ' + bc.GC + self.out[5])
				elif(self.out[2] == 'BITCOIN_ADDRESS'):
					print('\t' + sBan + ' Bitcoin Address: ' + bc.GC + self.out[5])
				else:
					continue
				self.outputDuplicates.append(self.out[5])
			else:
				continue
