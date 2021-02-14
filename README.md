# Macro Pad for Raspberry Pi Pico with Pimoroni Pico RGB Keypad Base 

This project creates a little&coloured macro pad with a Raspberry Pi Pico, using the [Pico RGB Keypad Base](https://shop.pimoroni.com/products/pico-rgb-keypad-base) by Pimoroni.

You can define 16 different configurations, with their name and their associated colour, and for each configuration an array of 15 different macros. 
When you start the Pico, the first thing that you will see will be the "configuration choser": the available configurations will colour the respective button. Pushing one button will select a configuration, giving you a "macro choser": the available macros will colour their respective button of the same color of the configuration. In this mode, the sixteenth button will be identified by a white light, and pushing it will let you return to the "configuration choser".

To have a more clear view, just hook up your serial console on the Pico, and you will see helpful messages with the id and the configuration/macro name. If you need to see the serial console in the terminal, follow this [AdaFruit guide for advanced serial console](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-mac-and-linux).

## Prerequisites
- CircuitPython loaded on the Pico -> [link to the source](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython)
- [CircuitPython libraries](https://github.com/adafruit/Adafruit_CircuitPython_Bundle) loaded in the "lib" folder of the Pico:
    + adafruit_hid
    + adafruit_bus_device
    + adafruit_dotstar
- From this repository, load code.py, abstract_classes.py and configurations.py in your Pico

## How to modify the configurations and the macros
The code is organized in a way that permits the user to edit the macros without touching the core code that manages the keyboard.
You need to know that you must follow the abstract classes defined in the file abstract_classes.py to define your configurations and your macro, then you can check my examples into configurations.py. Create your classes and remember to add the configuration classes in the array at the end of the configurations.py file.

## Credits
I'm not a python developer, on the microcontrollers I only love to mess a little with C++ on Arduino, so this project gave me a way to finally approach some python with a goal in mind. Thanks to [sandyjmacdonald](https://gist.github.com/sandyjmacdonald) and [pixlwave](https://github.com/pixlwave), I've taken some pieces of their code and various inspiration.
