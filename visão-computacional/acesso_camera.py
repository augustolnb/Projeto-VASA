#!/usr/bin/python
import cv2
import numpy
import sys
import termios
import fcntl
import os
import libardrone

drone = libardrone.ARDrone()
cv2.namedWindow("Capturando video", cv2.CV_WINDOW_AUTOSIZE)

cap = cv2.VideoCapture("udp://192.168.1.1:5555/video?x.avi")

while True:
	ret, frame = cap.read()

	cv2.imshow("Capturando video", frame)

	if cv2.waitKey(30) == 120:
		break
cap.release()
cv2.destroyAllWindow()
