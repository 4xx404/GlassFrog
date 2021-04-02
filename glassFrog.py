#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time, datetime
import requests
from bs4 import BeautifulSoup

class bc:
	GC = '\033[1;39m'
	BC = '\033[1;34m'
	RC = '\033[1;31m'

author = bc.BC + "\n Author: " + bc.RC + "4" + bc.GC + "x" + bc.BC + "x" + bc.RC + "4" + bc.GC + "0" + bc.BC + "4\n"
version = bc.BC + " Version: " + bc.RC + "1" + bc.GC + "." + bc.BC + "0\n"
github = bc.BC + " Github: " + bc.RC + "h" + bc.GC + "t" + bc.BC + "t" + bc.RC + "p" + bc.GC + "s" + bc.BC + ":" + bc.RC + "/" + bc.GC + "/" + bc.BC + "g" + bc.RC + "i" + bc.GC + "t" + bc.BC + "h" + bc.RC + "u" + bc.GC + "b" + bc.BC + "." + bc.RC + "c" + bc.GC + "o" + bc.BC + "m" + bc.RC + "/" + bc.GC + "4" + bc.BC + "x" + bc.RC + "x" + bc.GC + "4" + bc.BC + "0" + bc.RC + "4\n"

banner = bc.RC + '''
''' + bc.GC + '''   ___  __      __    ___  ___  ____  ____  _____  ___     _   _   
''' + bc.BC + '''  / __)(  )    /__\  / __)/ __)( ___)(  _ \(  _  )/ __)   (.)_(.)  
''' + bc.RC + ''' ( (_-. )(__  /(__)\ \__ \\\__ \ )__)  )   / )(_)(( (_-.  (   _   ) 
''' + bc.GC + '''  \___/(____)(__)(__)(___/(___/(__)  (_)\_)(_____)\___/  /`-----'\ 
''' + author + version + github

iBan = bc.BC + " [" + bc.GC + "?" + bc.BC + "]"
sBan = bc.BC + " [" + bc.GC + u'\u2713' + bc.BC + "]"
eBan = bc.BC + " [" + bc.RC + u'\u2717' + bc.BC + "]"

headers = {'Accept-Language': 'en-US,en;q=0.5', 'Cache-Control': 'no-cache', 'User-Agent': 'GlassFrog.V1'}

os.system('clear')
print(banner)
print(iBan + ' Include ' + bc.GC + 'http://' + bc.BC + ' or ' + bc.GC + 'https://' + bc.BC + ' in URL')
print('\t' + eBan + bc.RC + ' example.com')
print('\t' + eBan + bc.RC + ' www.example.com')
print('\t' + sBan + bc.GC + ' https://example.com')
print('\t' + sBan + bc.GC + ' https://www.example.com\n')

urls = []

def glassFrog():
	try:
		base_url = str(input(bc.BC + ' Enter Base URL: ' + bc.GC))
		keyWord = str(input(bc.BC + ' Enter Keyword: ' + bc.GC))
	except KeyboardInterrupt:
		os.system('clear')
		print(banner)
		print(bc.BC + ' Closing glassFrog...')
		time.sleep(1)
		os.system('clear')
		print(banner)
		quit()

	if(base_url == ''):
		os.system('clear')
		print(banner)
		print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Base URL value cannot be empty\n')
		time.sleep(1)
		glassFrog()
		
	if(base_url.endswith('/')):
		base_url = base_url
	else:
		base_url = base_url + "/"

	if(keyWord == ''):
		os.system('clear')
		print(banner)
		print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Keyword value cannot be empty\n')
		time.sleep(1)
		glassFrog()
		
	os.system('clear')
	print(banner)

	try:
		pageres = requests.get(base_url, headers=headers)
		soup = BeautifulSoup(pageres.content, 'html.parser')
		print(bc.BC + ' Base URL: ' + bc.GC + base_url)
		print(bc.BC + ' Searching for Keyword: ' + bc.GC + keyWord + '\n')
		time.sleep(1)
	except Exception:
		os.system('clear')
		print(banner)
		print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Failed to connect to: ' + bc.RC + base_url + '\n')
		time.sleep(1)
		glassFrog()

	duplicates = []
	hrefs = []

	x = open('modules/data/externalLinks.txt', 'w+')
	checkedLinks = 0
	for l in soup.find_all("a", href=True):
		link = l['href'].replace('\n','')
		if(link.startswith('http://')):
			link = link
		elif(link.startswith('https://')):
			link = link
		else:
			if(link.startswith('/')):
				link = base_url[:-1] + link
			elif(link.startswith('#')):
				#link = base_url[:-1] + link
				continue
			else:
				link = base_url + link

		if(link != base_url):
			if(link not in duplicates):
				hrefs.append(link)
				x.write(link + '\n')
				duplicates.append(link)
				checkedLinks += 1
			else:
				continue

	x.close()

	keyWordsFound = []
	keyWordsCount = 0
	try:
		for h in hrefs:
			try:
				r = requests.get(h)
			except Exception:
				continue

			if(r.status_code == 200):
				if(keyWord in r.text):
					print(sBan + ' ' + bc.GC + h)
					keyWordsFound.append(h)
					keyWordsCount += 1
				else:
					print(eBan + ' ' + bc.RC + h)
			else:
				pass

	except KeyboardInterrupt:
		print('\n\n' + sBan + ' Search Stopped\n')
		time.sleep(1)
		glassFrog()

	time.sleep(1)
	os.system('clear')
	print(banner)
	print(sBan + ' Base URL: ' + bc.GC + base_url)
	print(sBan + ' Keyword: ' + bc.GC + keyWord)
	print(sBan + ' Keyword Found: ' + bc.GC + str(keyWordsCount))
	print(sBan + ' Links Checked: ' + bc.GC + str(checkedLinks))

	print(bc.BC + '\n "' + bc.GC + keyWord.title() + bc.BC + '" Found on Pages: ')
	for f in keyWordsFound:
		print('\t' + sBan + ' ' + bc.GC + f)
	
	extendBanner = bc.BC + '\n Extend to External Links[' + bc.GC + 'y' + bc.BC + '/' + bc.GC + 'n' + bc.BC + ']: '
	extend = str(input(extendBanner + bc.GC)).lower()
	if(extend == 'y'):
		from modules.extender import extender
		os.system('clear')
		print(banner)
		extender(base_url, keyWord)
	elif(extend == 'n'):
		print()
		glassFrog()
	else:
		print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option, not extending...\n')
		glassFrog()

if __name__ == '__main__':
	glassFrog()
