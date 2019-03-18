#Bucle While

edad=int(input("Introduce la edad por favor: "))

while edad <5 or edad>100:
	print("Has introducido una edad incorrecta. Vuelve a intentarlo")
	edad=int(input("Introduce la edad por favor: "))

print("Gracias  por colaborar. Puedes pasar")
print("Edad del aspirante " + str(edad))
