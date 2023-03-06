from microbit import *
from maqueen import *

robot = Maqueen()

while True:
    distancia = robot.read_patrol(0)
    print(distancia)
    distancia = robot.read_patrol(1)
    print(distancia)