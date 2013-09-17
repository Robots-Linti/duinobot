#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from distutils.core import setup
import os.path
import glob

setup(name='duinobot',
      version='0.11-2',
      description='API en Python para el robot Multiplo N6',
      author='Joaquin Bogado, Fernando Lopez',
      author_email='soportelihuen@linti.unlp.edu.ar',
      url='http://lihuen.linti.unlp.edu.ar',
      packages=['duinobot', 'duinobot.pyfirmata'],
      package_dir={'duinobot': '.'},
      data_files=[('usr/share/doc/duinobot/ejemplos', glob.glob(os.path.join('ejemplos','*')))],
      requires=['pyserial', 'pygame']
     )
