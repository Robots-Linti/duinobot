from pyfirmata import *
from boards import BOARDS

__version__ = '0.9.2'

# shortcut classes

class Arduino(Board):
    """
    A board that wil set itself up as a normal Arduino.
    """
    def __init__(self, *args, **kwargs):
        args = list(args)
        args.append(BOARDS['arduino'])
        super(Arduino, self).__init__(*args, **kwargs)
        
    def __str__(self):
        return 'Arduino %s on %s' % (self.name, self.sp.port)
    
class ArduinoMega(Board):
    """
    A board that wil set itself up as an Arduino Mega.
    """
    def __init__(self, *args, **kwargs):
        args = list(args)
        args.append(BOARDS['arduino_mega'])
        super(ArduinoMega, self).__init__(*args, **kwargs)
    
    def __str__(self):
        return 'Arduino Mega %s on %s' % (self.name, self.sp.port)
        
class DuinoBot(Board):
    """
    A board that wil set itself up as an DuinoBot.
    """
    def __init__(self, *args, **kwargs):
        args = list(args)
        args.append(BOARDS['duinobot'])
        super(DuinoBot, self).__init__(*args, **kwargs)
    
    def __str__(self):
        return 'DuinoBot %s on %s' % (self.name, self.sp.port)
        