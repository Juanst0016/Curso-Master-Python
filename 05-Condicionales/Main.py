#Si un dato cumple una funcion se daran un grupo de valores y si no otros grupos de valores

#Condicional IF

#Si se_cumple_esta_condicion:
    #Ejecutar grupos de instruciones
#SI NO:
    #SE ejecutan otro grupo de instrucciones

#If condicion:
    #Instrucciones
#Else:
    #Se ejecutaran otras instruciones 

#OPERADORES DE COMPARACION 
# == : IGUAL
# !: DIFERENTE
# <: MENOR QUE 
# >: MAYOR QUE  
# <= MENOR IGUAL QUE 
# >= MAYOR IGUAL QUE 

#Ejemplo 1

# print("#################E J E M P L O 1################")

# #color = input("Adivina cual es mi color favorito :")
# color = "Rojo"
# if color == "Rojo":
#     print("Felicitaciones!!!")
#     print("El color es rojo")    
# else:
#     print("Ese no es el color, intentalo denuevo")


#EJEMPLO 2 

# print("\n ############E J E M P L O 2############")

# #year = "2020"

# year = 2021

# if year >= 2021:
#     print("Estamos en un año posterior a 2021")
# else:
#     print("Estamos en un año anterior al 2021")

# #EJEMPLO 3

# print("\n ############E J E M P L O 3############")

# nombre = "Juan torres"
# ciudad = "Campana"
# continente = "America" 
# edad = 22

# mayoria_edad = 18

# if edad >= mayoria_edad:
#     print(f"{nombre} es mayor de edad")
#     if continente == "America ":
#         print("El usuario no es Americano")
#     else:
#         print("El usuario es americano y de " + f"{ciudad}")
# else: 
#     print(f"{nombre} no es mayo de edad")

# #EJEMPLO 4

# # print("\n ############E J E M P L O 4############")

# dia = int(input("Introduce el numero del dia de la semana: "))

# # if  dia == 1:
# #     print("Es lunes")
# # else:
# #     if  dia == 2:
# #         print("Es Martes ")
# #     else:
# #         if dia == 3:
# #             print("Es Miercoles")
# #         if dia == 4:
# #             print("Es Jueves")
# #         if dia == 5:
# #             print("Es Viernes")
# #         if dia == 6:
# #             print("Es finde semana")

# # nombre = "juan"  
# # apellido = "torres"
# # hermano = "mauricio" 

# # print("mi nombre es {} {} y mi hermano {}".format( nombre, apellido, hermano,))

# #EJEMPLO 4

# print("\n ############E J E M P L O 4############")


# if dia == 1:
#     print("Es Lunes")
# elif dia == 2:
#     print("Es Martes")
# elif dia == 3:
#     print("Es Miercoles")
# elif dia == 4:
#     print("Es Jueves")
# elif dia == 5:
#     print("Es Viernes")
# else:
#     print("Es finde semana")

#EJEMPLO 5

print("\n ############E J E M P L O 5############")

edad_minima = 18
edad_maxima = 65
edad_oficial = 22

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en una de trabajar")
else:
    print("No esta en edad de trabajar")

#Operadores logicos
#And = Y
#Or = o 
# ! = Negacion
#Not = no 

#EJEMPLO 6

print("\n ############E J E M P L O 6############")

# pais = "España"

# if pais == "Mexico " or pais == "España" or pais == "Colombia ":
#     print(f"{pais} Es un pais de habla hispana")
# else:
#     print(f"{pais} No es un pais de habla hispana")


# pais = "España"

# if not (pais == "Mexico " or pais == "España" or pais == "Colombia "):
#     print(f"{pais} No es un pais de habla hispana")
# else:
#     print(f"{pais} Si es un pais de habla hispana")

#EJEMPLO 7

print("\n ############E J E M P L O 7############")

pais = "EEUU"

if pais != "Mexico " and pais != "España" and pais != "Colombia":
     print(f"{pais} No es un pais de habla hispana")
else:
     print(f"{pais} Si es un pais de habla hispana")






                    
    

                

