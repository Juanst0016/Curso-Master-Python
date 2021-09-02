class coche:
    #ATRIBUTOS O PROPIEDADES (VARIABLES)
    #CARACTERISTICAS DEL COCHE  
    
    color = "rojo"
    marca = "ferrari"
    modelo = "aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    soy_publico = "Hola,soy un atributo publico "
    __soy__privado= "Hola, soy un atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas


    #METODOS, SON ACCIONE QUE HACE EL OBJETO

    def getPrivado(self):
        return self.__soy__privado
        
    def setcolor(self, color):
        self.color = color 

    def getcolor(self):
        return self.color

    def setmodelo(self, modelo):
        self.modelo = modelo
    
    def getmodelo(self):
        return self.modelo
    
    def setmarca(self,marca):
        self.marca = marca
    
    def getmarca(self):
        return self.marca
    

    def accelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

    def getvelocidad(self):
        return self.velocidad
    
    def getinfo(self):
        info = "--------Información del coche------------"
        info += "\n color " + self.getcolor()
        info += "\n Marca " + self.getmarca()
        info += "\n modelo " + self.getmarca()
        info += "\n Velocidad " + str(self.getvelocidad())

        return info

#Fin definicion de clase 

