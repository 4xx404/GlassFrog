import os, sys, time
from pyngrok import ngrok
import subprocess

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

def runServer():
	print(bc.BC + " Starting Ngrok HTTP Tunnel...")
	try:
		http_tunnel = ngrok.connect()
		time.sleep(1)
		if http_tunnel:
			serverStatus = sBan + ' Ngrok Tunnel: ' + bc.GC + 'Connected'
		else:
			serverStatus = eBan + ' Ngrok Tunnel: ' + bc.RC + 'Disconnected'
		
		os.system('clear')
		print(banner)
		print(serverStatus)
		glassFrogURL = str(http_tunnel).replace('"', '').replace('NgrokTunnel: ', '').replace(' -> http://localhost:80', '').replace('http', 'https') + "/GlassFrog-UI/glassFrog.php"
		time.sleep(0.5)
		print(bc.BC + ' Interface URL: ' + bc.GC + glassFrogURL)
		ngrok_process = ngrok.get_ngrok_process()
		print(bc.BC + "\n" + iBan + bc.GC + " CTRL + C" + bc.BC + " to stop the server\n")
		os.chdir('/var/www/html/')
		subprocess.call(['php', '-S', 'localhost:80'])
		ngrok_process.proc.wait()
	except KeyboardInterrupt:
		os.system('clear')
		print(banner)
		print(bc.BC + " Closing PHP Web Server...")
		time.sleep(0.5)
		print(bc.BC + " Closing Ngrok HTTP Tunnel...")
		ngrok.disconnect(http_tunnel.public_url)
		time.sleep(0.5)
		print(bc.BC + " Killing Ngrok process...")
		time.sleep(0.5)
		ngrok.kill()
		time.sleep(0.5)
		os.system('clear')
		print(banner)
		quit()

if __name__ == '__main__':
	runServer()
