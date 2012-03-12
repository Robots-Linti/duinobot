#!/usr/bin/python
#-*- encoding: utf-8 -*-
###############################################################################
# Copyright (C) 2012 Fernando López <flopez AT linti.unlp.edu.ar>
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

import threading
import multiprocessing
import time
class SensesModel():
    def __init__(self):
        self.lineLeft = tk.StringVar()
        self.lineRight = tk.StringVar()
        self.ping = tk.StringVar()
        self.battery = tk.StringVar()

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
        label = tk.Label(self.frame)
        label["text"] = "Medidor de batería: "
        label.grid(row = 3, sticky = tk.W)
        self.battery = tk.Entry(self.frame)
        self.battery.grid(row = 3, column = 1)
        self.model = model
        self._setEntries()
        
    def _setEntries(self):
        self.lineLeft["textvariable"] = self.model.lineLeft
        self.lineRight["textvariable"] = self.model.lineRight
        self.ping["textvariable"] = self.model.ping
        self.battery["textvariable"] = self.model.battery

def _updateModel(model, messages, root):
    values = messages.get()
    if not values:
        return
    left, right = values["line"]
    model.ping.set(str(values["ping"]))
    model.lineLeft.set(str(left))
    model.lineRight.set(str(right))
    model.battery.set(str(values["battery"]))
    root.after(1000, _updateModel, model, messages, root)

def _sensesDialog(messages):
    global tk
    import Tkinter # Tkinter must be imported in the process that uses it
    tk = Tkinter
    root = tk.Tk()
    model = SensesModel()
    gui = SensesGUI(root, model)
    root.after_idle(_updateModel, model, messages, root)
    root.mainloop()
    root.quit()

def _sendSensorsValues(robot):
    messages = multiprocessing.Queue()
    senses = multiprocessing.Process(target = _sensesDialog, args = (messages,))
    senses.start()
    while senses.is_alive():
        values = {
            "line": robot.getLine(),
            "ping": robot.ping(),
            "battery": robot.battery()
        }
        #values = {
        #    "line": (1,1),
        #    "ping": int(time.time() % 100),
        #    "battery": int(time.time() % 100) 
        #}
        messages.put(values)
        time.sleep(1)
    senses.join()

def senses(robot):
    update = threading.Thread(target = _sendSensorsValues, args = (robot,))
    update.start()    

if __name__ == "__main__":
    from robot import *
    b = Board("/dev/ttyUSB0")
    r = Robot(b, 1)
    #r = None
    senses(r)
