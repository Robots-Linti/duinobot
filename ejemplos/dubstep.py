#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#http://www.jamendo.com/es/track/324954/xxl080808
from duinobot import *
import os
b = Board()
r1 = Robot(b, 5)
r2 = Robot(b, 0)

pid = os.fork()
if pid == 0:
	salida = os.open('/dev/null', os.O_WRONLY)
	os.dup2(salida, 2)
	os.dup2(salida, 1)
	os.execlp('mplayer', 'mplayer', '-nojoystick', 'ArenaOfElectronicMusicRazormanMechanical.mp3')

def uno(t):
	lr1,lr2 = r1,r2
	while t > 0:
		lr1.forward(80)		
		lr2.turnRight(40, 0.5)
		lr1.backward(80)		
		lr2.turnLeft(40, 0.5)		
		lr1.stop()
		lr1, lr2 = lr2, lr1
		t -= 1	
def dos(t):
	lr1,lr2 = r1,r2
	
	
	while t > 0:
		lr1.turnRight(60)
		lr2.turnLeft(60, 2)
			
		lr2.backward(30)	
		lr1.forward(60, 1)		
		lr2.stop()
		lr1, lr2 = lr2, lr1
		t -= 3	
def tres(t):
	lr1,lr2 = r1,r2
	
	
	while t > 0:
		lr1.turnRight(60)
		lr2.turnLeft(60, 2)
			
		lr2.backward(30)	
		lr1.forward(60, 1)		
		lr2.stop()
		lr1, lr2 = lr2, lr1
		t -= 3	
def pausa(t):
	r1.stop()
	r2.stop()
	lr1,lr2 = r1,r2
	sonido = 0.9
	while t > 0:
		lr1.beep(200, sonido)		
		lr2.beep(1200,sonido)
		lr1, lr2 = lr2, lr1
		sonido = 0.1
		t -= 1
	#if t != 0:
	#	wait(t)
def dosRapido(t):
	pasito = t / 16.0
	lr1, lr2 = r1, r2
	for i in range(16):
		lr1.turnLeft(100)
		restante = pasito
		while restante > 0:
			lr2.forward(60, .5)
			lr2.backward(30, .5)
			restante -= 1
		lr1, lr2 = lr2, lr1
def punchi(t):
	lr1, lr2 = r1, r2
	while t > 0:
		lr1.turnLeft(100, .5)
		lr2.turnRight(100, .5)
		lr1, lr2 = lr2, lr1
		t -= 1
def masTranqui(t):
	r1.motors(60, -40)
	r2.motors(-40, 60)
	wait(t)
def despacito(t):
	r1.motors(40, -30)
	r2.motors(-30, 40)
	wait(t)

pasos = [
	(27, uno),
	(47 - 28, dos),
	#(56, pausa),
	#(60 + 25, dosRapido),
	#(120 + 30, punchi),
	#(120 + 50, masTranqui),
	#(180 + 12, pausa),
	#(180 + 35, despacito),
	#(300 + 35, punchi),
	#(300 + 45, masTranqui),
	#(0, pausa)
]

for tiempo, paso in pasos:
	print(str(paso))
	paso(tiempo)
	

b.exit()
