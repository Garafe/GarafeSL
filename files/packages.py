#Tool Created By SL Hydra😈

import os
import sys
import time

# Set color
R = '\033[1;31m' #Red
W = '\033[1;37m' #White
G = '\033[1;32m' #Green
O = '\033[0;33m' #Orange
B = '\033[1;34m' #Blue
Y = '\033[1;33m' #Yello
P = '\033[1;35m' #Purple

def tprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

os.system ("clear")

logo = """\033[0;33m
		  ╔═══╗╔╗   ╔╗
		  ║╔═╗║║║   ║║
		  ║║ ║║║║   ║║
		  ║╚═╝║║║ ╔╗║║ ╔╗
		  ║╔═╗║║╚═╝║║╚═╝║
		  ╚╝ ╚╝╚═══╝╚═══╝
      ╔═══╗╔═══╗╔═══╗╔╗╔═╗╔═══╗╔═══╗╔═══╗╔═══╗
      ║╔═╗║║╔═╗║║╔═╗║║║║╔╝║╔═╗║║╔═╗║║╔══╝║╔═╗║
      ║╚═╝║║║─║║║║─╚╝║╚╝╝─║║─║║║║─╚╝║╚══╗║╚══╗
      ║╔══╝║╚═╝║║║─╔╗║╔╗║─║╚═╝║║║╔═╗║╔══╝╚══╗║
      ║║───║╔═╗║║╚═╝║║║║╚╗║╔═╗║║╚╩═║║╚══╗║╚═╝║
      ╚╝───╚╝─╚╝╚═══╝╚╝╚═╝╚╝─╚╝╚═══╝╚═══╝╚═══╝"""

print (logo)
time.sleep (1.0)

logo2 = """\033[1;33m
		[01] Install All Basic Packages
		[10] Back
		[00] Exit\n"""
tprint (logo2)

print ()
cho=int(input("\033[1;32m [+] Enter Your Choice : "))
print ()
if cho == 1:
	os.system ("clear")
	os.system ("figlet Please Wait . . . | lolcat")
	print ()
	time.sleep (1.0)
	os.system ("pkg install python -y && pkg update -y &&  pkg upgrade -y && pkg install python2 -y &&  pkg install fish -y && pkg install ruby -y && pkg install git -y &&  pkg install php -y &&  pkg install perl -y && pkg install nmap -y && pkg install bash -y && pkg install clang -y  && pkg install nano -y && pkg install w3m -y && pkg install hydra -y && pkg install figlet -y && pkg install cowsay -y && pkg install curl -y&& pkg install tar -y && pkg install zip -y && pkg install unzip -y && pkg install tor -y && pkg install wget -y && pkg install wcalc -y && pkg install bmon -y && pkg install golang -y && pkg install openssl -y && pkg install cmatrix -y && pkg install openssh -y && pkg install wireshark -y && pkg install toilet && pkg install sl && pkg install vim && pkg install tch && pkg install zsh && pkg install fortune && pkg install zsh && apt update && apt upgrade -y")
	print ()
	time.sleep (2.0)
	os.system ("figlet Done | lolcat")
	os.system ("cd;cd garafeSL;python garafe.py")

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
	sys.exit ()

else :
	print (""+R+" [+] Your Choice Is Wrong")
	time.sleep (1.0)
	os.system ("python packages.py")
