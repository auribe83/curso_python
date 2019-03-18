#instruccion continue dentro de un bucle

for letra in "Python":

	if letra=="h":
		continue #ignora el resto del bucle y pasa a la siguiente iteracion

	print("Viendo la letra: " + letra)

print(" ")
#otro ejemplo que cuenta la cantidad de caracteres
nombre="pildoras informaticas"

contador=0

for i in nombre:
	if i==" ":
		continue
	contador+=1 #incrementa el contador

#print(len(nombre))
print(contador)		