from microbit import *
from maqueen import *

robot = Maqueen()

while True:
    robot.set_motor(0, 100)
    robot.set_motor(1, 100)
    sleep(500)
    robot.motor_stop_all()
    sleep(500)
    
