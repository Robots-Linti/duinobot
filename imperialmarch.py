#!/bin/python

from pyfirmata import DuinoBot, util
from robot import Board, Robot
from time import *


b = Board()
r = Robot(b,1)


r.tone(500, 0.5)
r.wait(0.5)

r.tone(500, 0.5)
r.wait(0.5)

r.tone(500, 0.5)
r.wait(0.5)

r.tone(400, 0.5)
r.wait(0.4)

r.tone(600, 0.2)
r.wait(0.1)

r.tone(500, 0.5)
r.wait(0.5)

r.tone(400, 0.5)
r.wait(0.4)

r.tone(600, 0.2)
r.wait(0.1)

r.tone(500, 0.5)
r.wait(1)



r.tone(750, 0.5)
r.wait(0.5)

r.tone(750, 0.5)
r.wait(0.5)

r.tone(750, 0.5)
r.wait(0.5)

r.tone(810, 0.5)
r.wait(0.4)

r.tone(600, 0.2)
r.wait(0.1)

r.tone(470, 0.5)
r.wait(0.5)

r.tone(400, 0.5)
r.wait(0.4)

r.tone(600, 0.2)
r.wait(0.1)

r.tone(500, 0.5)
r.wait(1)

r.stop()
b.exit()
