from microbit import *
import radio
from maqueen import *

robot = Maqueen()
radio.config(group=23)
radio.on()

while True:
    radio.send('1')
    robot.set_led(0, 1)
    sleep(200)
    robot.set_led(0, 0)
    sleep(200)

    radio.send('2')
    robot.set_led(1, 1)
    sleep(200)
    robot.set_led(1, 0)
    sleep(200)