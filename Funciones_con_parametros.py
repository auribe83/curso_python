#Funciones con parametros

#Ejemplo1
def suma():
	num1=5
	num2=7
	print (num1+num2)

suma()

#Ejemplo2
def suma1(num1,num2):
	print(num1+num2)

suma1(100,50)

#Ejemplo3
def suma2(num1,num2):
	resultado= num1 + num2
	return resultado

print(suma2(3,2))

#se almacena el valor de la funcion en una variable
almacena_resultado=suma2(4,2)

print(almacena_resultado)
