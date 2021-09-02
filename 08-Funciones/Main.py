#Las funciones son un conjunto de intrucciones agrupadas bajo un nombre concreto 
#y pueden reutiliarse tantas veces como quieras 
"""
def  NombreDemiFuncion (Parametros)
    #BLOQUE DE CODIGO O CONJUNTO DE INTRUCCIONES 

NombreDeMiFuncion (Mi_Parametro)
"""

#Definir funcion 
#Ejemplo 1
# from os import pipe


# print("####### EJEMPLO1 #########")

# def muestranombre():
#     print("Juan")
#     print("Mauri")
#     print("Agus")

# #TENGO QUE INVOCAR UNA FUNCION
# muestranombre()
# muestranombre()
# muestranombre()

#Ejemplo 2
"""
print("########### EJEMPLO2 #############")



def mostrartunombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")


    if edad >= 18:
        print("Y eres mayor de edad ")


Nombre = (input("Introduce tu nombre : "))
edad = (int(input("Introduce tu edad : ")))

mostrartunombre(Nombre,edad)
#Parametro un dato que pasa desde afuera hasta adentro de la función 
"""
#Ejemplo 3
# print("######### EJEMPLO 3 ###########")

# def tabla(numero):
#     print(f"Tabla de multiplicar del número: {numero}")

#     for contador in range (11):
#         operacion = numero*contador
#         print(f"{numero} x {contador} = {operacion}")
    
#     print("\n")
# tabla(1)
# tabla(2)

# # EJEMPLO 3.1
# print("Ejemplo 3.1")

# for numero_tabla in range (1,11):
#     tabla(numero_tabla)
    


#EJEMPLO 4
#PARAMETROS OPCIONALES 
# print("######### EJEMPLO 4 ###########")
# def getEmpleado(nombre, dni = None):
#     print("EMPLEADO")
#     print(f"Nombre: {nombre} ")

#     if dni != None:
#         print(f"DNI: {dni}")

# getEmpleado("Juan Torres", 417636191)

#########EJEMPLO5############
#PARAMETROS OPCIONALES Y RETURN O DEVOLVER DATOS
# print("#############EJEMPLO5###############")

# saludame = "Juan torres" 


# def saludame(nombre):
#     saludo = f"Hola, saludos {nombre}"
    
#     return saludo 

# print(saludame("juan Torres"))

########EJEMPLO 6 ############

# def calculadora(numero1, numero2, basicas = False ):
#     suma = numero1 + numero2
#     resta = numero1 - numero2
#     multi = numero1 * numero2 
#     division = numero1 / numero2   
    
#     cadena = ""
#     if basicas != False:
#         cadena += "Suma: " + str(suma) 
#         cadena += "\n"
#         cadena += "Resta: " + str(resta)
#         cadena += "\n"
#     else:
#         cadena += "Multipliación:" + str(multi)
#         cadena += "\n"
#         cadena += "Division: " + str(division)
        


    
#     return cadena
# print(calculadora(56, 5, False))


########EJEMPLO 7 ############


# print("############# EJEMPLO 7 ##############")

# def getnombre(nombre):
#     texto = f"El nombre es {nombre}"
#     return texto

# def getapellidos(apellidos):
#     texto = f"El Apellido es {apellidos}"
#     return texto
     
     
# def Devuelvetodo(nombre, apellidos):
#     texto = getnombre(nombre) + "\n" + getapellidos(apellidos)
#     return texto

# print(getnombre("Juan") + "\n" + getapellidos("Torres"))

###################### EJEMPLO 8 ##################
print("############### EJEMPLO 8 ###################")

#FUNCIONES LAMBDA SON FUNCIONES QUE NO TIENEN NOMBRE CONCRETO Y QUE NO HACE FALTA DEFINIRLA CON EL DEF 
#SIRVEN PARA TAREAS SIMPLES Y PEQUEÑAS 

dime_el_year = lambda year: f"El año es {year * 50 }" 

print(dime_el_year(2013))

#YA VISTE QUE SON TAREAS CORTITA JUAN DEL FUTURO 






