#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time
from datetime import datetime
import sqlite3
from sqlite3 import Error

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

class database:
	def __init__(self):
		self.db = sqlite3.connect('/var/www/html/GlassFrog-UI/db/glassFrog.db')

	def createTables(self):
		try:
			try:
				self.db.execute('''CREATE TABLE branches(
					ID		INTEGER		PRIMARY KEY	AUTOINCREMENT	NOT NULL,
					FLD		TEXT						NOT NULL,
					BASE_URL	TEXT						NOT NULL,
					BRANCH_URL	TEXT						NOT NULL,
					BRANCH_SET_KEY	TEXT						NOT NULL,
					KEYWORD		TEXT						NOT NULL,
					KEYWORD_FOUND	TEXT						NOT NULL,			
					BRANCH_DATE	DATETIME);
				''')

				self.dbStatus = sBan + " Created Database Table: " + bc.GC + 'branches'
				print(self.dbStatus)
				time.sleep(1)
			except sqlite3.OperationalError:
				self.dbStatus = sBan + " Loaded Database Table: " + bc.GC + 'branches'
				print(self.dbStatus)
				time.sleep(1)
				pass
			try:
				self.db.execute('''CREATE TABLE branch_data(
					ID		INTEGER		PRIMARY KEY	AUTOINCREMENT	NOT NULL,
					CONTENT_ID	TEXT						NOT NULL,
					DATATYPE	TEXT						NOT NULL,
					BRANCH_URL	TEXT						NOT NULL,
					BRANCH_SET_KEY	TEXT						NOT NULL,
					DATA		TEXT						NOT NULL,
					DATA_DATE	DATETIME);
				''')

				self.dbStatus = sBan + " Created Database Table: " + bc.GC + 'branch_data'
				print(self.dbStatus)
				time.sleep(1)
			except sqlite3.OperationalError:
				self.dbStatus = sBan + " Loaded Database Table: " + bc.GC + 'branch_data'
				print(self.dbStatus)
				time.sleep(1)
				pass
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			quit()
