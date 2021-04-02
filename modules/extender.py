#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time, datetime
import socket
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

def extender(base_url, keyWord):
	print(bc.BC + ' Base URL: ' + bc.GC + base_url)
	print(bc.BC + ' Searching for Keyword: ' + bc.GC + keyWord + '\n')
	print(iBan + ' This may take a moment to start...')

	links = []

	x = open("modules/data/externalLinks.txt", 'r+')
	for li in x:
		li = str(li).replace('\n', '')
		links.append(li)
	x.close()

	for bURL in links:
		try:
			pageres = requests.get(bURL, headers=headers)
			soup = BeautifulSoup(pageres.content, 'html.parser')
		except Exception:
			continue
			
		duplicates = []
		hrefs = []
		checkedLinks = 0

		for l in soup.find_all("a", href=True):
			link = l['href'].replace('\n','')
			if(link.startswith('http://')):
				link = link
			elif(link.startswith('https://')):
				link = link
			else:
				if(link.startswith('/')):
					if(bURL.endswith('/')):
						link = bURL[:-1] + link
					else:
						link = bURL + link
				elif(link.startswith('#')):
					continue
				else:
					link = bURL + link

				if(link != bURL):
					if(link not in duplicates):
						hrefs.append(link)
						#x.write(link + '\n')
						duplicates.append(link)
						checkedLinks += 1
					else:
						continue
				else:
					continue

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
						print(bc.BC + '\n Searching "' + bc.GC + keyWord + bc.BC + '" on ' + h)
						time.sleep(1)
						print(sBan + ' ' + bc.GC + h)
						keyWordsFound.append(h)
						keyWordsCount += 1
					else:
						print(bc.BC + '\n Searching "' + bc.GC + keyWord + bc.BC + '" on ' + h)
						time.sleep(1)
						print(eBan + ' ' + bc.RC + h)
						continue
				else:
					continue

				hrefs.pop(0)
		except KeyboardInterrupt:
			print('\n\n' + sBan + ' Search Stopped\n')
			time.sleep(1)
			try:
				input(bc.BC + ' Press Enter to Continue...')
			except KeyboardInterrupt:
				print()
				quit()
			from glassFrog import glassFrog
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
			
	input(bc.BC + '\n Press Enter to Continue...')
	from glassFrog import glassFrog
	glassFrog()

if __name__ == '__main__':
	extender()
