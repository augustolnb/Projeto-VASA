import libardrone
import cv2
import numpy as np
import sys,os

drone = libardrone.ARDrone()


#Conectando com a camera
cv2.namedWindow("Camera Principal",cv2.CV_WINDOW_AUTOSIZE)
ip = "tcp://192.168.1.1:5555" 
cap = cv2.VideoCapture(ip)
#Para Mostrar a bateria precisa abrir uma conexao opencv com a camera
os.system("clear")


a = drone.navdata.get(0, dict()).get('battery', 0)
print "Bateria: %",a
