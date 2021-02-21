import usb_hid
import time
import random

from abstract_classes import AbstractConfiguration, AbstractMacro
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

## CONFIGURATIONS ##

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

class Git(AbstractConfiguration):
	def getName():
		return 'GIT'
	def getColor():
		return (247, 78, 39)
	def getMacros():
		return [
			MergeDevelop,
			MergeMaster,
			GitPush
		]

class RandomEstimation(AbstractConfiguration):
	def getName():
		return 'Random Esteem'
	def getColor():
		return (255, 0, 0)
	def getMacros():
		return [
			OneWeekEsteem, 
			OneMonthEsteem,
			SixMonthsEsteem
		]

class PhpStorm(AbstractConfiguration):
	def getName():
		return 'PHPStorm'
	def getColor():
		return (232, 49, 123)
	def getMacros():
		return [
			OpenInTerminal,
			Rename,
			ComposerAutoload,
			ListenForDebug,
			StepOver,
			StepInto,
			StepOut,
			NextBreakpoint
		]

## COMMANDS ##

class OpenInTerminal(AbstractMacro):
	def getMacroName():
		return 'Open in terminal'
	def getMacro():
		keyboard.send(Keycode.ALT, Keycode.T)

class Rename(AbstractMacro):
	def getMacroName():
		return 'Rename'
	def getMacro():
		keyboard.send(Keycode.SHIFT, Keycode.F6)

class ListenForDebug(AbstractMacro):
	def getMacroName():
		return 'Listen for debug'
	def getMacro():
		keyboard.send(Keycode.ALT, Keycode.D)

class StepOver(AbstractMacro):
	def getMacroName():
		return 'Step over'
	def getMacro():
		keyboard.send(Keycode.F8)

class StepInto(AbstractMacro):
	def getMacroName():
		return 'Step into'
	def getMacro():
		keyboard.send(Keycode.F7)

class StepOut(AbstractMacro):
	def getMacroName():
		return 'Step out'
	def getMacro():
		keyboard.send(Keycode.SHIFT, Keycode.F8)

class NextBreakpoint(AbstractMacro):
	def getMacroName():
		return 'Next breakpoint'
	def getMacro():
		keyboard.send(Keycode.ALT, Keycode.COMMAND, Keycode.R)

class ComposerAutoload(AbstractMacro):
	def getMacroName():
		return 'Composer autoload'
	def getMacro():
		layout.write('composer dump')
		keyboard.send(Keycode.KEYPAD_MINUS)
		layout.write('autoload')
		keyboard.send(Keycode.ENTER)

class OneWeekEsteem(AbstractMacro):
	def getMacroName():
		return '< 1 week'
	def getMacro():
		layout.write(str(random.randint(1, 5)))
		keyboard.send(Keycode.ENTER)

class OneMonthEsteem(AbstractMacro):
	def getMacroName():
		return '< 1 month'
	def getMacro():
		layout.write(str(random.randint(5, 20)))
		keyboard.send(Keycode.ENTER)

class SixMonthsEsteem(AbstractMacro):
	def getMacroName():
		return '< 6 months'
	def getMacro():
		layout.write(str(random.randint(20, 120)))
		keyboard.send(Keycode.ENTER)
		

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

class MergeDevelop(AbstractMacro):
	def getMacroName():
		return "Merge develop into master"
	def getMacro():
		layout.write("git checkout master")
		keyboard.send(Keycode.ENTER)
		time.sleep(0.5)
		layout.write("git merge develop")
		keyboard.send(Keycode.ENTER)

class MergeMaster(AbstractMacro):
	def getMacroName():
		return "Merge master into develop"
	def getMacro():
		layout.write("git checkout develop")
		keyboard.send(Keycode.ENTER)
		time.sleep(0.5)
		layout.write("git merge master")
		keyboard.send(Keycode.ENTER)

class GitPush(AbstractMacro):
	def getMacroName():
		return "Push"
	def getMacro():
		layout.write("git push")
		keyboard.send(Keycode.ENTER)
		

# Map your configurations inside this array
configurations_map = [Terminal, GoogleMeet, Obsidian, RandomEstimation, PhpStorm, Git ]	
