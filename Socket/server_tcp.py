#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import os, sys

host = '192.169.40.90'
port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "\nAguardado Conexão\n"
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
sock.bind((host, port))
sock.listen(1)

conn, addr = sock.accept()
print "Conectado"

while True:
	comand = conn.recv(16)
	comand = comand.lower()

	if comand == 'z':
		os.system("python comand.py z")

	if comand == 'x':
		os.system("python comand.py x")

	if comand == 'w':
		os.system("python comand.py w")

	if comand == 's':
		os.system("python comand.py s")

	if comand == 'a':
		os.system("python comand.py a")

	if comand == 'd':
		os.system("python comand.py d")

	if comand == 'q':
		os.system("python comand.py q")

	if comand == 'e':
		os.system("python comand.py e")

	if comand == 'i':
		os.system("python comand.py i")

	if comand == 'k':
		os.system("python comand.py k")

print "Conexão finalizada\n\n"
os.system("python comand.py x")

conn.close()
