#! /usr/bin/python
#! -*- coding: UTF-8 -*-

Numeros = range(1,11)
for Indice in Numeros:
	#print ("\n")
	print ("Tabla del " + str(Indice))
	print("------------------")
	for Indice_2 in Numeros:
		print (str(Indice) + " por " + str(Indice_2) + " es : " + str(Indice * Indice_2))