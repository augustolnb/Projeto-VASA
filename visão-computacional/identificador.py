# -*- coding: utf-8 -*-
import cv2
import numpy as np
import random
import time

# Cria a janela
cv2.namedWindow("drawing", cv2.CV_WINDOW_AUTOSIZE)
 
while True:
	# Desenha o fundo preto
	drawing = np.zeros([400, 640]) 
	# Desenha a área delimitada
	cv2.rectangle(drawing, (0, 0), (320, 200), (255, 255, 255), 0) 
	# Gera um numero aleatorio entre 0 e 620 para o eixo x
	x = random.sample(xrange(621), 1) 
	# Gera um numero aleatorio entra 0 e 380 para o eixo y
	y = random.sample(xrange(381), 1) 
	
	# Converte de lista para inteiro
	x = int(''.join(map(str, x))) 
	y = int(''.join(map(str, y))) 
	
	font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(drawing,"Quadrante 2", (30,15), font, 0.5,(255,255,255))


	#Desenha uma linha
	cv2.line(drawing,(320,0),(320,400),(255,0,0),1)
	cv2.line(drawing,(0,200),(640,200),(255,0,0),1)
	
	
	# Verifica em que lado da tela esta o ponto
	if x > 320:
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(drawing,"Movimento no lado direito", (360,360), font, 0.5,(255,255,255))
	else:
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(drawing,"Movimento no lado esquerdo", (360,360), font, 0.5,(255,255,255))
	
	# Verifica em que hemisfério esta o ponto
	if y > 200:
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(drawing,"Movimento na parte inferior", (80,360), font, 0.5,(255,255,255))
	
	else:
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(drawing,"Movimento na parte superior", (80,360), font, 0.5,(255,255,255))
	
	# Verifica se o ponto esta dentro da area delimitada
	if x > 0 and y > 0 and x < 320 and y < 200:
		# Mostra uma msg no terminal
		print 'Dentro da area'
		# Declara o tipo de fonte
		font = cv2.FONT_HERSHEY_SIMPLEX
		# Exibe um texto dentro da janela do OpenCV
		cv2.putText(drawing,"Objeto Detectado", (80,380), font, 0.5,(255,255,255))
		# Exibe as coordenadas do ponto
		print 'Coordenadas:', x, y
		
	else:
		# Mostra uma msg de negação no terminal
		print 'Fora da area'
		# Declara o tipo de fonte
		font = cv2.FONT_HERSHEY_SIMPLEX
		# Exibe uma msg dentro da janela do OpenCV
		cv2.putText(drawing,"Sem Movimento", (80,380), font, 0.5,(255,255,255))
		# Exibe as coordenadas do ponto
		print 'Coordenadas:', x, y
	
	# Pula uma linha
	print '\n'
	# Desenha um ponto na tela 
	# O -1 no final pinta o interior do ponto
	cv2.rectangle(drawing, (x, y), (x+4, y+4), (150, 150, 150), -1)
	# Cria a imagem final, um conjunto de : area delimitada
	# Ponto e msgs a serem exibidas na janela do OpenCV
	cv2.imshow("drawing", drawing)

	# Verificador de escape para fechamento do programa
	if cv2.waitKey(20) == 27:
		cv2.destroyWindow("drawing")
		self.cap.release()
		break	
	# Tempo de espera para criar nova imagem
	time.sleep(0.5)
