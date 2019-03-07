#Tuplas, las tuplas se les conoce porque se crean desntro de parantesis

miTupla=("Juan",13,1995)

print(miTupla[2])

#convertir tupla en lista
miLista=list(miTupla)

print(miLista)

#convertir lista en tupla
miLista1=("Argenis",36,1983,"M")
miTupla=tuple(miLista1)

print(miLista1)
print("Argenis" in miTupla) # verifica si el elemneto esta en la tupla
print(miTupla.count(36))    # cuenta cuantas veces esta el elemento en la tupla
print(len(miTupla))    # longitud de la tupla

#Tupla unitaria
miTupla2=("Ivanna",)
print(len(miTupla2)) 
print(miTupla2)

#Desempaquetados de tuplas, se colocan los elementos de la tupla en una varible por elemento
miTupla3=("Holys",28,1,1952)
nombre,dia,mes,agno=miTupla3

print(nombre)
print(dia)
print(mes)
print(agno)