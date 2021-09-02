import os
#COMO SE CREA UNA CARPETA

if not os.path.isdir("./Mi_carpeta"):
    os.mkdir("./Mi_carpeta")
else:
    print("Ya existe el directorio ")


#COMO BORRAR UNA CARPETA 
#os.rmdir("./Mi_carpeta")

#COMO COPIAR CARPETA
import shutil

ruta_original = "./Mi_carpeta"
ruta_nueva = "./Mi_carpeta_Copiada"

#shutil.copytree(ruta_original, ruta_nueva)
#os.rmdir("./Mi_carpeta_Copiada")

#LISTAR ARCHIVOS QUE ESTAN EL LA CARPETA 

print("Contenido de mi carpeta")
contenido = os.listdir("./mi_carpeta")

print(contenido)

for fichero in contenido:
    print("Fichero: " + fichero)

