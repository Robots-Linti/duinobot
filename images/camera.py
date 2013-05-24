#-*- encoding: utf-8 -*-
# Fernando López <flopez [AT] linti.unlp.edu.ar>

import cv
import Tkinter as tk
import ImageTk

__window = 0

def takePicture(index = -1):
	capture = cv.CaptureFromCAM(index)
	frame = cv.QueryFrame(capture)
	#cv.ReleaseCapture()
	return frame

def showCV(image):
	global __window
	__window += 1
	id = "Ventana " + str(__window)
	cv.NamedWindow(id)
	print image
	#print "Viene el show"
	cv.ShowImage(id, cv.GetImage(image))
	cv.WaitKey(-1)

def show(image):
	window = tk.Tk()
	window.grid()
	#frame = tk.Frame()
	#frame.master.title("Imagen")
	#frame.grid()
	photo = ImageTk.PhotoImage(image)
	p = photo
	label = tk.Label(image=photo)
	label.grid()
	tk.mainloop()
	#frame.mainloop()

if __name__ == "__main__":
	show(takePicture())
