"""
FUNCIONALIDADES YA HECHAS PARA REUTILIZAR 
EN PYTHON HAY MUCHOS MODULOS, QUE LOS PUEDES CONSULTAR AQUI:
https://docs.python.org/3/py-modindex.html 

PODEMOS CONSEGUIR MODULOS QUE YA VIENEN EN EL LENGUAJE
MODULOS EN INTERNET Y TAMBIEN PODEMOS CREAR NUESTROS MODULOS 
"""

#IMPORTAR MI MODULO 

#import Mimodulo  
#from Mimodulo import holamundo
#from Mimodulo import *

#print(Mimodulo.holamundo("Juan Torres WEB"))
#print(Mimodulo.calculadora(3,4,True))

#print(holamundo("Juan torres"))

#Modulod de fechas 
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)

fechapersonalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada", fechapersonalizada)

print(datetime.datetime.now().timestamp())

#MODULOS MATEMATICAS
import math 

print("Raiz cuadrada de 10 : ", math.sqrt(10))

print("Numero Pi :", float(math.pi))
print("Redondear :", math.floor(4.38512))

#MODULO RAMDON 
import random

print("Numero aleatorio entre 15 y 20:", random.randint(15, 67))
