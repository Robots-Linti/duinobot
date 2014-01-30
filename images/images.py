#!/usr/bin/env python
#-*- coding: utf-8 -*-
# (C) Fernando López <flopez [AT] linti.unlp.edu.ar>
import time
import Tkinter as tk
import cv2
import PIL
import PIL.Image
import ImageTk

from gui_events import _request_queue #, _tk_root, TK_AFTER_INTERVAL
import threading

DEF_COLOR = 'black'
DEF_BG_COLOR = 'blue'
DEF_THICKNESS = 1

class Drawing(object):
    """Ventana para hacer dibujos en Python o modificar fotos sacadas con la
    webcam.

    Podés dibujar circulos, rectángulos, líneas y puntos, lo primero que tenés
    que hacer es crear un nuevo Drawing:
        dibujo = Drawing()
        # Dibujamos un círculo de radio 5 en las coordenadas (100, 150)
        dibujo.circle(100, 150, 5)
        # Dibujamos un cuadrado de 10 x 10 en las coordenadas (20, 30)
        dibujo.rectangle(20, 30, 10, 10)
        # Dibujamos un triángulo
        dibujo.line(0, 0, 0, 50)
        dibujo.line(0, 50, 50, 50)
        dibujo.line(50, 50, 0, 0)

    Todos los métodos de Drawing permiten personalizar los dibujos con
    parámetros opcionales se puede definir el ancho del trazo (en píxels) con el
    parámetro thickness y el color de los contornos con el parámetro bg_color.

    Obviamente las líneas y los puntos no tienen color de fondo, solamente usan
    el color de contorno.

    Los dibujos se pueden guardar con save y después los podés abrir con el
    programa que quieras:
        dibujo.save('mi_dibujo.jpg')
        dibujo.save('/home/usuario/foto.jpg')
    """
    def __init__(self, width = 200, height = 200):
        self.width = width
        self.height = height
        self.window = tk.Toplevel()
        self.canvas = tk.Canvas(self.window, width = width, height = height)
        self.canvas.pack()

    def circle(self, x, y, r,
               thickness = DEF_THICKNESS,
               color = DEF_COLOR,
               bg_color = DEF_BG_COLOR):
        pass

    def rectangle(self, x, y, width, height,
                  thickness = DEF_THICKNESS,
                  color = DEF_COLOR,
                  bg_color = DEF_BG_COLOR):
        self.canvas.create_rectangle(x, y,
                                     x + width,
                                     y + height,
                                     fill = bg_color)

    def line(self, x0, y0, x1, y1,
             thickness = DEF_THICKNESS,
             color = DEF_COLOR):
        self.canvas.create_line(x0, y0, x1, y1, fill = color)

    def grid_with_coords(self, color = "grey"):
        "Dibuja una grilla con las coordenadas (x, y) de la ventana"
        self.line(1, 1, 1, self.height - 1, color = color)
        self.line(1, 1, self.width - 1, 1, color = color)
        self.canvas.create_text(1, 1, text = '0', anchor = tk.NW)
        for i in range(0, self.width, 10):
            self.line(i, 1, i, self.height - 1, color = color)
            self.line(1, i, self.width - 1, i, color = color)
            if (i > 0 and i % 40 == 0):
                self.canvas.create_text(i, 1, text = str(i), anchor = tk.N)
                self.canvas.create_text(1, i, text = str(i), anchor = tk.W)

if __name__ == "__main__":
    canvas = Drawing()
    canvas.rectangle(20, 30, 100, 150)
    canvas.grid_with_coords()
    tk.mainloop()
    time.sleep(5)
