from duinobot import *
b = Board("/dev/ttyUSB0")
robot = Robot(b, 1)

for i in range(0, 4):
    robot.forward(50, 2)
    robot.turnRight(50, .5)

b.exit()
