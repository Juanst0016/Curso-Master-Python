"""
Ejercicio 2
Escribir un scrip que nos muestre por pantalla 
todo los numeros pares del 1 al 120

"""
#Para dividir tenes que poner esto % juancho soy tu yo del pasado esforzate 

contador = 1 

for contador in range(1,121):
    if contador%2 == 0:
        print(f"{contador} es par")
    else:
        print(f"{contador} es impar")