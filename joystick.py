# -*- encoding: utf-8 -*-

###############################################################################
# joystick.py
#
# Copyright (C) 2012 Fernando López <soportelihuen AT linti.unlp.edu.ar>
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

try:
    import pygame
    # Inicializar solamente el Joystick es más rápido pero suele fallar
    pygame.init()
except ImportError:
    print('Para usar joysticks tenés que instalar pygame')


def joysticks():
    "Retorna una lista joysticks conectados"
    Joystick._Joystick__refresh()
    joys = []
    for id in range(pygame.joystick.get_count()):
        j = pygame.joystick.Joystick(id)
        joys.append((id, j.get_name(),))
        j.quit()
    return joys


class Joystick:
    "Permite controlar un robot con un joystick"
    if 'pygame' in globals():
        joystickDetected = pygame.joystick.get_count() > 0
    else:
        joystickDetected = False

    @classmethod
    def __refresh(cls):
        """Esta función permite conectar el joystick aun después de haber
        importado el módulo, pero solo tendrá efecto una vez luego de
        detectar algún joystick (es decir si se conectan o desconectan
        joysticks más tarde la función no tendrá efecto)"""
        if pygame.joystick.get_count() == 0 and not Joystick.joystickDetected:
            pygame.joystick.quit()
            pygame.joystick.init()
            Joystick.joystickDetected = pygame.joystick.get_count() > 0

    def __init__(self, robot, joystickNumber=0):
        """Crea un joystick asociado con un objeto Robot, si
        no se idica el numero de joystick se asume 0"""
        Joystick.__refresh()
        self.js = pygame.joystick.Joystick(joystickNumber)
        self.js.init()
        self.robot = robot

    def play(self):
        """Permite controlar un robot con un joystick analógico o
        digital, cuando se usan los botones el robot
        se mueve a velocidad máxima, si se usa un control analógico
        se puede graduar la velocidad"""
        previous = None  # Permite evitar procesar eventos repetidos
        # Las siguientes 3 variables sirven para evitar conflictos
        # entre los eventos que se generan para cada eje.
        forward = False
        rotate = False
        digitalRotate = False
        while True:
            event = pygame.event.wait()
            if (
                    previous and
                    event.type == pygame.JOYAXISMOTION and
                    event.joy == previous.joy and
                    event.value == previous.value and
                    event.axis == previous.axis):
                pass
            else:
                if event.type == pygame.JOYAXISMOTION:
                    previous = event
                elif event.type == pygame.JOYBUTTONDOWN and event.button == 9:
                    return
                else:
                    continue

                if event.axis == 2 or event.axis == 1:
                    vel = event.value * 100
                    if vel > 100:
                        vel = 100
                    elif vel < -100:
                        vel = -100
                    if event.axis == 1 and not rotate:
                        self.robot.forward(-vel)
                        forward = vel != 0
                    elif event.axis == 2 and not forward and not digitalRotate:
                        self.robot.turnLeft(-vel)
                        rotate = vel != 0
                elif event.axis == 0:
                    digitalRotate = True
                    if event.value > 0:
                        self.robot.turnRight(100)
                    elif event.value < 0:
                        self.robot.turnLeft(100)
                    else:
                        digitalRotate = False
                        self.robot.stop()
