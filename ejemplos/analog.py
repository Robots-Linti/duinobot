from duinobot import *
import sys

b = Board()
# id del robot
idr = 1
r = Robot(b, idr)

while 1:
    for i in range(6):
        print b.analog(i, robotid=idr),
        print '\t',
    print '\n',
    if r.ping() < 50:
        break


b.exit()
