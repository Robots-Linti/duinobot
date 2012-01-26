#!/bin/python

from pyfirmata import DuinoBot, util
from robot import Board, Robot
from time import *


b = Board()
r = Robot(b,1)

ctime = time()
while time() - ctime < 30:
    l1, l2 = r.getLine()
    if l1 < 500 or l2 < 500:
        r.turnRight(100, 0.5)
    else:
        r.forward(50)
r.stop()
b.exit()
