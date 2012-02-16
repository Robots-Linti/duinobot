from robot import *
import time 
b = Board("/dev/ttyUSB0")
robot = Robot(b, 1)

for i in range(0, 4):
    robot.forward(50, .5)
    robot.turnRight(50, 1)
    time.sleep(1)


