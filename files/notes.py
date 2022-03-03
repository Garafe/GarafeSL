# CREDITS âž¤ SL Hydra

import sys
import os
import time

logo = """\033[1;32m
 ######     ###   ########    ###   ####### ########
##    ##   ## ##  ##     ##  ## ##  ##      ##
##        ##   ## ##     ## ##   ## ##      ##
##   ######     ########## ##     ######### ######
##    ## ###########   ##  ###########      ##
##    ## ##     ####    ## ##     ####      ##
 ######  ##     ####     ####     ####      ########

     d8b   db  .d88b.  d888888b d88888b .d8888.
     888o  88 .8P  Y8. `~~88~~' 88'     88'  YP
     88V8o 88 88    88    88    88ooooo `8bo.
     88 V8o88 88    88    88    88        `Y8b.
     88  V888 `8b  d8'    88    88.     db   8D
     VP   V8P  `Y88P'     YP    Y88888P `8888Y'"""

logo1 = """
		\033[1;35mChoose Your Note 👇

		\033[1;34m[01] HTML LESSONS
		[02] PROGRAMMING LESEONS
		[03] HACKING LESSONS
		[03] All LESSONS

		\033[0;33m[10] Back
		[00] Exit\n"""

os.system ("clear")
print (logo)
time.sleep (1.0)
print (logo1)
time.sleep (1.0)
print ()

cho=int(input("\033[1;32m [âž¸] Enter Your Choice >>> "))
print ()
if cho == 1:
	print ("\033[1;32m [+] Loading....")
	time.sleep (1.0)
	print ()
	print ("\033[1;32m [+] Downloading.... Please Wait!")
	os.system ("cd files;cd notes;python html.py")
	print ("\033[1;33m [+] Our HTML PDF Set was Successfuly Downloaded")
	time.sleep (2.0)
	os.system ("python notes.py")

elif cho == 2:
	print ("\033[1;32m [+] Loading....")
	time.sleep (1.0)
	print ()
	print ("\033[1;32m [+] Downloading.... Please Wait!")
	os.system ("cd files;cd notes;python programming.py")
	print ("\033[1;33m [+] Our PROGRAMMING PDF Set was Successfuly Downloaded")
	time.sleep (2.0)
	os.system ("python notes.py")

elif cho == 3:
	print ("\033[1;32m [+] Loading....")
	time.sleep (1.0)
	print ()
	print ("\033[1;32m [+] Downloading.... Please Wait!")
	os.system ("cd files;cd notes;python hacking.py")
	print ("\033[1;33m [+] Our HACKING PDF Set was Successfuly Downloaded")
	time.sleep (2.0)
	os.system ("python notes.py")

elif cho == 4:
	print ("\033[1;32m [+] Loading....")
	time.sleep (1.0)
	print ()
	print ("\033[1;32m [+] Downloading.... Please Wait!")
	os.system ("cd files;cd notes;python all.py")
	print ("\033[1;33m [+] Successfuly Downloaded")
	time.sleep (2.0)
	os.system ("python notes.py")

elif cho == 10:
	print ("\033[1;32m [+] Loading....")
	time.sleep (1.0)
	os.system ("python garafe.py")

elif cho == 0:
	print ("\033[1;31m [+] Exiting....")
	time.sleep (1.0)
	print ()
	print ("\033[1;31m [+] Bye Bye....")
	time.sleep (1.0)
	print ()
	sys.exit()

else :
	print ("\033[1;31m [+] Your Choice Is Wrong!")
	time.sleep (1.0)
	os.system ("python notes.py")
