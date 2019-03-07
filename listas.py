#Manejo de listas

miLista=["Maria","Pepe","Marta","Antonio"]

#se imprime la lista completa
print(miLista[:])

#se imprime un elemento de la lista
print(miLista[2])

#se imprime  elemento de la lista por porciones, solo cuando es extensa
print(miLista[0:2])

#se imprime  elemento de la lista por porciones, solo mostrara lo restante de la lista al final
print(miLista[2:])

#agregar elementos al final de la lista
miLista.append("Sandra")

print(miLista[:])

#agregar elementos a una posicion determinada de la lista
miLista.insert(2,"Argenis")

print(miLista[:])

#agregar varios elementos a la lista
miLista.extend(["Ivanna","Miguel","Lucia"])

print(miLista[:])

#imprime el indice de un elemento de la lista
print(miLista.index("Ivanna"))

""" se verifica si un elemento se encuentra en la lista, 
devuelve true si es verdadero y false en caso contrario """
print("Ylaya" in miLista)

#Eliminar elementos de una lista
miLista.remove("Lucia")

print(miLista[:])


#Eliminar el ultimo elemento agregado en la lista
miLista.pop()

print(miLista[:])