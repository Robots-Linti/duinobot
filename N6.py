from pyfirmata import DuinoBot, util


class N6:

    def __init__(self, device='/dev/ttyUSB0'):
        '''Inicializa el dispositivo de conexion con el robot'''
        self.board = DuinoBot(device)
        it = util.Iterator(self.board)
        it.start()
        self.board.pass_time(0.1)
        
    def motor0(self,vel):
        if(vel >= 0 and vel <= 100):
            self.board.send_sysex(1,[vel])    

    def motor1(self,vel):
        if(vel >= 0 and vel <= 100):
            self.board.send_sysex(2,[vel])   
            
    def motors(self,vel1, vel2, tiempo=-1):
        if(abs(vel1)<=100 and abs(vel2)<=100):
            self.board.send_sysex(4,[abs(vel1), abs(vel2), 1 if vel1>0 else 0, 1 if vel2>0 else 0])   
            if tiempo!=-1:
                self.board.pass_time(tiempo)
                self.motors(0,0)

    def ping(self):
        '''Devuelve la distancia en centimetros al obstaculo mas cercano'''
        self.board.send_sysex(3,[])
        # wait 20ms (ping delay) + 20ms (comm)
        self.board.pass_time(0.04)
        return self.board.nearest_obstacle   

    def sleep(self,time):
        self.board.pass_time(time)

    def exit(self):
        self.board.exit()
        
    def analog(self,ch,samples=1): 
        self.board.send_sysex(6,[ch, samples])
        self.board.pass_time(0.03)
        return self.board.analog_value

    def digital(self,pin): 
        self.board.send_sysex(7,[pin])
        self.board.pass_time(0.02)
        return self.board.digital_value
        
    def tone(self, freq=0, duration=0):
        '''Frecuencia del tono y duracion en microsegundos.'''
        hi=freq>>7
        lo=freq%128
        if freq!=0:
            if duration==0:
                self.board.send_sysex(5,[hi, lo])
            else:
                self.board.send_sysex(5,[hi, lo, int(duration*1000)])
                #self.board.pass_time(duration)

        else:
            self.board.send_sysex(5,[])
    
    def forward (self, impulse=50, seconds=-1):
        '''El robot avanza con impulso impulse durante seconds segundos.'''
        self.motors(-(impulse), -(impulse), seconds)

    def backward (self, impulse=-50, seconds=-1):
        '''El robot retrocede con impulso impulse durante seconds segundos.'''
        self.forward(impulse,seconds)

    def getLine(self):
        '''Devuelve los valores de los sensores de Line.'''
        #FIXME: Falta parametrizar cuales son los sensores de LINE
        a = self.analog(18)
        b = self.analog(19)
        return (a,b)

    def getObstacle(self, distance=10):
        '''Devuelve True si hay un obstaculo a menos de distance centimetros del robot.'''
        if self.ping() < distance :
            return True
        else:
            return False

    def battery(self):
        self.board.send_sysex(6,[6, 1])
        self.board.pass_time(0.02)
        return self.board.analog_value*5.0/1024

    def sensors(self):
        '''Imprime informacion de los sensores.'''
        print 'Line1 = ' + str(self.analog(18))
        print 'Line2 = ' + str(self.analog(19))
        print 'Obstaculo mas cercano = ' + str(self.ping()) + ' cm.'
        print 'Pontenciometro = ' + str(self.analog(15))
        print 'Bateria = ' + str(self.battery()) + ' v.'

