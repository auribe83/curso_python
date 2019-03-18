#se crea una funcion tradicional
def generaPares(limite):

	num=1

	miLista=[]

	while num<limite:

		miLista.append(num*2)

		num=num+1

	return miLista

print(generaPares(10))

print(" ")

#ahora se crea el generador
print(" ahora se crea el generador ")

def generaPares(limite):

	num=1


	while num<limite:

		yield num*2  #construye un objeto iterable que devuelve la funcion

		num=num+1

devuelvePares=generaPares(10)		

for i in devuelvePares:

	print(i)

#ahora se crea el generador de otra forma para que muesrte solo los objetos q se desean
print(" ahora se crea el generador ")

def generaPares(limite):

	num=1


	while num<limite:

		yield num*2  #construye un objeto iterable que devuelve la funcion

		num=num+1

devuelvePares=generaPares(10)	#se crea el objeto generador devuelvePares	

print(next(devuelvePares)) # con el next devuleve el primer objeto en su interior

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))


