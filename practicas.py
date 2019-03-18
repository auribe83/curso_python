#Lee cadena inversa

def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

print(inversa("hola"))    

def maxi(num1,num2):
	if num1 > num2:
		print ("El " + str(num1) + " es mayor que el "+ str(num2) )
	elif num2 > num1:
		#print (num2)
		print ("El " + str(num2) + " es mayor que el "+ str(num1) )
	else:
		print("Son iguales")

print(maxi(100,100))    

def largo_cadena(lista):
	cont=0
	for i in lista:
		cont=cont+1
	return cont

print(largo_cadena("argenis"))  	

def letra_vocal(v):
	if v=="a" or  v=="e" or  v=="i" or  v=="o" or  v=="u":
		return True
	elif v=="A" or  v=="E" or  v=="I" or  v=="O" or  v=="U":
		return True
	else:
		return False

print (letra_vocal("a"))		


