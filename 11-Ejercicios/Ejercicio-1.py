"""
Ejercicio 1 .Hacer un programa que tenga una lista 
de 8 numeros enteros y haga lo siguiente:
-Recorrer la lista y motrarla (Hecho)
-Hacer una función que recorra lista de numeros y devuelva un string (Hecho )
-Ordenarla y mostrarla (Hecho)
-Mostrar su longitud (Hecho )
-Buscar algun elemento (Que el usuario pida por teclado)
"""
#Crear una lista 
numeros  = [18,29,41,49,7,91,26]

def Recorrerlist(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += ("\n")

    return resultado 




#RECORRER Y MOSTRAR 
"""""
print("##########-RECORRER Y MOSTRAR-###########")
for numero in numeros:
    print(numero)
numeros.sort
print(numeros)
"""""
print(Recorrerlist(numeros))
print(Recorrerlist(numeros))

# ORDENAR UNA LISTA CON EL METODO SORT
print("######ORDENAR UNA LISTA#########")

numeros.sort()
print(Recorrerlist(numeros))

#MOSTRAR SU LONGITUD 
print("###############Mostrar longitud######")

print(len(numeros))

#BUSCAR LO QUE TE PIDA EL USUARIO EN UNA LISTA CON MANEJO DE ERRORES 

try:
    Busqueda = int(input("Introduce el número :"))

    comprobar = isinstance(Busqueda, int)

    while not comprobar or Busqueda <= 0:
        Busqueda = int(input("Introduce el número :"))
    else:
        print(f"Has introducido el {Busqueda}")

    print(f"########Buscar en la lista el número {Busqueda}########")

    Shearch = numeros.index(Busqueda)
    print(f"El número existe en la lista, es el indicé: {Shearch}")
except:
    print("El numero no esta en la lista, lo siento  ")




