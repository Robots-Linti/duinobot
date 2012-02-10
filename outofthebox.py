#!/bin/python

from robot import Board, Robot
from time import *


b = Board('/dev/ttyUSB1')
r = Robot(b,1)

ctime = time()
while time() - ctime < 30:
    l1, l2 = r.getLine()
    if l1 < 500 or l2 < 500:
        r.backward(30, 0.5)
        r.turnRight(30, 0.5)
    else:
        r.forward(30)
r.stop()
b.exit()
