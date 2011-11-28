from pyfirmata import DuinoBot, util
from N6 import N6

import sys

placa=N6();

# canales analogicos: 0, 1, 2, 3, 4, 5
for i in range(6):
    print "Analog",
    print i,
    print ": ",
    print placa.analog(i)

# canales digitales
for i in [2, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
    print "Digital",
    print i,
    print ": ",
    print placa.digital(i)


# prende los dos motores en potencia 20 por 1 segundo
placa.motors(20,20,1)

# prende un motor para cada lado a maxima potencia, por tiempo indefinido
placa.motors(-100,100)

# delay
placa.sleep(1)

# apago motores
placa.motors(0,0)

# reproduce un tono de 1khz por 200ms
placa.tone(1000,0.1)

# reproduce un tono de 2khz por tiempo indefinido
placa.tone(2000)

# delay
placa.sleep(0.2)

placa.tone(500)

# delay
placa.sleep(0.3)

# detiene el tono
placa.tone()

# mido distancia con sensor Ping)))
print "Nearest object [cm]: ",
print placa.ping()

placa.exit()
