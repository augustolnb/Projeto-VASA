#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Grupo de Pesquisa Gredes

import numpy as np
import cv2
import sys,os
import libardrone
from time import sleep

#Declaração da Função que desenha a trajetoria do ARDrone
def quadrado():
	print"\n\n	Rota do VOO \n\n"
	print" _________________________"
	print"|         <---------      |"
	print"| |			^ |"
	print"| |		  	| |"
	print"| |		  	| |"
	print"| |			| |"
	print"| |			| |"
	print"| v		        | |"
	print"|			  |"
	print"|	  --------->  	  |"
	print"|          O O		  |"
	print"|___________|_____________|"
	print"           O O"

drone = libardrone.ARDrone() #variavel que recebe a biblioteca ARDrone	
drone.speed = 0.1 #Velocidade do Drone

#Conectando com a camera
cv2.namedWindow("Camera Principal",cv2.CV_WINDOW_AUTOSIZE)
ip = "tcp://192.168.1.1:5555" #ip para a porta de video do ARDrone
cap = cv2.VideoCapture(ip)#Conectando com a camera principal do ARDrone
#Para Mostrar a bateria precisa abrir uma conexao opencv com a camera
os.system("clear")#Limpar a Tela
a = drone.navdata.get(0, dict()).get('battery', 0) #Variavel que recebe status da bateria
print "Bateria: %",a #Impressão do status da bateria

if a>20:
	drone.takeoff() #Drone Decola
	sleep(2)	#Espera 2 segundos
	drone.hover()	#Drone Estabilisa
	sleep(2)	#Espera 2 segundos
	drone.move_up() #Drone Sobe
	sleep(4)	#Espera 4 segundos
	drone.hover()#Drone Estabilisa
	sleep(2) #Espera 2 segundos

while a>20:   
	a = drone.navdata.get(0, dict()).get('battery', 0)#Variavel que recebe status da bateria
	os.system("clear") #Limpar a Tela
	print "Bateria: %",a #Impressão do status da bateria
	quadrado() #Chama a função quadrado

	drone.move_right()#Move para Direita
	sleep(2) #Espera 2 segundo
	drone.hover() #Drone Estabilisa
	sleep(2) #Espera 2 segundos

	drone.move_forward() #Drone Move para Frente
	sleep(4)	#Espera 4 Segundos
	drone.hover() #Drone Estabilisa
	sleep(2)	#Espera 2 segundos

	drone.move_left()	#Drone Move para Esquerda
	sleep(4)	#Espera 4 segundos
	drone.hover()	#Drone Estabilisa
	sleep(2)	#Drone Espera 2 segundos

	drone.move_backward() #Drone move para atras
	sleep(4)	#Drone Espera 4 segundos
	drone.hover()	#Drone Estabilisa
	sleep(2) #Drone Espera 2 segundos

	drone.move_right()	#Drone move para Direita
	sleep(2)	#Drone Espera 2 segundos
	drone.hover()	#Drone Estabilisa
	sleep(2)	#Drone Espera 2 segundos

drone.land()	#Drone Pousa
drone.halt()	#Drone Desliga as conexões

