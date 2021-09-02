#PROGRAMACION ORIENTADA A OBJETOS 
#BASICAMENTE UNA CLASE ES UN MOLDE PARA CREAR MAS OBJETOS SIMILIRES O IGUAL A LA MISMA (YA ESTA EXPLICADO EN POO-EXPLICACION)

#DEFINIR UNA CLASE (molde para crear mas objetos )
#Coche con caracteristica similares 




class coche:
    #ATRIBUTOS O PROPIEDADES (VARIABLES)
    #CARACTERISTICAS DEL COCHE  
    
    color = "rojo"
    marca = "ferrari"
    modelo = "aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    #METODOS, SON ACCIONE QUE HACE EL OBJETO
    def setcolor(self, color):
        self.color = color 

    def getcolor(self):
        return self.color

    def setmodelo(self, modelo):
        self.modelo = modelo
    
    def getmodelo(self):
        return self.modelo


    def accelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

    def getvelocidad(self):
        return self.velocidad

#Fin definicion de clase 

#Crear objeto / instaciar la clase 
print("COCHE 1 : ")

Coche = coche()

Coche.setcolor("Amarillo ")
Coche.setmodelo("Murcielago")

print(Coche.marca, Coche.getmodelo(), Coche.getcolor())
print("Velocidad actual :", Coche.getvelocidad())

Coche.accelerar()
Coche.accelerar()
Coche.accelerar()
Coche.accelerar()
Coche.frenar()

print("Velocidad nueva :", Coche.getvelocidad())

print("--------------------------------------")

#CREAR MAS OBJETOS 
coche2 = coche()
coche2.setcolor("Azul")
coche2.setmodelo("Luciernaga")
print(coche2.getcolor())

print(coche2.marca, coche2.getmodelo(), coche2.getcolor())
    