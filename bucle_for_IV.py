#Ejemplo de for con cadena que comprueba cualquier email que se introduzca por teclado
contador=0
miEmail=input("Introduce tu direccion de Email: ")

#for i in "argenis429@gmail.com":
for i in miEmail:	
	if(i=="@" or i=="."):
		contador=contador + 1

if contador==2:
#if email: # otra forma de evaluar el if, asumiendo q es True	
	print("Email es correcto")
else:
	print("El email no es correcto")