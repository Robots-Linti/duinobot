from pyfirmata import DuinoBot, util
from N6 import N6

import sys

placa=N6();

while 1:
    for i in range(6):
        print placa.analog(i),
        print '\t',
    print '\n',
    if placa.ping() < 50:
        break


placa.exit()
