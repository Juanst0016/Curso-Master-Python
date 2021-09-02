from Coche import coche 

carro = coche("Amarillo", "Renault", "Oroch", 214, 200, 4)

print(carro.getinfo())

#Esto sirve para crear varios objetos del mismo padre y variables entre si con ligeros cambios 

#DETECTAR TIPADO 
if type (carro) == coche:
    print("Es un objeto correcto ")
else:
    print("No es un objeto ")


#VISIBILIDAD PUBLIC O PRIVATE 

print(carro.soy_publico)

print(carro.getPrivado())