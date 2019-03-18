#Ejemplo de for con cadena que comprueba cualquier email que se introduzca por teclado
email=False
miEmail=input("Introduce tu direccion de Email: ")

#for i in "argenis429@gmail.com":
for i in miEmail:	
	if(i=="@"):
		email=True

if email==True:
#if email: # otra forma de evaluar el if, asumiendo q es True	
	print("Email es correcto")
else:
	print("El email no es correcto")