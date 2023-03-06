from microbit import *
from maqueen import *

robot = Maqueen()

while True:
    distancia = robot.read_distance()
    print(distancia)