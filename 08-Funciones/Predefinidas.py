"""
funciones predefinidas que podemos usar como quieramos que viene con python 

"""
Nombre = "Juan Torres"
##FUNCIONES GENERALES
print(type(Nombre))


##DETECTAR EL TIPADO 

comprobar = isinstance(Nombre, int)
if comprobar:
    print("Esa variable es un string ")
else:
    print("No es una cadena ")

if not isinstance(Nombre, float):
    print("No es un numero con decimales ")


####LIMPIAR ESPACIOS
frase = "    Mi contenido      "
print(frase)
print(frase.strip()) #VA A LIMPIAR TODOS LO ESPACIOS DE LA PRIMERA IMPRESION POR PANTALLA 

# year = 2021

# del year 

# print(year)


###COMPROBAR VARIABLE VACIA 
texto = "   gg    "


if len(texto) <= 0:
    print("La variable esta vacia ")
else:
    print("La variable tiene contenido: ", len(texto ))

###### encontrar caractere 
frase = "La vida es bella "
print(frase.find("vida")) #SIRVE PARA ENONTRAR CARACTERES O PALABRAS

#### REMPLAZAR PALABRAS EN UN STRING 
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)


###PROCESAR MAYUSCULAS Y MINUSCULAS 
print(Nombre)
print(Nombre.upper())#MAYUSCULA
print(Nombre.lower())#MINUSCULA
 


