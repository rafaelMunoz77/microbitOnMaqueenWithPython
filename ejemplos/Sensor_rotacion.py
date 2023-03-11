# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    readingX = accelerometer.get_x()
    if (readingX < -500):
        display.set_pixel(0, 2, 9)
    else:
        display.set_pixel(0, 2, 0)
        
    if (readingX > 500):
        display.set_pixel(4, 2, 9)
    else:
        display.set_pixel(4, 2, 0)


    readingY = accelerometer.get_y()
    if (readingY < -500):
        display.set_pixel(2, 0, 9)
    else:
        display.set_pixel(2, 0, 0)
    
    if (readingY > 500):
        display.set_pixel(2, 4, 9)
    else:
        display.set_pixel(2, 4, 0)
    