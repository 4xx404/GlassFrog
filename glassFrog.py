#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time
import requests
import sqlite3
from bs4 import BeautifulSoup
from modules.connectDB import database
from modules.collectBranches import collector

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

os.system('clear')
print(banner)

db = database()
db.createTables()

print('\n' + iBan + ' Include ' + bc.GC + 'http://' + bc.BC + ' or ' + bc.GC + 'https://' + bc.BC + ' in URL')
print('\t' + eBan + bc.RC + ' example.com')
print('\t' + eBan + bc.RC + ' www.example.com')
print('\t' + sBan + bc.GC + ' https://example.com')
print('\t' + sBan + bc.GC + ' https://www.example.com\n')

def glassFrog():
	base_url = ''
	keyword = ''
	try:
		base_url = str(input(bc.BC + ' Base URL: ' + bc.GC))
		keyword = str(input(bc.BC + ' Keyword: ' + bc.GC))
		if(base_url == ''):
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Base URL value cannot be empty\n')
			time.sleep(1)
			glassFrog()
		elif(keyword == ''):
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Keyword value cannot be empty\n')
			time.sleep(1)
			glassFrog()
		else:
			keyword = ' ' + str(keyword) + ' '
			if(base_url.endswith('/')):
				base_url = base_url
			else:
				base_url = base_url + '/'

			if(base_url.startswith('https://') or base_url.startswith('https://')):
				setBranches = ['' , '', '']
				branch = collector()
				branch.addBranches(base_url, keyword)
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Base URL must start with ' + bc.RC + 'http://' + bc.BC + ' or ' + bc.RC + 'https://' + '\n')
				time.sleep(1)
				glassFrog()

			try:
				os.system('sort data-analysis/UNKNOWN-TYPE-DATA.txt | uniq -d >> data-analysis/UNKNOWN-TYPE-DATA.txt')
			except Exception:
				print('\n' + eBan + ' Failed to remove duplicates from: ' + bc.RC + 'data-analysis/UNKNOWN-TYPE-DATA.txt\n')
				input(bc.BC + ' Press Enter to Continue...')

			print('\n' + sBan + ' Removed duplicates from ' + bc.GC + 'data-analysis/UNKNOWN-TYPE-DATA.txt\n')

			time.sleep(1)
			extendStr = bc.BC + ' Extend to Branches[' + bc.GC + 'y' + bc.BC + '/' + bc.GC + 'n' + bc.BC +']: '
			extend = str(input(extendStr + bc.GC))
			if(extend == 'y'):
				os.system('clear')
				print(banner)
				print(eBan + ' [' +bc.GC + ' * * * ' + bc.BC + '] EXTENDER COMING SOON! [' + bc.GC + ' * * * ' + bc.BC + ']')
				time.sleep(1)
				glassFrog()
			else:
				os.system('clear')
				print(banner)
				print(bc.BC + ' Returning to Glass Frog...\n')
				time.sleep(1)
				glassFrog()

	except KeyboardInterrupt:
		os.system('clear')
		print(banner)
		quit()
			
if __name__ == '__main__':
	glassFrog()
