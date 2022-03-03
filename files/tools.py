# CREDITS ➤ SL Hydra

import sys
import os
import time

def tprint(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.01)

os.system ("clear")

logo = """\033[0;49;34m
    d888b   .d8b.  d8888b.  .d8b.  d88888b d88888b
   88  Y8b d8   8b 88   8D d8   8b 88      88
   88      88ooo88 88oobY  88ooo88 88ooo   88ooooo
   88  ooo 88   88 88 8b   88   88 88      88
   88   8  88   88 88  88  88   88 88      88
    Y888Y  88   88 88   88 88   88 88      8888888"""

logo1 = """\033[0;49;34m
 ╔════╗╔═══╗╔═══╗╔╗───────╔═══╗╔════╗╔═══╗╔═══╗╔═══╗
 ║╔╗╔╗║║╔═╗║║╔═╗║║║───────║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║║╔══╝
 ╚╝║║╚╝║║─║║║║─║║║║───────║╚══╗╚╝║║╚╝║║─║║║╚═╝║║╚══╗
   ║║──║║─║║║║─║║║║─╔╗────╚══╗║──║║──║║─║║║╔╗╔╝║╔══╝
   ║║──║╚═╝║║╚═╝║║╚═╝║────║╚═╝║──║║──║╚═╝║║║║╚╗║╚══╗
   ╚╝──╚═══╝╚═══╝╚═══╝────╚═══╝──╚╝──╚═══╝╚╝╚═╝╚═══╝\n"""

logo2 = """\033[1;35m
      [~] Author-SL HYDRA(Garafe Official ADMIN)
      [~] Do not Copy This Tool

¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡\n"""

print (logo)
time.sleep (1.0)
print (logo1)
time.sleep (1.0)
print (logo2)
print ()
time.sleep (1.0)

logo3 = """\033[1;33m
	[01] Termux Banner	[02] T-Buttons
	[03]

		\033[0;33m[10] Back
		[00] Exit\n"""

tprint (logo3)

logo4 = """\033[1;32m
     ➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸
     ➸+------------------------------+➸
     \033[1;32m➸|      \033[1;33m[01] Run This Tool\033[0;0m      \033[1;32m|➸
     \033[1;32m➸|      \033[1;33m[02] Back\033[0;0m               \033[1;32m|➸
     \033[1;32m➸|      \033[1;33m[00] Exit\033[0;0m               \033[1;32m|➸
     \033[1;32m➸+------------------------------+➸
     \033[1;32m➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸\n"""

print ()
cho = int(input("\033[0;31;47m [+] Enter Your Choice >>> \033[0;0m"))
print ()
if cho == 1:
	print (" \033[1;32m[+] Loading....")
	time.sleep (1.0)
	print ()
	print (" \033[1;32m[+] Installing....")
	time.sleep (2.0)
	print ()
	os.system ("figlet Successfully | lolcat")
	os.system ("figlet Installed | lolcat")
	os.system ("clear")
	tprint (logo4)
