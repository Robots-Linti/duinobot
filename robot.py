#!/bin/python
# -*- coding: utf-8 -*-
###############################################################################
# duinobot-interactive
# Conjunto de clases python para permitir que el robot Multiplo Duinobot N6
# pueda programarse en forma interactiva, sin necesidad de bajar firmware al
# robot. Sin embargo es necesario el soporte del firmware del lado del robot
#
# Copyright (C) 2011 David Vilaseca <http://www.robotgroup.com.ar>
# Copyright (C) 2011 Joaquín Bogado <jbogado en linti.unlp.edu.ar>
# 
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the RobotGroup Multiplo Pacifist License (RMPL)
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the RMPL license along with this program. 
# If not, see <multiplo.com.ar/soft/Mbq/Lic.Minibloq.ESP.pdf>.
###############################################################################

from pyfirmata import DuinoBot, util

class Board:
    def __init__(self, device='/dev/ttyUSB0'):
        '''Inicializa el dispositivo de conexion con el/los robot/s'''
        self.board = DuinoBot(device)
        it = util.Iterator(self.board)
        it.start()
        self.board.pass_time(0.1)

    def __del__(self):
        self.exit()
        
    def motor0(self,vel,robotid):
        if(vel >= 0 and vel <= 100):
            self.board.send_sysex(1,[int(vel), robotid])    

    def motor1(self,vel,robotid):
        if(vel >= 0 and vel <= 100):
            self.board.send_sysex(2,[int(vel), robotid])   
            
    def motors(self,vel1, vel2, seconds=-1, robotid=0):
        if(abs(vel1)<=100 and abs(vel2)<=100):
            self.board.send_sysex(4,[int(abs(vel1)), int(abs(vel2)), 1 if vel1>0 else 0, 1 if vel2>0 else 0, robotid])   
            if seconds!=-1:
                self.board.pass_time(seconds)
                self.motors(0,0,-1,robotid)

    def ping(self,robotid):
        self.board.send_sysex(3,[robotid])
        # wait 20ms (ping delay) + 20ms (comm)
        self.board.pass_time(0.04)
        return self.board.nearest_obstacle[robotid]  

    def sleep(self,time):
        self.board.pass_time(time)

    def exit(self):
        self.board.exit()
        
    def analog(self,ch,samples=1,robotid=0): 
        self.board.send_sysex(6,[ch, samples, robotid])
        self.board.pass_time(0.04)
        return self.board.analog_value[robotid]

    def battery(self,robotid): 
        self.board.send_sysex(6,[6, 1, robotid])
        self.board.pass_time(0.04)
        return self.board.analog_value[robotid]*5.0/1024

    def digital(self,pin,robotid): 
        self.board.send_sysex(7,[pin,robotid])
        self.board.pass_time(0.04)
        return self.board.digital_value[robotid]
        
    def beep(self, freq=0, microseconds=0, robotid=0):
        hi=freq>>7
        lo=freq%128
        if freq!=0:
            if microseconds==0:
                self.board.send_sysex(5,[hi, lo, robotid])
            else:
                self.board.send_sysex(5,[hi, lo, int(microseconds*1000), robotid])
                #self.board.pass_time(microseconds)

        else:
            self.board.send_sysex(5,[robotid])

    def report(self): 
    	self.board.live_robots=[0 for i in range(128)]
        self.board.send_sysex(9,[])
        self.board.pass_time(0.5)
        for i in range(128):
            if self.board.live_robots[i]:
                print "Robot", i, "prendido"

    def set_id(self,new_id,robotid): 
        self.board.send_sysex(8,[new_id,robotid])
        self.board.pass_time(0.02)
    
    def getLine(self, robotid):
        a = self.analog(18,robotid=robotid)
        b = self.analog(19,robotid=robotid)
        return (a,b)

    wait = sleep

class Robot:
    def __init__(self, board, robotid=0):
        '''Inicializa el robot y lo asocia con la placa board'''
        self.robotid = robotid
        self.board = board
        self.name = ''
        
    def __del__(self):
        self.board.exit()
        
    ##MOVIMIENTO
    def forward(self, vel=50, seconds=-1):
        '''El robot avanza con vel impulse durante seconds seconds.'''
        self.board.motors(vel, vel, seconds, self.robotid)

    def backward(self, vel=50, seconds=-1):
        '''El robot retrocede con velocidad vel durante seconds segundos.'''
        self.forward(-vel, seconds)
    
    def motors(self, vel1, vel2, seconds=-1):
		'''Permite mover las ruedas independientemente, con velocidad vel1 para un motor y vel2 para el otro motor, durante second'''
		self.board.motors(vel1, vel2, seconds, self.robotid)

    def turnLeft(self, vel=50, seconds=-1):
       '''El robot gira a la izquierda con velocidad vel durante seconds segundos.'''
       self.board.motors(vel, 0, seconds, self.robotid)

    def turnRight(self, vel=50, seconds=-1):
        '''El robot gira a la derecha con velocidad vel durante seconds segundos.'''
        self.board.motors(0, vel, seconds, self.robotid)

    def stop(self):
        '''Detiene todo movimiento del robot inmediatamente'''
        self.board.motors(0, 0, robotid=self.robotid)

    ##SENSORES
    def getLine(self):
        '''Devuelve los valores de los sensores de Line.'''
        return self.board.getLine(self.robotid)

    def getObstacle(self, distance=10):
        '''Devuelve True si hay un obstaculo a menos de distance
         centimetros del robot.'''
        if self.board.ping(self.robotid) < distance :
            return True
        else:
            return False

    def battery(self):
        '''Devuelve el voltaje de las baterías del robot.'''
        return self.board.battery(self.robotid)

    def ping(self):
        '''Devuelve la distancia en centimetros al objeto frente al robot'''
        return self.board.ping(self.robotid)

    def beep(self, freq=0, seconds=0):
        '''Hace que el robot emita un pitido con frecuencia freq durante seconds segundos'''
        self.board.beep(freq, robotid=self.robotid)
        self.board.wait(seconds)
        self.board.beep(0, robotid=self.robotid)
        
    def wait(self, seconds):
        '''Produce un retardo de seconds segundos en los que el robot no hace nada'''
        self.board.wait(seconds)

    def sensors(self):
        '''Imprime informacion de los sensores.'''
        print 'Line = ' + str(self.getLine()) 
        print 'Obstaculo mas cercano = ' + str(self.ping()) + ' cm.'
        print 'Bateria = ' + str(self.battery()) + ' v.'
    
    ##Identificadores
    def setId(self, newid):
        '''Setea el robotid'''
        self.board.set_id(newid, self.robotid)
        self.robotid = newid
    
    def setName(self, name):
        '''Setea el nombre para el robot.'''
        self.name = str(name)
    
    def getId(self):
        '''Devuelve el robotid.'''
        return self.robotid

    def getName(self):
        '''Devuelve el nombre del robot.'''
        return self.name
    
    ## Otras funciones
    def speak(self, msj):
        '''Imprime en la terminal el mensaje msj'''
        print msj

from senses import *
Robot.senses = senses
