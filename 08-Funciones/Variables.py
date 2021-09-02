"""
UNA VARIABLE LOCAL Y UNA VARIABLE GLOBAL
VARIABLE LOCAL = ES AQUELLA QUE SE DEFINE EN LA FUNCION Y QUE SOLO SE PUEDE UASR UN RETURN
PARA DEVOLVERLA 

VARIABLE GLOBAL = SON LAS QUE SE DECLARAN FUERA DE LA FUNCION Y ESTAN DISPONIBLES DENTRO Y FUERA 
DE LA FUNCION 
"""

#VARIABLE GLOBAL 
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holamundo():
    frase = "Hola mundo "
    print("Dentro de la función")
    print(frase)

    year = 2021
    print(year)

    global website #ASI ES COMO SE PONE UNA VARIABLE GLOBAL 
    website = "JUANTORRES.COM"



    return "Dato devuelvo " + str(year)

print(holamundo())

print("Fuera", website)