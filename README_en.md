[En español](README.md)

What is it?
-----------

Duinobot is a Python package which allows to control simple robots, it is
intended to be used by students of secondary schools as part of a course where
they learn the basic skills in computer programming.

How does look a program using Duinobot?
---------------------------------------

It is simply a Python program which uses the Duinobot package to interact with
the robots.

For example we can program a robot to go forward until it finds an obstacle
and then turn to the left and go forward again:

```python
from duinobot import *
# Initialization
board = Board()
robot = Robot(board, 2)

# Go forward at speed 50
robot.forward(50)
while True:
    # If there is something less than 30cm away
    if robot.getObstacle(30):
        # Turn left 2 seconds at speed 50
        robot.turnLeft(50, 2)
        # Go forward again
        robot.forward(50)

# Program end
board.exit()
```

With which robots it works?
---------------------------

In this moment it only works with the robots [Multiplo N6 from
RobotGroup](http://robotgroup.com.ar/index.php/productos/131-robot-n6), but
it could work with any robot that uses some kind of serial conection (for
example through bluetooth) and in which the protocol
[Firmata](http://firmata.org) can be implemented.

How can I test it without robots?
---------------------------------

We are working in a simulator based on Pilas Engine. The first beta version is
already usable and can be downloaded [packaged for Debian](http://sl.linti.unlp.edu.ar/2014/03/esta-disponible-la-primer-version-del-simulador-del-multiplo-n6/)
or [with git from the repository of the project on GitHub](https://github.com/apehua/pilas).

In which operating systems it works?
------------------------------------

We tested it and it's packaged on [Lihuen GNU/Linux](http://lihuen.linti.unlp.edu.ar)
(this distribution is fully compatible with Debian stable).

In theory it should work on any GNU/Linux system without any problem and in
other operating systems it may not detect automatically Joysticks and the
controller board of the robots.

We know of cases in which this package was used in Ubuntu without any problem
and even in Windows (in the later with the limitations mentioned before).

How to install it?
----------------------

In the [Duinobot's user manual (in spanish)](http://robots.linti.unlp.edu.ar/material_disponible)
which is available on the
[official site of the project (in spanish)](http://robots.linti.unlp.edu.ar)
there is a guide of installation for the package on distributions based on
Debian.

Alternatively you can clone the last version of Duinobot with git:
```bash
git clone git@github.com:Robots-Linti/duinobot.git
git submodule init
git submodule update
```

User manual and didactic materials
----------------------------------

The [Duinobot's user manual](http://robots.linti.unlp.edu.ar/material_disponible)
was written to be read directly by the secondary school students targeted by the
project. In general those students didn't have any previous knowledge in
computer programming. Therefore in the manual basic concepts as variables,
functions, modules, and control structures are introduced in a simple way with
several examples.

Also in the materials there are slides for 4 lectures and exercises for each
one of the lectures. All this materials are available with a Creative Commons
license.

Contributions
-------------

To contribute new code for the package you can create a fork of Duinobot in
GitHub, make the commits in the develop branch in case the code adds new
functionality and finaly make a Pull Request.

Also didactic material, pictures and videos of the activities can be
contributed, just get in contact with us by e-mail:
* robots[arroba]linti.unlp.edu.ar

Official page of the project
----------------------------

* http://robots.linti.unlp.edu.ar


