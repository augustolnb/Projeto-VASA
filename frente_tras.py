#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Grupo de Pesquisa Gredes

import numpy as np
import cv2
import sys,os
import libardrone
from time import sleep

drone = libardrone.ARDrone() #variavel que recebe a biblioteca ARDrone	
drone.speed = 0.2 #Velocidade do Drone

#Conectando com a camera
cv2.namedWindow("Camera Principal",cv2.CV_WINDOW_AUTOSIZE)
ip = "tcp://192.168.1.1:5555" #ip para a porta de video do ARDrone
cap = cv2.VideoCapture(ip)#Conectando com a camera principal do ARDrone
#Para Mostrar a bateria precisa abrir uma conexao opencv com a camera
os.system("clear")#Limpar a Tela
a = drone.navdata.get(0, dict()).get('battery', 0) #Variavel que recebe status da bateria
print "Bateria: %",a #Impressão do status da bateria


if a>13:
	drone.takeoff() #Drone Decola
	sleep(2)	#Espera 2 segundos
	drone.hover()	#Drone Estabilisa
	sleep(2)	#Espera 2 segundos
	
	drone.move_up() #Drone Sobe
	sleep(2)	#Espera 4 segundos
	drone.hover()#Drone Estabilisa
	sleep(2) #Espera 2 segundos


while a>13:   
	a = drone.navdata.get(0, dict()).get('battery', 0)#Variavel que recebe status da bateria
	os.system("clear") #Limpar a Tela
	print "Bateria: %",a #Impressão do status da bateria

	drone.move_forward() #Drone Move para Frente
	sleep(4)	#Espera 4 Segundos
	drone.hover() #Drone Estabilisa
	sleep(1)	#Espera 2 segundos
	
	drone.move_left()
	sleep(1)
	drone.hover()
	sleep(1)
	
	drone.move_backward() #Drone move para atras
	sleep(4)	#Drone Espera 4 segundos
	drone.hover()	#Drone Estabilisa
	sleep(2) #Drone Espera 2 segundos


drone.land()	#Drone Pousa
drone.halt()	#Drone Desliga as conexões
