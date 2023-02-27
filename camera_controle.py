#!/usr/bin/python
import cv2
import numpy
import sys
import termios
import fcntl
import os
import libardrone

drone=libardrone.ARDrone()
cv2.namedWindow("Pilotando o Drone", cv2.CV_WINDOW_AUTOSIZE)
cap = cv2.VideoCapture("http://192.168.1.1:5555/video?x.mjpeg")

while(True):
	ret, frame = cap.read()
	cv2.imshow('Pilotando o Drone',frame)

	if cv2.waitKey(30) == 119:
		drone.move_forward()

	if cv2.waitKey(30) == 115:
		drone.move_backward()

	if cv2.waitKey(30) == 97:
		drone.move_left()

	if cv2.waitKey(30) == 100:
		drone.move_right()

	if cv2.waitKey(30) == 113:
		drone.turn_left()

	if cv2.waitKey(30) == 101:
		drone.turn_right()

	if cv2.waitKey(30) == 105:
		drone.move_up()

	if cv2.waitKey(30) == 107:
		drone.move_down()

	if cv2.waitKey(30) == 104:
		drone.hover()

	if cv2.waitKey(30) == 116:
		drone.takeoff()

	if cv2.waitKey(30) == 108:
		drone.land()

	if cv2.waitKey(30) == 120:
		break
cap.release()
cv2.destroyAllWindows()
