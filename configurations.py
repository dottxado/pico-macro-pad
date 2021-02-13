import usb_hid
import time

from abstract_classes import AbstractConfiguration, AbstractMacro
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

class Terminal(AbstractConfiguration):
	def getName():
		return 'Terminal'
	def getColor():
		return (0, 255, 0)
	def getMacros():
		return [
			Ls, 
			Pwd,
			Home
		]

class GoogleMeet(AbstractConfiguration):
	def getName():
		return 'Google Meet'
	def getColor():
		return (255, 128, 0)
	def getMacros():
		return [
			ToggleMicrophone, 
			ToggleWebcam
		]

class OBS(AbstractConfiguration):
	def getName():
		return 'OBS'
	def getColor():
		return (0, 0, 255)
	def getMacros():
		return [
			SelectScene1, 
			SelectScene2,
			SelectScene3,
			MuteOn,
			MuteOff
		]

class Obsidian(AbstractConfiguration):
	def getName():
		return 'Obsidian'
	def getColor():
		return (51, 51, 255)
	def getMacros():
		return [
			AddNewLog
		]

class Ls(AbstractMacro):
	def getMacroName():
		return 'ls -al'
	def getMacro():
		layout.write("ls ")
		keyboard.send(Keycode.KEYPAD_MINUS)
		layout.write("al")
		keyboard.send(Keycode.ENTER)

class Pwd(AbstractMacro):
	def getMacroName():
		return 'pwd'
	def getMacro():
		layout.write("pwd")
		keyboard.send(Keycode.ENTER)

class Home(AbstractMacro):
	def getMacroName():
		return 'Home'
	def getMacro():
		layout.write("cd ")
		keyboard.send(Keycode.ENTER)

class ToggleMicrophone(AbstractMacro):
	def getMacroName():
		return 'Toggle Microphone'
	def getMacro():
		keyboard.send(Keycode.COMMAND, Keycode.D)

class ToggleWebcam(AbstractMacro):
	def getMacroName():
		return 'Toggle Webcam'
	def getMacro():
		keyboard.send(Keycode.COMMAND, Keycode.E)

class SelectScene1(AbstractMacro):
	def getMacroName():
		return 'Scene 1'
	def getMacro():
		keyboard.send(Keycode.LEFT_ALT, Keycode.ONE)

class SelectScene2(AbstractMacro):
	def getMacroName():
		return 'Scene 2'
	def getMacro():
		keyboard.send(Keycode.LEFT_ALT, Keycode.TWO)

class SelectScene3(AbstractMacro):
	def getMacroName():
		return 'Scene 3'
	def getMacro():
		keyboard.send(Keycode.LEFT_ALT, Keycode.THREE)

class MuteOn(AbstractMacro):
	def getMacroName():
		return 'Mute'
	def getMacro():
		keyboard.send(Keycode.LEFT_ALT, Keycode.FOUR)

class MuteOff(AbstractMacro):
	def getMacroName():
		return 'Unmute'
	def getMacro():
		keyboard.send(Keycode.LEFT_ALT, Keycode.FIVE)

class AddNewLog(AbstractMacro):
	def getMacroName():
		return 'New Log'
	def getMacro():
		keyboard.send(Keycode.COMMAND, Keycode.P)
		layout.write("Insert template")
		time.sleep(0.1)
		keyboard.send(Keycode.ENTER)
		layout.write("New log")
		time.sleep(0.1)
		keyboard.send(Keycode.ENTER)

configurations_map = [Terminal, GoogleMeet, OBS, Obsidian]	
