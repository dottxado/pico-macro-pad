## Example configurations for Linux Ubuntu ##
import usb_hid
import time
import random

from abstract_classes import AbstractConfiguration, AbstractMacro
from empty_classes import EmptyConfiguration, EmptyMacro
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

class Obsidian(AbstractConfiguration):
	def getName():
		return 'Obsidian'
	def getColor():
		return (51, 51, 255)
	def getMacros():
		return [
			AddNewLog,
			AddNewDailyPlan,
			AddQuestionsDailyPlan
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
			SelectOpenedFile,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			ListenForDebug,
			StepOver,
			StepInto,
			StepOut,
			NextBreakpoint
		]


class Zoom(AbstractConfiguration):
	def getName():
		return 'Zoom'
	def getColor():
		return (80, 140, 246)
	def getMacros():
		return [
			ToggleMicrophoneZoom,
			EmptyMacro,
			ToggleVideoZoom,
			EmptyMacro,
			ToggleScreenShareZoom,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			LeaveMeetingZoom
		]


class NumPad(AbstractConfiguration):
	def getName():
		return 'Numeric pad'
	def getColor():
		return (205, 255, 0)
	def getMacros():
		return [
			Num0,
			Num1,
			Num2,
			Num3,
			Num4,
			Num5,
			Num6,
			Num7,
			Num8,
			Num9
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
		keyboard.send(Keycode.F9)

class SelectOpenedFile(AbstractMacro):
	def getMacroName():
		return 'Select Opened File'
	def getMacro():
		keyboard.send(Keycode.SHIFT, Keycode.F1)

class Ls(AbstractMacro):
	def getMacroName():
		return 'll'
	def getMacro():
		layout.write("ll")
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
		layout.write("cd $HOME")
		keyboard.send(Keycode.ENTER)

class AddNewLog(AbstractMacro):
	def getMacroName():
		return 'New Log'
	def getMacro():
		keyboard.send(Keycode.CONTROL, Keycode.P)
		layout.write("Insert template")
		time.sleep(0.1)
		keyboard.send(Keycode.ENTER)
		layout.write("New log")
		time.sleep(0.1)
		keyboard.send(Keycode.ENTER)

class AddNewDailyPlan(AbstractMacro):
	def getMacroName():
		return 'New daily plan'
	def getMacro():
		keyboard.send(Keycode.CONTROL, Keycode.P)
		layout.write("Insert template")
		time.sleep(0.1)
		keyboard.send(Keycode.ENTER)
		layout.write("New daily plan")
		time.sleep(0.1)
		keyboard.send(Keycode.ENTER)

class AddQuestionsDailyPlan(AbstractMacro):
	def getMacroName():
		return 'Add questions for next daily'
	def getMacro():
		keyboard.send(Keycode.CONTROL, Keycode.P)
		layout.write("Insert template")
		time.sleep(0.1)
		keyboard.send(Keycode.ENTER)
		layout.write("Questions for next daily")
		time.sleep(0.1)
		keyboard.send(Keycode.ENTER)


class ToggleMicrophoneZoom(AbstractMacro):
	def getMacroName():
		return "Toggle microphone"
	def getMacro():
		keyboard.send(Keycode.ALT, Keycode.A)

class ToggleVideoZoom(AbstractMacro):
	def getMacroName():
		return "Toggle video"
	def getMacro():
		keyboard.send(Keycode.ALT, Keycode.V)

class ToggleScreenShareZoom(AbstractMacro):
	def getMacroName():
		return "Toggle screen share"
	def getMacro():
		keyboard.send(Keycode.ALT, Keycode.S)

class LeaveMeetingZoom(AbstractMacro):
	def getMacroName():
		return "Close call"
	def getMacro():
		keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.E)

class Num0(AbstractMacro):
	def getMacroName():
		return "Number 0"
	def getMacro():
		layout.write("0")

class Num1(AbstractMacro):
	def getMacroName():
		return "Number 1"
	def getMacro():
		layout.write("1")

class Num2(AbstractMacro):
	def getMacroName():
		return "Number 2"
	def getMacro():
		layout.write("2")

class Num3(AbstractMacro):
	def getMacroName():
		return "Number 3"
	def getMacro():
		layout.write("3")
		
class Num4(AbstractMacro):
	def getMacroName():
		return "Number 4"
	def getMacro():
		layout.write("4")

class Num5(AbstractMacro):
	def getMacroName():
		return "Number 5"
	def getMacro():
		layout.write("5")

class Num6(AbstractMacro):
	def getMacroName():
		return "Number 6"
	def getMacro():
		layout.write("6")

class Num7(AbstractMacro):
	def getMacroName():
		return "Number 7"
	def getMacro():
		layout.write("7")

class Num8(AbstractMacro):
	def getMacroName():
		return "Number 8"
	def getMacro():
		layout.write("8")

class Num9(AbstractMacro):
	def getMacroName():
		return "Number 9"
	def getMacro():
		layout.write("9")


# Map your configurations inside this array
configurations_map = [ NumPad, Zoom, Obsidian, EmptyConfiguration, Terminal, PhpStorm ]	
