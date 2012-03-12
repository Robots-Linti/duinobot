#!/bin/python
# -*- coding: utf-8 -*-
from robot import Board, Robot
from time import *


b = Board('/dev/ttyUSB0')
r = Robot(b,1)

ctime = time()
#avanza hasta que detecta una línea
r.forward(30)

while time() - ctime < 30:
	izq, der = r.getLine()
	if izq > 500:
		while izq > 500 and time() - ctime < 30:
			r.turnRight(30, 0.2)
	if der > 500:
		while izq > 500 and time() - ctime < 30:
			r.turnLeft(30, 0.2)
	r.forward(30)
r.stop()
b.exit()
