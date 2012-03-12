from pyfirmata import DuinoBot, util
from N6 import N6

import sys

placa=N6();



placa.report()

#placa.set_id(11,10)

 
#placa.report()


placa.tone(2000,0.1,11)

placa.tone(2000,0.1,10)


#placa.motors(100,100,1,11)

#placa.motors(100,100,1,10)


print placa.batt_in_v(13)

placa.exit()
