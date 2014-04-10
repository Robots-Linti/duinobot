[In english](README_en.md)

¿Qué es?
--------

Duinobot es un paquete Python para controlar robots simples, está pensado para
ser usado por alumnos de escuelas secundarias como parte de un curso en donde
aprender los conceptos básicos de programación.

¿Cómo se ve un programa que usa Duinobot?
-----------------------------------------

Simplemente es un programa Python común y corriente que utiliza el paquete
Duinobot para interactuar con los robots.

Por ejemplo podemos programar un robot para que avance hasta encontrar un
obstáculo
y que al encontrarlo gire y luego siga avanzando:

```python
from duinobot import *
# Inicialización
board = Board()
robot = Robot(board, 2)

# Avanzar a velocidad 50
robot.forward(50)
while True:
    # Si hay algo a menos de 30cm
    if robot.getObstacle(30):
        # Girar a velocidad 50 por 2 segundos
        robot.turnLeft(50, 2)
        # Seguir avanzando
        robot.forward(50)

# Terminación del programa
board.exit()
```

¿Con qué robots funciona?
-------------------------

Por el momento solamente funciona con los robots [Multiplo N6 de
RobotGroup](http://robotgroup.com.ar/index.php/productos/131-robot-n6), pero
podría funcionar con cualquier robot que tenga algún tipo de conexión serial
(por ejemplo a través de bluetooth) y en el cuál se pueda implementar el
protocolo [Firmata](http://firmata.org).

¿Puedo probarlo sin robots?
---------------------------

Estamos trabajando en un simulador basado en Pilas Engine. La primer beta ya es
utilizable y se puede descargar [empaquetada para
Debian](http://sl.linti.unlp.edu.ar/2014/03/esta-disponible-la-primer-version-del-simulador-del-multiplo-n6/) o [con git desde el
repositorio del proyecto en GitHub](https://github.com/apehua/pilas).

¿En qué sistemas operativos funciona?
-------------------------------------

Lo probamos y empaquetamos principalmente en la distribución [Lihuen
GNU/Linux](http://lihuen.linti.unlp.edu.ar)
que es completamente compatible con Debian estable.

En teoría debería funcionar en cualquier sistema GNU/Linux sin problemas y en
otros sistemas operativos puede no detectar automáticamente los
Joysticks y la placa controladora de los robots.

Conocemos casos en los que pudieron usar este paquete en Ubuntu sin
inconvenientes e incluso en Windows (el último con las limitaciones antes
mencionadas).

¿Cómo lo instalo?
-----------------

En el [manual de uso de Duinobot](http://robots.linti.unlp.edu.ar/material_disponible) que está en el [sitio oficial del proyecto](http://robots.linti.unlp.edu.ar) hay una guía de
instalación para el paquete en distribuciones basadas en Debian.

De forma alternativa se puede clonar la última versión de Duinobot con git:
```bash
git clone git@github.com:Robots-Linti/duinobot.git
git submodule init
git submodule update
```

Manual de uso y material didáctico
----------------------------------

El [manual de uso de Duinobot](http://robots.linti.unlp.edu.ar/material_d
isponible) fue redactado para ser leído directamente por los alumnos
destinatarios del proyecto pertenecientes a escuelas secundarias. Los mismos,
por lo general, no tienen conocimientos previos en programación. Por lo tanto,
en el manual, se introducen conceptos básicos como variables, funciones,
módulos, y estructuras de control de forma simple y con ejemplos.

También hay entre los materiales 4 clases teóricas y sus guías prácticas
correspondientes con licencias Creative Commons.

¿Cómo puedo contribuir?
-----------------------

Para contribuir nuevo código para el paquete es recomendable crear un fork
del mismo en GitHub, hacer los commits en el branch develop en el caso de
nuevas funcionalidades y finalmente hacer un Pull Request.

También se puede contribuir con material didáctico, fotos o videos de las
actividades realizadas, para esto ponerse en contacto con:
* robots[arroba]linti.unlp.edu.ar

Página oficial del proyecto
------------------------------------------

* http://robots.linti.unlp.edu.ar


