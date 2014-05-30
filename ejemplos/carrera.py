# -*- encoding: utf-8 -*-
# Solución del ejercicio 4 de la sección 3.2.3.
from duinobot import *

b = Board("/dev/ttyUSB0")

robot1 = Robot(b, 1)
robot2 = Robot(b, 10)


def carrera(r1, r2, tiempo):
    r1.forward(100)
    r2.forward(100)
    wait(tiempo)
    r1.stop()
    r2.stop()

carrera(robot1, robot2, 3)

b.exit()
