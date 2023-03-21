from microbit import *
import radio
from maqueen import *

robot = Maqueen()
radio.config(group=23)
radio.on()

while True:
    message = radio.receive()
    if message == '1':
        robot.set_led(0, 1)
        sleep(200)
        robot.set_led(0, 0)
        sleep(200)        

    if message == '2':
        robot.set_led(1, 1)
        sleep(200)
        robot.set_led(1, 0)
        sleep(200)        
