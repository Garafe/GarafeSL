# CREDITS ➤ SL Hydra

import os
import sys
import time

def mprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

logo = """\033[1;33m
	[01] Termux Packages Install For Beginners
	[02] Tool Store
	[03] Our Notes
	[04] Report Errors

	\033[0;33m[05] Our Youtube Channel
	[06] Our Whatsappp Groups
	[07] Our Github Page
	[08] Our Whatsapp Bot
	[09] Tool Owners
		[10] Update Tool
		[00] Exit\n"""

mprint (logo)
