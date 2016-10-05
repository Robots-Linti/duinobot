#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from duinobot import *

board = Board('/dev/ttyUSB0')
robot = Robot(board, 1)

if not joysticks():
    print('No se encontró ningún joystick')
    board.exit()
    exit()

print('Ahora puede controlar el robot usando el joystick, '
      'presione el botón "start" para terminar el programa.')
# Si esto falla ejecutar joysticks() de forma interactiva para ver
# cuántos joysticks se detectaron
# si hay más de uno, indique el número del que desea utilizar como
# segundo argumento de Joystick().
joystick = Joystick(robot)
joystick.play()

board.exit()
