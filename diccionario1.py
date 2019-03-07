
miDiccionario={"Alemania":"Berlin",23:"Jordan","Mosqueteros":3}

print(miDiccionario)

#utilizando una tupla en los diccionarios
mitupla=["Espana","Francia","Reino Unido","Alemania"]

miDiccionario1={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}

print(miDiccionario1)

#se accede al valor de un elemento
print(miDiccionario1["Francia"])

#un diccionario almacene una tupla

miDiccionario2={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}

print(miDiccionario2)

print(miDiccionario2["anillos"])

#un diccionario que almacene otro diccionario
miDiccionario3={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}

print(miDiccionario3)

#imprimir las claves del diccionario
print(miDiccionario3.keys())

#imprimir los valores del diccionario
print(miDiccionario3.values())

#imprimir la logintud del diccionario
print(len(miDiccionario3))