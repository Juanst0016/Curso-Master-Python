"""
Ejercicio 8
¿Cuanto es el x% de x numero ?
ejemplo 20% de 150
"""
numero = int(input("Introduce el número :"))
porcentaje = int(input(f"¿Que porcentaje quieres sacar del {numero}? : "))

Operacion = (numero * (porcentaje/100))
print(f"El {porcentaje}% de {numero} es : {Operacion}")