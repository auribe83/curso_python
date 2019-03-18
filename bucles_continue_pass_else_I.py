#instruccion pass dentro de un bucle

#class Miclase:
	#pass #Para implementar mas tarde, el pass devuleve un null

#instruccion break dentro de un bucle	
email=input("Introduce tu email por favor: ")

for i in email:

	if i=="@":

		arroba=True

		break; #se sale del bucle for y continuara la ejecucion del programa
else:

	arroba=False

print(arroba)