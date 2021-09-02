######################FUNCIONES PREDEFINIDAS##############
Cantantes = ["Zarcort", "Harry Styles", "Zayn"]
numeros = [1, 3, 2, 5, 4]

#OREDENAR
print(numeros)
numeros.sort()
print(numeros)

#AGREGAR ELEMENTOS A UNA LISTA 
Cantantes.append("Ricardo fort")
print(Cantantes)
Cantantes.insert(1, "Louis")
print(Cantantes)

#ELIMINAR ELEMENTO DE UNA LISTA 
Cantantes.pop(1)
print(Cantantes)
Cantantes.remove("Zarcort")
# print(Cantantes)

#DAR LA VUELTA A UNA LISTA 

# numeros.reverse()
# print(numeros)

#BUSCAR DENTRO DE UNA LISTA
print("Zayn" in  Cantantes)

#CONTAR ELEMENTOS 
print(Cantantes)
print(len(Cantantes))

#VER CUANTAS VECES APARECE UN ELEMENTO EN UNA LISTA

print(Cantantes.count("Zayn"))

#CONSEGUIR INDICES
print(Cantantes.index("Zayn"))

#UNIR LISTAS
Cantantes.extend(numeros)

print(Cantantes)
