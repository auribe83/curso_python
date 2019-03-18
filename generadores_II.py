  # cuando se coloca una * en los parametros se le indica que recibira un numero 
 #indetermiando de parametros y los recibe en forma de tupla 

def devuelve_ciudades(*ciudades):
 	for elemento in ciudades:

 		#for subelemento in elemento:

 			yield from elemento

#se crea el objeto generador

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

def funcion_1(a, b):
    '''Esta funcion retorna la suma de ambos argumentos.'''
    return a + b


