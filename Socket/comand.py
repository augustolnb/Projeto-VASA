import os, sys
import libardrone
import time

comand = sys.argv[1]

drone = libardrone.ARDrone()
drone.speed = 0.5

if comand == 'z':
	drone.takeoff()
	drone.hover()

if comand == 'x':
	drone.land()

if comand == 'w':
	drone.move_forward()
	time.sleep(1)
	drone.hover()

if comand == 's':
	drone.move_backward()
	time.sleep(1)
        drone.hover()

if comand == 'a':
	drone.move_left()
	time.sleep(1)
        drone.hover()

if comand == 'd':
	drone.move_right()
	time.sleep(1)
        drone.hover()

if comand == 'q':
	drone.turn_left()
	time.sleep(1)
	drone.hover()

if comand == 'e':
	drone.turn_right()
	time.sleep(1)
	drone.hover()

if comand == 'i':
	drone.move_up()
	time.sleep(1)
	drone.hover()

if comand == 'k':
	drone.move_down()
	time.sleep(1)
	drone.hover()

time.sleep(1)

drone.halt()
