#BUCLE FOR 
# for variable in elemento_iterable (Lista-Rango-Etc)
    #BLOQUE DE INSTRUCCION 

contador = 0
resultado = 0

for contador in range (0,10):
    print("voy por el " + str(contador))

    resultado += resultado + contador
print(f"El resultado es: {resultado}" )


#EJEMPLO TABLA MULTIPLICAR

print("\n######## E J E M P L O 2##########")

numero_usuario = int(input("¿De que numero quieres ver la tabla ? :"))

if numero_usuario < 1:
    numero_usuario = 1

print(f"###### Tabla de Multiplicar del numero {numero_usuario}######")

for numero_tabla in range(0, 10):

    if numero_usuario == 45:
        print("no se pueden mostrar numeros prohibidos")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada.") 