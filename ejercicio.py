#!/usr/bin/python3
# -*- coding: utf-8 -*-

fichero = open('/etc/passwd', 'r')

lineas = fichero.readlines()
fichero.close()

diccionario = {}
for linea in lineas:
	elementos = linea.split(':')
	usuario = elementos[0]
	shell = elementos[-1][:-1]
	diccionario[usuario] = shell

print("La shell del usuario root es: " + diccionario['root'])
try:
	print("La shell del usuario imaginario es: " + diccionario['imaginario'])
except:
	print("El nombre de usuario 'imaginario' no existe")