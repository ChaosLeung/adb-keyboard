#!/usr/bin/python
import termios, fcntl, sys, os

def sendAdbCmd(cmd):
	os.system(cmd);

def sendKeyEvent(keyCode):
	sendAdbCmd("adb shell input keyevent %d" % (keyCode))

def sendText(text):
	sendAdbCmd("adb shell input text %s" % (text))

def getKeyCodeByASCII(asciiCode):
	if asciiCode == 1:# Left
		code = 21
	elif asciiCode == 23:# UP
		code = 19
	elif asciiCode == 4:# RIGHT
		code = 22
	elif asciiCode == 24:# DOWN
		code = 20
	elif asciiCode == 2:# ESCAPE
		code = 111
	elif asciiCode == 10:# ENTER
		code = 66
	elif asciiCode == 127:# BACKSPACE
		code = 67
	elif asciiCode == 8:# HOME
		code = 3
	elif asciiCode in range(97, 123):# a-z
		code = asciiCode - 68
	elif asciiCode in range(65, 91):# A-Z
		code = asciiCode - 36
	elif asciiCode in range(48, 58):# 0-9
		code = asciiCode + 96
	else:
		code = -1
	return code


fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

editMode = bool(0)

try:
	while 1:
		try:
			c = sys.stdin.read(1)
			asciiCode = ord(c)
			if asciiCode == 5: # Edit Mode
				editMode = not editMode
			elif editMode:
				sendText(c)
			else:
				sendKeyEvent(getKeyCodeByASCII(asciiCode))

		except IOError: pass
finally:
	termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
	fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)