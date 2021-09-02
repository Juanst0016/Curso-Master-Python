"""
Ejericio 9
Hacer un programa que pida numeros al usuario definidamente hasta meter el numero 111

"""
Contador = 1

while Contador < 100:
    numero = int(input("Introduce un número : "))


    if numero == 111:
        print("Programa finalizado ")
        break
    else:
        print(f"Has introducido el {numero}")
