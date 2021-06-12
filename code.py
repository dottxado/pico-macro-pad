import time
import board
import busio

from configurations import configurations_map
from empty_classes import EmptyConfiguration, EmptyMacro

from adafruit_bus_device.i2c_device import I2CDevice
import adafruit_dotstar


from digitalio import DigitalInOut, Direction, Pull

# Pull CS pin low to enable level shifter
cs = DigitalInOut(board.GP17)
cs.direction = Direction.OUTPUT
cs.value = 0

# Set up APA102 pixels
num_pixels = 16
pixels = adafruit_dotstar.DotStar(board.GP18, board.GP19, num_pixels, brightness=0.2, auto_write=True)

# Set up I2C for IO expander (addr: 0x20)
i2c = busio.I2C(board.GP5, board.GP4)
device = I2CDevice(i2c, 0x20)

# Define two modes for the keyboard
class ButtonMode:
	CONFIGURATION_CHOSER = 0
	MACRO_CHOSER = 1

# Function to map 0-255 to position on colour wheel
def colourwheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

# Read button states from the I2C IO expander on the keypad
def read_button_states(x, y):
    pressed = [0] * 16
    with device:
        # Read from IO expander, 2 bytes (8 bits) correspond to the 16 buttons
        device.write(bytes([0x0]))
        result = bytearray(2)
        device.readinto(result)
        b = result[0] | result[1] << 8

        # Loop through the buttons
        for i in range(x, y):
            if not (1 << i) & b:
                pressed[i] = 1
            else:
                pressed[i] = 0
    return pressed

# Define initial values for the global variables
held = [0] * 16
button_mode = ButtonMode.CONFIGURATION_CHOSER
last_button_mode = ''
chosen_configuration = 0

# Manage the colors of the buttons, depending on the mode and the available congigurations/macros
def updateLeds():
	global held
	global last_button_mode
	
	if button_mode == ButtonMode.CONFIGURATION_CHOSER and last_button_mode != ButtonMode.CONFIGURATION_CHOSER:
		last_button_mode = ButtonMode.CONFIGURATION_CHOSER
		for i in range(16):
			if i < len(configurations_map):
				pixels[i] = configurations_map[i].getColor()
			else:
				pixels[i] = (0, 0, 0)
		
	elif button_mode == ButtonMode.MACRO_CHOSER and last_button_mode != ButtonMode.MACRO_CHOSER:
		last_button_mode = ButtonMode.MACRO_CHOSER
		for i in range(16):
			if chosen_configuration < len(configurations_map):
				if i < min(len(configurations_map[chosen_configuration].getMacros()), 15) and not issubclass(configurations_map[chosen_configuration].getMacros()[i], EmptyMacro):
					pixels[i] = configurations_map[chosen_configuration].getColor()
				else: 
					pixels[i] = (0, 0, 0)

		pixels[15] = (255, 255, 255)
		
# Read button press
def readButton(delay):
	global button_mode
	global chosen_configuration
	global configurations_map

	pressed = read_button_states(0, 16)
	for i in range(16):
		if pressed[i]:

			if button_mode == ButtonMode.CONFIGURATION_CHOSER:
				if i < len(configurations_map) and not issubclass(configurations_map[i], EmptyConfiguration):
					chosen_configuration = i
					button_mode = ButtonMode.MACRO_CHOSER
					logMacros()
					time.sleep(delay)
			elif button_mode == ButtonMode.MACRO_CHOSER:
				if not held[i]:
					held[i] = 1
					if chosen_configuration < len(configurations_map):
						macros = configurations_map[chosen_configuration].getMacros()
						if i < len(macros) and not issubclass(macros[i], EmptyMacro):
							logMessage("Selected macro: " + macros[i].getMacroName())
							macros[i].getMacro()
						else:
							configurations_map[chosen_configuration].nothing()

				if i == 15:
					button_mode = ButtonMode.CONFIGURATION_CHOSER
					logConfigurations()
					time.sleep(delay)
			
		else:
			held[i] = 0

# Build a message for the user with the available configurations
def logConfigurations():
	logMessage("Available configurations:")
	for j in range(len(configurations_map)):
		logMessage(str(j) + ": " + configurations_map[j].getName())

# Build a message for the user with the selected configuration and the available macros
def logMacros():
	if chosen_configuration < len(configurations_map):
		logMessage("Selected configuration: " + configurations_map[chosen_configuration].getName())
		logMessage("Available macros:")
		macros = configurations_map[chosen_configuration].getMacros()
		for j in range(len(macros)):
			logMessage( str(j) + ": " + macros[j].getMacroName())

# Print the message to the serial console
def logMessage(message):
	print(message)


logConfigurations()
while True:
	updateLeds()
	readButton(0.3)
	time.sleep(0.001)