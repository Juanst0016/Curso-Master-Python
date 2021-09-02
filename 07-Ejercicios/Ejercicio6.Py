"""
Ejercicio6
Mostrar las tablas de multiplicar del 1 al 10
mostrando el titulo de la tabla y luego las multiplicaciones 
"""

for cabecera in range (1, 11):
    print("##########")
    print(f"########## TABLA DEL {cabecera} ######### ")
    print("####################")

    for numero in range (1, 11):
        print(f"{numero} x {cabecera} = {numero*cabecera}")

    print("\n")
