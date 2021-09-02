"""
Ejercicio7 
hacer un programa que muestre todos los numeros impares entro 
dos numeros que elija el usuario 
"""

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el numero segundo numero: "))

if numero1 < numero2:
    
    for x in range(numero1, (numero2 + 1)):
        if x%2 == 0:
            print(f"{x} Es PAR")
        else:
            print(f"{x} Es IMPAR")
    
else:
    print("El numero 1 debe ser mayor al 2")



