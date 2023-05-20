from microbit import *
import time
from maqueen import *

robot = Maqueen()

while True:
    if button_b.was_pressed():
        robot.motor_stop_all()
        
    if button_a.was_pressed():
        tiempoDetectandoHueco = 0
        tiempoActual = 0
        robot.set_motor(0, 50)
        robot.set_motor(1, 50)

        while tiempoDetectandoHueco < 500:
            if robot.read_distance() < 6:
                display.show(Image.NO)
                tiempoDetectandoHueco = 0
                tiempoActual = time.ticks_ms()
            else:
                display.show(Image.YES)
                tiempoDetectandoHueco = time.ticks_ms() - tiempoActual

        display.show(Image.HEART)
        robot.motor_stop_all()
        # Comienza aparcamiento
        robot.set_motor(0, -50)
        sleep(500)
        robot.set_motor(1, -50)
        sleep(650)
        robot.set_motor(0, 0)
        sleep(500)
        robot.motor_stop_all()