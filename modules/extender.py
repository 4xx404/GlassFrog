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
links = []
keyWordsFound = []

os.system('clear')
print(banner)

def extender(base_url, keyWord):
	x = open("links/externalLinks.txt", 'r+')
	bURLTotal = 0
	for line in x:
		line = str(line).replace('\n', '')
		links.append(line)
		bURLTotal += 1
	x.close()
	
	bURLCount = 0
	for bURL in links:
		bURLCount += 1
		os.system('clear')
		print(banner)
		print(bc.BC + ' Search Type: ' + bc.GC + 'Single Keyword' + bc.BC + '[' + bc.GC + 'Extended' + bc.BC + ']')
		print(bc.BC + ' Base URL: ' + bc.GC + base_url)
		print(bc.BC + ' Keyword: ' + bc.GC + keyWord.replace(' ', '') + '\n')
		print(iBan + ' This may take a while, be patient...\n')
		try:
			pageres = requests.get(bURL, headers=headers)
			soup = BeautifulSoup(pageres.content, 'html.parser')
			checkedLinks = 0
			print(bc.BC + " Progress: " + bc.GC + str(bURLCount) + bc.BC + "/" + bc.GC + str(bURLTotal) + bc.BC + " Base URL's")
			print(bc.BC + ' Using Base URL: ' + bc.GC + bURL + '\n')

			duplicates = []
			hrefs = []
			checkedLinks = 0

			x = open('links/externalLinks-EXTENDED.txt', 'w+')
			for l in soup.find_all("a", href=True):
				link = l['href'].replace('\n','')
				if(link.startswith('http://')):
					link = link
				elif(link.startswith('https://')):
					link = link
				elif(link.startswith('/')):
					if(bURL.endswith('/')):
						link = bURL[:-1] + link
					else:
						link = bURL + link
				elif(link.startswith('#')):
					#link = ''
					continue
				else:
					link = bURL + link

				if(link != ''):
					if(link != bURL):
						if(link not in duplicates):
							if(link not in links):
								hrefs.append(link)
								duplicates.append(link)
								x.write(link + '\n')
								checkedLinks += 1
							else:
								continue
						else:
							continue
					else:
						continue
				else:
					continue

				keyWordsCount = 0
				for h in hrefs:
					if(h != base_url or h != base_url[:-1]):
						r = requests.get(h)
						try:
							if(r.status_code == 200):
								if(keyWord in r.text):						
									print(sBan + ' ' + bc.GC + h)
									keyWordsFound.append(h)
									keyWordsCount += 1
								else:
									print(eBan + ' ' + bc.RC + h)
							hrefs.pop(0)
						except KeyboardInterrupt:
							continue

		#			except Exception:
		#				continue
		#				try:
#							input(bc.BC + ' Press Enter to Continue...')
#						except KeyboardInterrupt:
#							print()
#							quit()
#						from glassFrog import glassFrog
#						glassFrog()


			try:
				x = open('collected-data/search-output-EXTENDED.txt', 'w+')
				kFound = 0
				for f in keyWordsFound:
					print('\t' + sBan + ' ' + bc.GC + f)
					x.write(f + '\n')
					kFound += 1
				x.close()
					#input(bc.BC + '\n Press Enter to Continue...')
			except KeyboardInterrupt:
				print(bc.BC + '\n\n Returning to GlassFrog...\n')
				time.sleep(1)
				from glassFrog import glassFrog
				glassFrog()

		except Exception:
			continue
		except KeyboardInterrupt:
			try:
				continue
			except KeyboardInterrupt:
				os.system('clear')
				print(banner)
				print(bc.BC + ' Returning to GlassFrog...')
				time.sleep(1)
				from glassFrog import glassFrog
				glassFrog()
				x.close()
	time.sleep(1)
	os.system('clear')
	print(banner)
	print(sBan + ' Search Type: ' + bc.GC + 'Single Keyword' + bc.BC + '[' + bc.GC + 'Extended' + bc.BC + ']')	
	print(sBan + ' Base URL: ' + bc.GC + base_url)
	print(sBan + ' Keyword: ' + bc.GC + keyWord.replace(' ', ''))
	print(sBan + ' Total Keyword Found: ' + bc.GC + str(kFound))
	print(sBan + ' Links Checked: ' + bc.GC + str(checkedLinks))
	print(bc.BC + '\n "' + bc.GC + keyWord.replace(' ', '').title() + bc.BC + '" Found on Pages: ')
	x = open('collected-data/search-output-EXTENDED.txt', 'r+')
	for f in x:
		f = str(f).replace('\n', '')
		print('\t' + sBan + ' ' + bc.GC + f)
	x.close()	
	try:
		input(bc.BC + '\n\n Press Enter to Continue...\n')
	except KeyboardInterrupt:
		print(bc.BC + '\n Closing GlassFrog...')
		time.sleep(1)
		quit()
	from glassFrog import glassFrog
	glassFrog()

if __name__ == '__main__':
	extender()
