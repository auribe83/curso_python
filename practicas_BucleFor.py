contadorarroba=0
contadorpunto=0

for i in input("Introduce tu email: "):

 if(i=="@"):
 	contadorarroba=contadorarroba+1

 if(i=="."):
 	contadorpunto=contadorpunto+1


if contadorarroba==1 and contadorpunto>=1:
	print("Email correcto")
else:
	print("El email no es correcto")