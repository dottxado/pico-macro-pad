import time
import board
import busio

from configurations import configurations_map

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

# Set up the keyboard

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

held = [0] * 16
button_mode = ButtonMode.CONFIGURATION_CHOSER
chosen_configuration = 0


def updateLeds():
	global held
	
	if button_mode == ButtonMode.CONFIGURATION_CHOSER and all(state == 0 for state in held):
		for i in range(16):
			if i < len(configurations_map):
				pixels[i] = configurations_map[i].getColor()
			else:
				pixels[i] = (0, 0, 0)
		
	elif button_mode == ButtonMode.MACRO_CHOSER:
		for i in range(16):
			if chosen_configuration < len(configurations_map):
				if i < min(len(configurations_map[chosen_configuration].getMacros()), 15):
					pixels[i] = configurations_map[chosen_configuration].getColor()
				else: 
					pixels[i] = (0, 0, 0)

		pixels[15] = (255, 255, 255)
		

def readButton(delay):
	global button_mode
	global chosen_configuration
	global configurations_map

	pressed = read_button_states(0, 16)
	for i in range(16):
		if pressed[i]:

			if button_mode == ButtonMode.CONFIGURATION_CHOSER:
				if i < len(configurations_map):
					chosen_configuration = i
					button_mode = ButtonMode.MACRO_CHOSER
					logMacros()
					time.sleep(delay)
			elif button_mode == ButtonMode.MACRO_CHOSER:
				if not held[i]:
					held[i] = 1
					if chosen_configuration < len(configurations_map):
						macros = configurations_map[chosen_configuration].getMacros()
						if i < len(macros):
							print("Selected macro: " + macros[i].getMacroName())
							macros[i].getMacro()
						else:
							configurations_map[chosen_configuration].nothing()

				if i == 15:
					button_mode = ButtonMode.CONFIGURATION_CHOSER
					logConfigurations()
					time.sleep(delay)
			
		else:
			held[i] = 0

def logConfigurations():
	print("Available configurations:")
	for j in range(len(configurations_map)):
		print(str(j) + ": " + configurations_map[j].getName())

def logMacros():
	if chosen_configuration < len(configurations_map):
		print("Selected configuration: " + configurations_map[chosen_configuration].getName())
		print("Available macros:")
		macros = configurations_map[chosen_configuration].getMacros()
		for j in range(len(macros)):
			print( str(j) + ": " + macros[j].getMacroName())


logConfigurations()
while True:
	updateLeds()
	readButton(0.3)
	time.sleep(0.001)