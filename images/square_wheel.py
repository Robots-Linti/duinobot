#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import threading
import atexit
import time
import Queue as queue
import Tkinter as tk
import cv
import signal
import copy
import PIL
import PIL.Image
import ImageTk

_terminate_thread = threading.Event()

TK_AFTER_INTERVAL = 10

perror = sys.stderr.write
def _tk_loop():
	global _tk_root
	try:
		_tk_root = tk.Tk() # Ventana root
		_tk_root.withdraw() # Oculta
		_tk_root.after(TK_AFTER_INTERVAL, _tk_attend_requests)
		_tk_root.mainloop()
	except (Exception,) as e:
		print e
		_tk_root = None
		perror("Error inicializando los gráficos\n")
# Que se ejecute al salir:
#@atexit.register
def _tk_loop_cleanup():
	"Indica al thread que se detenga y lo espera"
	_terminate_thread.set()
	_tk_loop_thread.join(5)
	if _tk_loop_thread.is_alive():
		print "Timeout :("
# También para el Ctrl+C:
signal.signal(signal.SIGINT | signal.SIGTERM, lambda signal, frame: _tk_loop_cleanup)
#signal.signal(signal.SIGTERM, lambda signal, frame: _tk_loop_cleanup)

_tk_loop_thread = threading.Thread(target=_tk_loop)
#print _tk_loop_thread.daemon
_tk_loop_thread.daemon = True
_tk_loop_thread.start()

_request_queue = queue.Queue()

def _tk_attend_requests():
	"""Atiende requests desde adentro del thread,
	recibe métodos desde _request_queue"""
	if _terminate_thread == None or _terminate_thread.is_set():
		# Terminar el thread desde adentro
		_tk_root.quit()
		exit()
	try:
		request = _request_queue.get(block=False)
	except queue.Empty:
		pass
	else:
		_tk_root.after(0, request)
	finally:
		_tk_root.after(TK_AFTER_INTERVAL, _tk_attend_requests)

class Senses(object):
	def __init__(self, robot):
		_request_queue.put(self.run)
	def run(self):
		toplevel = tk.Toplevel()
		toplevel.grid()
		label = tk.Label(toplevel, text="Hola")
		label.pack()

def _ipl2pil(frame):
        return PIL.Image.fromstring(
                'RGB', 
                cv.GetSize(frame), 
                frame.tostring(), 
                'raw', 
                'BGR', 
                frame.width*3, 
                0   
        )


class WebCam(object):
	def __init__(self, index = 0):
		self.index = index
		self.capture = cv.CaptureFromCAM(self.index)
	def takePicture(self):
		return Picture(_ipl2pil(cv.QueryFrame(self.capture)))

showWindow = None

class Picture(object):
	def __init__(self, pilimage):
		self.image = pilimage
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
				showLabel.photoref =  ImageTk.PhotoImage(self.image)
				showLabel.configure(image = showLabel.photoref)
			else:
				showLabel.photoref.paste(self.image)
		_request_queue.put(doShow)
		# Para darle una chance de ejecutarse al otro thread
		# hay que hacer una operación bloqueante:
		time.sleep(.1)

#a = raw_input()
s = Senses(2)
w = WebCam()
for i in xrange(100):
	picture = w.takePicture()
	picture.show()
#b = raw_input()
#try:
#	while True:
#		time.sleep(1)
#except KeyboardInterrupt:
#	pass

time.sleep(5)
