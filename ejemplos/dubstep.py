#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# http://www.jamendo.com/es/track/324954/xxl080808
# http://www.jamendo.com/es/track/247586/razorman-mechanical
from duinobot import *
import os
b = Board()
r1 = Robot(b, 5)
r2 = Robot(b, 18)

pid = os.fork()
if pid == 0:
    salida = os.open('/dev/null', os.O_WRONLY)
    os.dup2(salida, 2)
    os.dup2(salida, 1)
    os.execlp('mplayer',
              'mplayer',
              '-nojoystick',
              'ArenaOfElectronicMusicRazormanMechanical.mp3')


def uno(t):
    lr1, lr2 = r1, r2
    while t > 0:
        lr1.forward(80)
        lr2.turnRight(40, 0.5)
        lr1.backward(80)
        lr2.turnLeft(40, 0.5)
        lr1.stop()
        lr1, lr2 = lr2, lr1
        t -= 1


def dos(t):
    lr1, lr2 = r1, r2

    while t > 0:
        lr1.turnRight(60)
        lr2.turnLeft(70, 0.5)

        lr2.backward(30)
        lr1.forward(70, 0.5)
        lr2.stop()
        lr1, lr2 = lr2, lr1
        t -= 1


def tres(t):
    lr1, lr2 = r1, r2
    while t > 0:
        lr2.turnRight(60)
        lr1.forward(30, 4)

        lr1.backward(30)
        lr2.turnLeft(60, 4)
        lr1.stop()
        t -= 8


def pausa(t):
    print "acomodar Robots!!"
    r1.stop()
    r2.stop()
    lr1, lr2 = r1, r2
    sonido = 0.9
    while t > 0 and sonido > 0:
        lr1.beep(200, sonido)
        lr2.beep(1200, sonido)
        lr1, lr2 = lr2, lr1
        t -= 2*sonido
        sonido -= 0.1
    # if t != 0:
    #     wait(t)


def punchi(t):
    lr1, lr2 = r1, r2
    while t > 0:
        lr1.beep(200)
        lr1.turnLeft(100)
        lr2.turnRight(100, .5)
        lr1.beep(0)
        lr1.stop()
        lr1, lr2 = lr2, lr1
        t -= 0.5

pasos = [
    (27, uno),
    (47 - 28, dos),
    (55 - 47, pausa),
    (65 - 55, tres),
    (75 - 65, dos),
    (81 - 75, punchi),
    (91 - 81, pausa),
    (110 - 91, uno),
    (120 - 110, punchi),
]

for tiempo, paso in pasos:
    print(str(paso))
    paso(tiempo)


b.exit()
