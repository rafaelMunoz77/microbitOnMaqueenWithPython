from microbit import *
from maqueen import *

robot = Maqueen()

while True:
    robot.set_led(0, 1)
    sleep(200)
    robot.set_led(0, 0)
    sleep(200)