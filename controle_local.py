import sys
import termios
import fcntl
import os
import libardrone
import time
import string
    
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
drone=libardrone.ARDrone()

drone.speed = 0.8
try:
	while 1:
		try:
			c = sys.stdin.read(1)
			c = c.lower()

			if c =='a' or c == 's' or c == 'd' or c == 'w' or c == 'q' or c =='e' or c == 'i' or c == 'j' or c == 'k' or c == 'l' or c == 'r' or c == 'x':
				print 'Tecla Pressionada', c
			else:
				print 'Comando Invalido!!'

			if c == 'a':
				drone.move_left()
			if c == 'd':
				drone.move_right()
			if c == 'w':
				drone.move_forward()
			if c == 's':
				drone.move_backward()
			if c == ' ':
				drone.land()
				drone.hover()
			if c == '\n':
				drone.takeoff()
				drone.hover()
			if c == 'q':
				drone.turn_left()
			if c == 'e':
				drone.turn_right()
			if c == 'i':
				drone.move_up()
			if c == 'j':
				drone.hover()
			if c == 'k':
				drone.move_down()
			if c == 'r':
				drone.reset()
			if c == 'l':
				drone.trim()
			if c == 'x':
				break
			print '\n'
		except IOError:
			pass
finally:
	termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
	fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
	drone.halt()
