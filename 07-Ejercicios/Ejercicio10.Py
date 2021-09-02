"""
Ejercicio 10
El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla 
cuanto han aprobado y cuantos han desaprobado.
"""

contador =  0
Aprobados = 0
Desaprobados = 0

numero_alumnos = int(input("¿Cuantos alumnos tienes? : "))

while contador <= numero_alumnos:
    nota = int(input(f"¿Que nota quiere ponerle al  \"alumno {contador}\" ?:"))

    contador += 1

    if  nota >= 5:
        Aprobados += 1
    else:
        Desaprobados += 1
    
print(f"Alumnos aprobados : \n{Aprobados}")
print(f"Alumnos desaprobados : \n{Desaprobados}")