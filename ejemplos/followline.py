#!/bin/python
# -*- coding: utf-8 -*-
from duinobot import *
from time import *


b = Board('/dev/ttyUSB0')
r = Robot(b, 1)

ctime = time()
# Sigue líneas negras sobre fondos blancos
r.forward(30)
r.senses()
while time() - ctime < 30:
    izq, der = r.getLine()
    if izq > 500:
        r.turnRight(30)
    elif der > 500:
        r.turnLeft(30)
    else:
        r.forward(30)
    wait(0.3)  # Espera al menos 0.3 segundos antes de volver a sensar
r.stop()
b.exit()
