#!/usr/bin/python
# -*- encoding: utf-8 -*-
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


class SensesModel():
    def __init__(self):
        self.wheelLeft = tk.StringVar()
        self.wheelRight = tk.StringVar()
        self.ping = tk.StringVar()
        self.battery = tk.StringVar()


class SensesGUI():
    def __init__(self, root, model):
        self.root = root
        root.title("Senses")
        self.frame = tk.Frame(root)
        self.frame.pack(expand=1, padx=5, pady=5)
        # self.frame["padding"] = 5
        label = tk.Label(self.frame)
        label["text"] = "Ping:"
        label.grid(row=0, sticky=tk.W)
        self.ping = tk.Entry(self.frame)
        self.ping.grid(row=0, column=1)
        label = tk.Label(self.frame)
        label["text"] = "Sensores de las ruedas:"
        label.grid(row=1, columnspan=2)
        self.wheelLeft = tk.Entry(self.frame)
        self.wheelLeft.grid(row=2, column=0)
        self.wheelRight = tk.Entry(self.frame)
        self.wheelRight.grid(row=2, column=1)
        label = tk.Label(self.frame)
        label["text"] = "Medidor de batería: "
        label.grid(row=3, sticky=tk.W)
        self.battery = tk.Entry(self.frame)
        self.battery.grid(row=3, column=1)
        self.model = model
        self._setEntries()

    def _setEntries(self):
        self.wheelLeft["textvariable"] = self.model.wheelLeft
        self.wheelRight["textvariable"] = self.model.wheelRight
        self.ping["textvariable"] = self.model.ping
        self.battery["textvariable"] = self.model.battery


def _updateModel(model, messages, root):
    values = messages.get()
    if not values:
        return
    wleft, wright = values["wheels"]
    model.ping.set(str(values["ping"]))
    model.wheelLeft.set(str(wleft))
    model.wheelRight.set(str(wright))
    model.battery.set(str(values["battery"]))
    root.after(1000, _updateModel, model, messages, root)


def _sensesDialog(messages):
    global tk
    import Tkinter  # Tkinter must be imported in the process that uses it
    tk = Tkinter
    root = tk.Tk()
    model = SensesModel()
    gui = SensesGUI(root, model)
    root.after_idle(_updateModel, model, messages, root)
    root.mainloop()
    root.quit()


def _sendSensorsValues(robot):
    messages = multiprocessing.Queue()
    senses = multiprocessing.Process(target=_sensesDialog,
                                     args=(messages,))
    senses.daemon = True
    senses.start()
    while senses.is_alive():
        values = {
            "wheels": robot.getWheels(),
            "ping": robot.ping(),
            "battery": robot.battery()
        }
        # values = {
        #     "line": (1,1),
        #     "ping": int(time.time() % 100),
        #     "battery": int(time.time() % 100)
        # }
        messages.put(values)
        time.sleep(1)
    senses.join()

import platform
mayor, minor, revision = platform.python_version_tuple()
if mayor != '2' or minor < '6':
    print("El módulo senses precisa una versión de Python mayor" +
          "o igual a 2.6 y menor a 3")

    def senses(robot):
        print("Función no disponible en esta versión de Python")
else:
    import threading
    import multiprocessing
    import time

    def senses(robot):
        update = threading.Thread(target=_sendSensorsValues, args=(robot,))
        update.setDaemon(True)
        update.start()

if __name__ == "__main__":
    from duinobot import *
    b = Board("/dev/ttyUSB0")
    r = Robot(b, 1)
    senses(r)
