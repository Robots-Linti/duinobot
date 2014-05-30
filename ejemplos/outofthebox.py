#!/bin/python
# -*- coding: utf-8 -*-

from duinobot import *
from time import *


b = Board('/dev/ttyUSB0')
r = Robot(b, 1)

ctime = time()
while time() - ctime < 30:
    l1, l2 = r.getLine()
    if l1 < 500 or l2 < 500:
        r.backward(30, 0.7)
        r.turnRight(30, 0.7)
    else:
        r.forward(30)
r.stop()
b.exit()
