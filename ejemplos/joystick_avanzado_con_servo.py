#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from duinobot import *
# Importamos pygame.joystick para poder controlar el servo con los
# botones de acción.
import pygame.joystick

# Inicializar el módulo de joysticks si es necesario.
if not pygame.joystick.get_init():
    pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)


board = Board('/dev/ttyUSB0')
robot = Robot(board, 1)

# En este caso el servomotor está conectado al pin digital 9 del
# robot.
robot.configServo(9)

# Botones: estos números corresponden a los botones a la derecha
# del modelo de joystick que pudimos probar.
abrir_brazo = 1         # 1 es el botón de acción izquierdo
cerrar_brazo = 3        # 3 es el derecho
descanzar_brazo = 2     # 2 es el de abajo
salir = 9               # 9 es el botón salir

# Ejes: pygame identifica los ejes del d-pad con estos números.
vertical = 1
horizontal = 0

# Estado: Usamos estas variables para controlar cuando el robot
# debe detenerse, la condición para detener el robot depende
# de qué tipo de movimiento está realizando en este momento.
moviendose_eje_vertical = False
moviendose_eje_horizontal = False

print('A continuación puede utilizar el Joystick')
print('Use las teclas de dirección para mover el robot')
print('El botón de acción izquierdo abre el brazo y el derecho lo cierra')
print('Use el botón de abajo para poner el brazo en una posición de descanzo mientras no lo utiliza para evitar forzar el motor')
print('Si presiona el botón start el programa termina')

# Inicializamos el joystick a usar para que pygame reporte los eventos
# generados por el mismo.
joystick.init()
seguir = True
while seguir:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == salir:
                seguir = False
            elif event.button == abrir_brazo:
                robot.moveServo(9, 0)
                wait(0.2)  # esperamos un tiempo para que el servo se mueva
            elif event.button == cerrar_brazo:
                robot.moveServo(9, 180)
                wait(0.2)
            elif event.button == descanzar_brazo:
                robot.moveServo(9, 90)
                wait(0.2)
        elif event.type == pygame.JOYAXISMOTION:
            if event.axis == vertical:
                if event.value < -0.5:
                    # Arriba
                    robot.forward(60)
                    moviendose_eje_vertical = True
                elif event.value > 0.5:
                    # Abajo
                    robot.backward(60)
                    moviendose_eje_vertical = True
            elif event.axis == horizontal:
                if event.value < -0.5:
                    # Izquierda
                    robot.turnLeft(60)
                    moviendose_eje_horizontal = True
                elif event.value > 0.5:
                    # Derecha
                    robot.turnRight(60)
                    moviendose_eje_horizontal = True
            if abs(event.value) <= 0.5:
                # Para detener el robot es necesario conocer el estado
                # actual.
                if event.axis == vertical and moviendose_eje_vertical:
                    robot.stop()
                    moviendose_eje_vertical = False
                if event.axis == horizontal and moviendose_eje_horizontal:
                    robot.stop()
                    moviendose_eje_horizontal = False

board.exit()
pygame.quit()
