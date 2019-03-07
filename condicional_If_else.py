#Condicional if-else

print("Verificacion de Acceso")

print() #imprime linea en blanco

edad_usuario=int(input("Introduce tu edad, por favor:"))

if edad_usuario <18:
	print("No puedes pasar")
elif edad_usuario >100:
	print("Edad incorrecta")
else:
	print("Puedes Pasar")

print("El programa ha finalizado")