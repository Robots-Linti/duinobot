# http://www.stealth-x.com/programming/driver-writing-with-python.php
import sys

_vel = 50
_tiempo = .3
def pad_up():
	print "Up"
	r.forward(_vel, _tiempo)
def pad_down():
	r.backward(_vel, _tiempo)
	print "Down"
def pad_left():
	print "Left"
	r.turnLeft(_vel, _tiempo)
def pad_right():
	print "Right"
	r.turnRight(_vel, _tiempo)

jmap = {
	0x800204: pad_up,
	0x7f0204: pad_down,
	0x800203: pad_left,
	0x7f0203: pad_right,
}

def key(cmd):
	return cmd[5] * 65536 + cmd[6] * 256 + cmd[7]


joy = open("/dev/input/js1", "r")

################
from robot import *
#try:
#	b = Board("/dev/ttyUSB1")
#except:
b = Board("/dev/ttyUSB0")
b.report()
r = Robot(b, 1)
################

byte = joy.read(1)
count = 0
cmd = []
def salir():
	b.exit()
	exit()
jmap[0x000109] = salir
while byte:
	if count == 8:
		try:
			jmap[key(cmd)]()
		except KeyError:
			pass
		#sys.stdout.write("0x")
		#for b in cmd:
		#	sys.stdout.write("{0:02x} ".format(b))
		#sys.stdout.write("\n")
		count = 0
		cmd = []
	
	cmd.append(ord(byte))
	count += 1
	byte = joy.read(1)

joy.close()

b.exit()
