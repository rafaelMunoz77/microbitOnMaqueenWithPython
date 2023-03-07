import microbit
import machine
import utime
import neopixel

class Maqueen:

    def __init__(self):
        self.rgbleds = neopixel.NeoPixel(microbit.pin15, 4)
        print("MAQUEEN initialized")

    def set_led(self, lednumber, value):
        if lednumber == 0:
            microbit.pin8.write_digital(value)
        elif lednumber == 1:
            microbit.pin12.write_digital(value)

    def read_distance(self):
        divider = 42
        maxtime = 250 * divider
        microbit.pin2.read_digital()  # just for setting PULL_DOWN on pin2
        microbit.pin1.write_digital(0)
        utime.sleep_us(2)
        microbit.pin1.write_digital(1)
        utime.sleep_us(10)
        microbit.pin1.write_digital(0)

        duration = machine.time_pulse_us(microbit.pin2, 1, maxtime)
        distance = duration/divider
        return int(distance)

    def read_patrol(self, which):
        if which == 0:  # left
            return microbit.pin13.read_digital()
        elif which == 1:  # right
            return microbit.pin14.read_digital()

    def set_motor(self, motor, value):
        data = bytearray(3)
        if motor == 0:  # left motor
            data[0] = 0
        else:
            data[0] = 2  # right motor is 2
        if value < 0:  # ccw direction
            data[1] = 1
            value = -1*value
        data[2] = value
        microbit.i2c.write(0x10, data, False)  # 0x10 is i2c address of motor driver

    def motor_stop_all(self):
        self.set_motor(0, 0)
        self.set_motor(1, 0)

    def motor_stop(self, motor):
        self.set_motor(motor, 0)