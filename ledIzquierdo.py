# Imports go at the top
from microbit import *

#neopixel.NeoPixel(pin15, 4)

while True:
    pin8.write_digital(0)
    sleep(100)
    pin8.write_digital(1)
    sleep(100)
    