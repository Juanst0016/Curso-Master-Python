from io import open #Para abrir o crear archivos tene en cuenta petiso 

import pathlib

import shutil

#Abrir archivo 
ruta = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"
print(ruta)
archivo = open(ruta, "a+")

#ESCRIBIR EN UN ARCHIVO 
archivo.write("---------Soy un texto metido desde python---------" "\n")

#CERRAR EL ARCHIVO 
#archivo.close()

#Abrir archivo  #Leer archivo 
ruta = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"
print(ruta)
archivo_Lectura = open(ruta, "r") #Leer archivo Tenes que meter la letra R (read)


open(ruta, "a+")

#LEER CONTENIDO 
#contenido = archivo_Lectura.read()

#print(contenido)

#LEER CONTENIDO Y GUARDARLO EN UNA LISTA 

lista = archivo_Lectura.readlines()
archivo_Lectura.close

for elemento in lista:
    elemento_lista = elemento.split() # Convertir frase en una lista 
    print(elemento_lista)
    #print("- "+ elemento.capitalize())


#COPIAR ARCHIVO
""""
ruta_original = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/ficheros_copiado.txt"
ruta_alternativa = "./07-Ejercicios/ficheros_copiado77.txt"
shutil.copyfile(ruta_original, ruta_alternativa)
"""

#MOVER UN ARCHIVO 
#ruta_original = str(pathlib.Path().absolute()) + "/ficheros_COPIADO.txt"
#ruta_nueva =  str(pathlib.Path().absolute()) + "/ficheros_COPIADO_Nuevo.txt"

#shutil.move(ruta_original, ruta_nueva)

#ELIMINAR
""""
import os 
os.remove(str(pathlib.Path().absolute()) + "/ficheros_COPIADO_Nuevo.txt")
"""

#COMPROBAR SI EXISTE 
import os.path

#print(os.path.abspath("./14"))
ruta_comprobar = os.path.abspath("./") + "/ficheros_texto.txt"
print(ruta_comprobar)


if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe ")

