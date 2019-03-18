#como hacer que un bucle sea infinito
#Raiz cuadrada de un numero

import math

print("Programa de calculo de raiz cuadrada")

numero= int(input("Introduce un numero por favor: "))

intentos=0

while numero<0: # aqui la condicion es true
	print("No se puede hallar la raiz de un numero negativo")

	if intentos==2:
		print("Has consumido demasiados intentos. El programa ha finalizado")
		break; #sale de la linea de ejecucion del bucle y continua el recorrido

	numero= int(input("Introduce un numero por favor: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))