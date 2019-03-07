#Diccionario en pyton, los diccionario van entre llaves{}

miDiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","Espana":"Madrid"}

#se accede mediante la clave, para obtener el valor
print(miDiccionario["Alemania"])

#imprime todo el diccionario
print(miDiccionario)

#agregar elemento al diccionario
miDiccionario["Venezuela"]="Caracas222"

print(miDiccionario)

#modificar elemento al diccionario, se sobreescribe el valor
miDiccionario["Venezuela"]="Caracas"

print(miDiccionario)

#eliminar elemento al diccionario
del miDiccionario["Reino Unido"]

print(miDiccionario)