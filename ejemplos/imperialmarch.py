#!/bin/python

from duinobot import *

b = Board()
r = Robot(b, 1)


r.beep(500, 0.5)
wait(0.5)

r.beep(500, 0.5)
wait(0.5)

r.beep(500, 0.5)
wait(0.5)

r.beep(400, 0.5)
wait(0.4)

r.beep(600, 0.2)
wait(0.1)

r.beep(500, 0.5)
wait(0.5)

r.beep(400, 0.5)
wait(0.4)

r.beep(600, 0.2)
wait(0.1)

r.beep(500, 0.5)
wait(1)

r.beep(750, 0.5)
wait(0.5)

r.beep(750, 0.5)
wait(0.5)

r.beep(750, 0.5)
wait(0.5)

r.beep(810, 0.5)
wait(0.4)

r.beep(600, 0.2)
wait(0.1)

r.beep(470, 0.5)
wait(0.5)

r.beep(400, 0.5)
wait(0.4)

r.beep(600, 0.2)
wait(0.1)

r.beep(500, 0.5)
wait(1)

r.stop()
b.exit()
