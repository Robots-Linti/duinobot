#-*- encoding: utf-8 -*-
# Fernando López <flopez [AT] linti.unlp.edu.ar>

import cv
import Tkinter as tk
import ImageTk
import PIL
import PIL.Image

__window = 0

def __ipl2pil(frame):
	return PIL.Image.fromstring(
		'RGB', 
		cv.GetSize(frame), 
		frame.tostring(), 
		'raw', 
		'BGR', 
		frame.width*3, 
		0
	)

def takePicture(index = -1):
	capture = cv.CaptureFromCAM(index)
	frame = cv.QueryFrame(capture)
	return __ipl2pil(frame)

def show(image):
	#window = tk.Tk()
	#window.grid()
	window = root
	photo = ImageTk.PhotoImage(image)
	label = tk.Label(window, image=photo)
	label.grid()
	#tk.mainloop()


import threading
__rootLock = threading.Lock()
def __guiLoop():
	global root
	root = tk.Tk()
	root.grid()
	label = None
	__rootLock.release()
	while True:
		__rootLock.acquire()
		root.update()
		image = takePicture()
		photo = ImageTk.PhotoImage(image)
		if label:
			label.destroy()
		label = tk.Label(root, image=photo)
		label.grid()
		__rootLock.release()

__rootLock.acquire()
__guiThread = threading.Thread(target=__guiLoop)
__guiThread.start()
#while True:
#	__rootLock.acquire()
#	show(takePicture())
#	__rootLock.release()


