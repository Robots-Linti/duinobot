#!/usr/bin/python
#-*- encoding: utf-8 -*-

import Tkinter as tk
import threading
import time
class SensesModel():
    def __init__(self):
        self.lineLeft = tk.StringVar()
        self.lineRight = tk.StringVar()
        self.ping = tk.StringVar()

class SensesGUI():
    def __init__(self, root, model):
        self.root = root
        root.title("Senses")
        self.frame = tk.Frame(root)
        self.frame.pack(expand = 1, padx = 5, pady = 5)
        #self.frame["padding"] = 5
        label = tk.Label(self.frame)
        label["text"] = "Ping:"
        label.grid(row = 0, sticky = tk.W)
        self.ping = tk.Entry(self.frame)
        self.ping.grid(row = 0, column = 1)
        label = tk.Label(self.frame)
        label["text"] = "Sensores de línea:"
        label.grid(row = 1, columnspan = 2)
        self.lineLeft = tk.Entry(self.frame)
        self.lineLeft.grid(row = 2, column = 0)
        self.lineRight = tk.Entry(self.frame)
        self.lineRight.grid(row = 2, column = 1)
        self.model = model
        self._setEntries()
        
    def _setEntries(self):
        self.lineLeft["textvariable"] = self.model.lineLeft
        self.lineRight["textvariable"] = self.model.lineRight
        self.ping["textvariable"] = self.model.ping


def _updateModel(model, robot, event):
    while not event.isSet():
        left, right = robot.getLine()
        model.ping.set(str(robot.ping()))
        model.lineLeft.set(str(left))
        model.lineRight.set(str(right))
        time.sleep(1)

_root = None

def _senses(robot):
    global _root
    _root = tk.Tk()
    model = SensesModel()
    gui = SensesGUI(_root, model)
    event = threading.Event()
    update = threading.Thread(target = _updateModel, args = (model, robot, event))
    update.start()    
    tk.mainloop()
    # When the window is closed set event, to make the update thread to finish
    event.set()
    # Wait update finishes
    update.join()
    _root.quit()
    _root = None

def senses(robot):
    global _robot
    if _root:
        return
    senses = threading.Thread(target = _senses, args = (robot,))
    senses.start()

if __name__ == "__main__":
    from robot import *
    b = Board("/dev/ttyUSB0")
    r = Robot(b, 1)
    senses(r)
