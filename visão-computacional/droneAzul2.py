#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2, math
import sys,os
import libardrone
from time import sleep

drone = libardrone.ARDrone()
drone.speed = 0.1 

drone.takeoff() #Drone Decola
sleep(2)	#Espera 2 segundos
drone.hover()	#Drone Estabilisa
sleep(2)	#Espera 2 segundos

drone.move_up() #Drone Sobe
sleep(2)	#Espera 4 segundos
drone.hover()#Drone Estabilisa
sleep(2) #Espera 2 segundos
	
class IdentificarObjeto:
	def __init__(self):
		cv2.namedWindow("DeteccaoDeObjetos", cv2.CV_WINDOW_AUTOSIZE)
		#self.cap = cv2.VideoCapture(0)
		self.cap =	cv2.VideoCapture("tcp://192.168.1.1:5555/,0,1")
		self.scale_down = 4
		
	
	def run(self):
		while(True):
			f, frameOrig = self.cap.read()
			
			frameOrig = cv2.flip(frameOrig,1)
			frameNew = cv2.GaussianBlur(frameOrig,(5,5),0)
			frameNew = cv2.cvtColor(frameOrig, cv2.COLOR_BGR2HSV)
			
			frameNew = cv2.resize(frameNew, (len(frameOrig[0]) / self.scale_down, len(frameOrig) / self.scale_down))
			color_lower = np.array([100,150,0],np.uint8)
			color_upper = np.array([130,255,255], np.uint8)
			
			color_binary = cv2.inRange(frameNew, color_lower, color_upper)
			dilation = np.ones((15,15), 'uint8')
			color_binary = cv2.dilate(color_binary, dilation)
			contours, hierarchy = cv2.findContours(color_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)		
			max_area = 0
			largest_contour = None
			points = []
			
			for idx, contour in enumerate(contours):
				area = cv2.contourArea(contour)
				if area > max_area:
					max_area = area
					largest_contour = contour		
			
			if not largest_contour == None:
				moment = cv2.moments(largest_contour)
				if moment["m00"] > 1000 / self.scale_down:
					rect = cv2.minAreaRect(largest_contour)
					pt1 = (rect[0][0] * self.scale_down, rect[0][1] * self.scale_down)
					pt2 = (rect[1][0] * self.scale_down, rect[1][1] * self.scale_down)
					rect = (pt1, pt2 , rect[2])
					points.append(pt1)
					points.append(pt2)
					box = cv2.cv.BoxPoints(rect)
					box = np.int0(box)
					posx=cv2.cv.Round((pt1[0]+pt2[0])/2)
					posy=cv2.cv.Round((pt1[1]+pt2[1])/2)
					posicao = "Coordenadas: {0}x | {1}y".format(posx, posy)
					
					if posx > 0 and posy > 0 and posx < 160 and posy < 260:
						cv2.putText(frameOrig,"Esquerda", (5,110),cv2.FONT_HERSHEY_SIMPLEX, 1, 0)	
						drone.move_left()	#Drone Move para Esquerda
						sleep(1)	#Espera 4 segundos
						drone.hover()	#Drone Estabilisa
						sleep(1)	#Drone Espera 2 segundos
						
					elif posx > 240 and posy > 0 and posx < 340 and posy < 260:
						cv2.putText(frameOrig,"Direita", (5,110),cv2.FONT_HERSHEY_SIMPLEX, 1, 0)	
						drone.move_right()#Move para Direita
						sleep(1) #Espera 2 segundo
						drone.hover() #Drone Estabilisa
						sleep(1) #Espera 2 segundos
					
					else:
						drone.hover() #Drone Estabilisa
						sleep(1)
					
			cv2.rectangle(frameOrig, (0, 0), (250, 640), (0, 255, 255), 3)	
			cv2.rectangle(frameOrig, (410, 0), (638, 480), (0,0, 255), 3)		
			cv2.imshow("DeteccaoDeObjetos", frameOrig)
			
			
			if cv2.waitKey(20) == 27:
				cv2.destroyWindow("DeteccaoDeObjetos")
				self.cap.release()
				break
						

if __name__ == "__main__":
	identificaObjeto = IdentificarObjeto()
	identificaObjeto.run()
