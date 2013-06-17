#!/usr/bin/env python
#-*- coding: utf-8 -*-
# (C) Fernando López <flopez [AT] linti.unlp.edu.ar>
import time
import Tkinter as tk
import cv2
import PIL
import PIL.Image
import ImageTk

from gui_events import _request_queue

class Webcam(object):
	discard_frames = 30
	def __init__(self, index = 0):
		self.index = index
	#	self.capture = cv2.VideoCapture(self.index)
	#def takePicture(self):
	#	for i in xrange(5):
	#		# 5 intentos para una captura exitosa
	#		ret, im = self.capture.read()
	#		if ret:
	#			break
	#	return Picture(im)
	def takePicture(self):
		self.capture = cv2.VideoCapture(self.index)
		for i in xrange(Webcam.discard_frames):
			# Descarta 30 frames para que la camara se ajuste a la luminosidad
			ret, im = self.capture.read()
		self.capture.release()
		return Picture(im) if ret else None

showWindow = None

class Picture(object):
	def __init__(self, numpy_array):
		self.image = numpy_array
		self.pil_image = None # Solo actualizado en self.show()
	def show(self):
		def doShow():
			global showWindow, showLabel
			if not showWindow:
				showWindow = tk.Toplevel()
				showWindow.grid()
				showLabel = tk.Label(showWindow)
        			showLabel.pack()
				showLabel.photoref = None
			# Variable de instancia para evitar al Garbage Collector (es un bug de ImageTk)
			if not showLabel.photoref:
				showLabel.photoref =  ImageTk.PhotoImage(self.pil_image)
				showLabel.configure(image = showLabel.photoref)
			else:
				showLabel.photoref.paste(self.pil_image)
		self.pil_image = PIL.Image.fromarray(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
		_request_queue.put(doShow)
		# Para darle una chance de ejecutarse al otro thread
		# hay que hacer una operación bloqueante:
		time.sleep(.1)

class Senses(object):
	def __init__(self, robot):
		def senses():
			if not self.window:
				self.window = tk.Toplevel()
				self.window.title("Senses robot {1}".format(self.robot))
				self.window.grid()
				label = tk.Label(self.window, text = "Ping:")
				label.grid(row = 0, sticky = tk.W)
				self.ping = tk.Entry(self.frame)
				self.ping.grid(row = 0, column = 1)
				label = tk.Label(self.window, text = "Wheels:")
				label.grid(row = 1, columnspan = 2)
				_request_queue
			self.ping["textvariable"] = self.robot.ping()
		self.window = None	
		self.robot = robot

if __name__ == "__main__":
	w = Webcam()
	for i in xrange(100):
		picture = w.takePicture()
		picture.show()
	time.sleep(5)
