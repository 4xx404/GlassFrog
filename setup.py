#!/usr/bin/python3

import os, sys, time

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

def runSetup():
	print(bc.BC + ' Running GlassFrog setup...\n Installing Dependencies...\n')
	try:
		os.system('python3 -m pip install -r modules/requirements.txt')
	except Exception:
		print(eBan + bc.RC + ' Failed to install dependencies\n')
		quit()
	
	os.system('clear')
	print(banner)
	print(sBan + ' Dependencies Installed')
	try:
		os.system('mv GlassFrog-UI /var/www/html/')
	except Exception:
		print(eBan + ' Failed to move ' + bc.RC + 'GlassFrog-UI/' + bc.BC + ' to ' + bc.RC + '/var/www/html/')
		print(eBan + ' Setup failed')
		quit()

	print(sBan + ' Moved ' + bc.GC + 'GlassFrog-UI/' + bc.BC + ' to ' + bc.GC + '/var/www/html/')
	print(sBan + ' Setup successful')
	quit()

if __name__ == '__main__':
	runSetup()
