import usb_hid
import time
import random

from abstract_classes import AbstractConfiguration, AbstractMacro, AbstractLoopMacro
from empty_classes import EmptyConfiguration, EmptyMacro
from adafruit_hid.keyboard import Keyboard
from keyboard_layout import KeyboardLayout
from keyboard_keycodes import Keycode
from adafruit_hid.mouse import Mouse

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)
mouse = Mouse(usb_hid.devices)

## CONFIGURATIONS ##

class Ddev(AbstractConfiguration):
	def getName():
		return 'DDEV'
	def getColor():
		return (64,81,181)
	def getMacros():
		return [
			DdevStart, 
			DdevStop,
			DdevSame,
			Exit,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro
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
			NextBreakpoint,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro
		]
		
class Git(AbstractConfiguration):
	def getName():
		return 'GIT'
	def getColor():
		return (241,78,50)
	def getMacros():
		return [
			CheckoutMainBranch,
			CheckoutNewBranch,
			CheckoutOldBranch,
			EmptyMacro,
			Add,
			Commit,
			Push,
			PushUpstream,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro
		]

class Composer(AbstractConfiguration):
	def getName():
		return 'Composer'
	def getColor():
		return (105, 169, 100)
	def getMacros():
		return [
			RunCodingStandards,
			RunFixCodingStandards,
			RunPsalm,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro
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

## COMMANDS ##

class RunCodingStandards(AbstractMacro):
	def getMacroName():
		return 'PHPCS'
	def getMacro():
		layout.write("composer run check-coding-standards")
		keyboard.send(Keycode.ENTER)

class RunFixCodingStandards(AbstractMacro):
	def getMacroName():
		return 'PHPCS fix'
	def getMacro():
		layout.write("composer run fix-coding-standards")
		keyboard.send(Keycode.ENTER)

class RunPsalm(AbstractMacro):
	def getMacroName():
		return 'PSalm'
	def getMacro():
		layout.write("composer run check-psalm:no-cache")
		keyboard.send(Keycode.ENTER)
			
class CheckoutNewBranch(AbstractMacro):
	def getMacroName():
		return 'Checkout creating branch'
	def getMacro():
		layout.write("git checkout -b ")
		
class CheckoutMainBranch(AbstractMacro):
	def getMacroName():
		return 'Checkout main branch'
	def getMacro():
		layout.write("git checkout main && git pull")
		keyboard.send(Keycode.ENTER)
		
class CheckoutOldBranch(AbstractMacro):
	def getMacroName():
		return 'Checkout old branch'
	def getMacro():
		layout.write("git checkout  && git pull")
		keyboard.send(Keycode.LEFT_ARROW)
		time.sleep(0.1)
		keyboard.send(Keycode.LEFT_ARROW)
		time.sleep(0.1)
		keyboard.send(Keycode.LEFT_ARROW)
		time.sleep(0.1)
		keyboard.send(Keycode.LEFT_ARROW)
		time.sleep(0.1)
		keyboard.send(Keycode.LEFT_ARROW)
		time.sleep(0.1)
		keyboard.send(Keycode.LEFT_ARROW)
		time.sleep(0.1)
		keyboard.send(Keycode.LEFT_ARROW)
		time.sleep(0.1)
		keyboard.send(Keycode.LEFT_ARROW)
		time.sleep(0.1)
		keyboard.send(Keycode.LEFT_ARROW)
		time.sleep(0.1)
		keyboard.send(Keycode.LEFT_ARROW)
		time.sleep(0.1)
		keyboard.send(Keycode.LEFT_ARROW)
		time.sleep(0.1)
		keyboard.send(Keycode.LEFT_ARROW)
		
class PushUpstream(AbstractMacro):
	def getMacroName():
		return 'Push upstream'
	def getMacro():
		layout.write("git push --set-upstream origin ")

class Push(AbstractMacro):
	def getMacroName():
		return 'Push'
	def getMacro():
		layout.write("git push")
		keyboard.send(Keycode.ENTER)

class Add(AbstractMacro):
	def getMacroName():
		return 'Add'
	def getMacro():
		layout.write("git add .")
		keyboard.send(Keycode.ENTER)

class Commit(AbstractMacro):
	def getMacroName():
		return 'Commit'
	def getMacro():
		layout.write("git commit -m\"\"")
		keyboard.send(Keycode.LEFT_ARROW)

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
		
class DdevStart(AbstractMacro):
	def getMacroName():
		return 'Start'
	def getMacro():
		layout.write("ddev auth ssh && ddev start")
		time.sleep(0.1)
		keyboard.send(Keycode.ENTER)

class DdevStop(AbstractMacro):
	def getMacroName():
		return 'Stop'
	def getMacro():
		layout.write("ddev stop")
		time.sleep(0.1)
		keyboard.send(Keycode.ENTER)
		
class DdevSame(AbstractMacro):
	def getMacroName():
		return 'Same'
	def getMacro():
		layout.write("ddev same")
		time.sleep(0.1)
		keyboard.send(Keycode.ENTER)
		
class Exit(AbstractMacro):
	def getMacroName():
		return 'Exit'
	def getMacro():
		layout.write("exit")
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





# Map your configurations inside this array
configurations_map = [ Ddev, Git, Composer, EmptyConfiguration, EmptyConfiguration, EmptyConfiguration, EmptyConfiguration, PhpStorm, EmptyConfiguration, EmptyConfiguration, EmptyConfiguration, EmptyConfiguration, Zoom, EmptyConfiguration ]	
