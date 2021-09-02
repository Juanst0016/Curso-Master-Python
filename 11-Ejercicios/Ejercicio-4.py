"""
Ejercicio 4.
Crear un scrip que tenga 4 variables, una lista, un entero, un booleano, un string 
y que imprima un mensaje segun el tipo de dato de cada variable

"""
def traducir(tipo):
    result = None
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "Cadena de texto"
    elif tipo == int:
        result = "Numero entero "
    elif tipo == bool:
        result = "Booleano"

    return result

    


def comprobar_tipado(dato, tipo):
    test = isinstance(dato,tipo)
    result = ""

    if test:
        result = f"Este del tipo {traducir(tipo)}"
    else:
        result = "El tipo de dato no es correcto "
    
    return result





mi_lista = ["Hola mundo", 77]
titulo = "Master en python"
numero = 100
verdadero = True 

print(comprobar_tipado(mi_lista,list))
print(comprobar_tipado(titulo,str))
