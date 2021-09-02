"""
Set es un tipo de dato, para tener una coleccion de valores,
pero no tiene ni indice ni orden 
"""
personas = {
    "victor",
    "Manolo",
    "Francisco"
}

personas.add("Franco")
personas.remove("Manolo")
print(type(personas))
print (personas)