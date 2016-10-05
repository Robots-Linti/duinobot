#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from distutils.core import setup
import os.path
import glob

setup(name='duinobot-socks',
      version='0.15',
      description='API en Python para el robot Multiplo N6',
      author='Fernando Lopez, Sofia Martin, Augusto Guerrero, Joaquin Bogado',
      author_email='soportelihuen@linti.unlp.edu.ar',
      url='http://lihuen.linti.unlp.edu.ar',
      packages=['duinobot', 'duinobot.pyfirmata'],
      package_dir={'duinobot': '.'},
      data_files=[('usr/share/doc/duinobot/ejemplos',
                   glob.glob(os.path.join('ejemplos', '*.py')))],
      requires=['pygame'],
      classifiers=[
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Education",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7"
      ])
