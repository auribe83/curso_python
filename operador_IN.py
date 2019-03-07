#Operador IN
print("Asignaturas Optativas ano 2019")
print()
print(" Asignaturas Optativas: Informatica Grafica - Pruebas de Software - Usabilidad y accesibilidad")

asignatura=input("Escribe la asignatura escogida: ")

#opcion=input("Escribe la asignatura escogida: ")
#asignatura=opcion.lower()

if asignatura in ("Informatica Grafica", "Pruebas de Software", "Usabilidad y accesibilidad"):

	print("Asignatura elegida " + asignatura)

else:

	print("La asignatura escogida no esta contemplada")