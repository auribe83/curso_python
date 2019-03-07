#Ejemplo uso de operadores de comparacion concatenados

salario_presidente=int(input("Introduce salario presidente: "))
print("Salario Presidente: "+ str(salario_presidente))

salario_director=int(input("Introduce salario director: "))
print("Salario Director: "+ str(salario_director))

salario_jefe_area=int(input("Introduce salario Jefe Area: "))
print("Salario Jefe Area: "+ str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario Administrativo: "))
print("Salario Administrativo: "+ str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")