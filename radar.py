from pyfirmata import DuinoBot, util
from N6 import N6

import sys

placa=N6(); 

placa.motors(-15,15)

for i in range(1000):
    print placa.ping()

placa.motors(0,0)

placa.exit()






    
