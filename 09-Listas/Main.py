"""
LISTAS O (ARRAYS)
SON COLECCIONES DE DATOS BAJO UN UNICO NOMBRE 
PARA PODER ACCEDER A ESOS DATOS DEBEMOS USAR UN INDICE NÚMERICO.

"""
# pelicula = "Batman"
# #DEFINIR LISTA JUANCHO ESTO MAS O MENOS YA LO SABES 
# peliculas = ["batman", "spiderman", "el señor de los anillos" ]
# cantantes = list(("2pa", "eminem", "zarcort")) #SIEMPRE PONER UNA TUPLA PARA PODER MODIFICAR UNA LISTA 
# years = list(range (2000, 2022))
# Variada = [21, "Juan", "buena gente ", "año 2021"]



# """"
# print(pelicula)
# print(cantantes)
# print(years)
# print(Variada)
# """

# ## INDICES 
# peliculas[1] = "Iron man" # modificar indice de las listas que creo (OSEA JUANCHO REMPLAZO COSAS DE LA LISTA)
# print(peliculas[1])
# print(peliculas[0])
# print(peliculas[2])
# print(peliculas[0:3])#VA SACAR DESDE EL 1 AL 3 ESTO ES PARA CUANDO QUERES MANDAR ALGUNOS SELECTIVOS DE LA LISTA
# print(peliculas[0:])

# #AÑADIR ELEMENTOS A UNA LISTA 
# cantantes.append ("Alejandro sans")
# cantantes.append("Spiderman y yolanda")
# print(cantantes)

# print("##########LISTADO DE PELICULAS#########")

# #RECORRER LISTA 
# nueva_pelicula = "nada"
# while nueva_pelicula != "parar":
#     nueva_pelicula = input("Introduce la nueva pelicula: ")

#     if nueva_pelicula != "parar":
#         peliculas.append(nueva_pelicula)


# for pelicula in peliculas:
#     print(f"{peliculas.index(pelicula)}. {pelicula}")#VER INDICE DE PELICULAS Y NUMERACION DE CADA UNA 


##############LISTAS MULTIDIMENCIONALES################
print("##################LISTADO DE CONTACTOS#####################")

Contactos = [
    [
        "Juan" ,
        "Juanst0016@gmail.com"
    ],
    [
        "Luis" ,
        "Luis@gmail.com"
    ],
    [
        "Mauricio" ,
        "Mauri@gmail.com"
    ]
]

for contacto in Contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")


# print(Contactos[1][1]) 


