#Tkinter
#ES UN MODULO PARA CREAR INTERFACES GRAFICAS DE USUARIO 
from tkinter import *
import os.path


class programa:

    def __init__(self):
        self.title = "Master pyhton"
        self.icon = "./imagenes/logo.ico"
        self.icon_alt = "./21-TKINTER/imagenes/logo.ico"
        self.size = "770x470"
        self.resizable = False
    
    def cargar(self):
        #Crear la ventana raiz 
        ventana = Tk()
        self.ventana = ventana

        #TITULO DE LA VENTANA
        ventana.title(self.title)

        #COMPROBAR SI EXISTE UN ARCHIVO 
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)



        #ICONO DE LA VENTANA
        ventana.iconbitmap(ruta_icono)

        #MOSTRAR TEXTO EN EL PROGRAMA 
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        #CAMBIO EN EL TAMAÑO EN LA VENTANA
        ventana.geometry(self.size)

        #BLOQUEAR TAMAÑO DE LA VENTANA 
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()
    
    def mostrar(self):
        self.ventana.mainloop() #ARRANCAR Y MOSTRAR VENTANA HASTA QUE CIERRE

        

#INSTANCIAR MI PROGRAMA 
programa  = programa()
programa.cargar()
programa.addTexto("Soy un master de python")
programa.addTexto("Hola")
programa.mostrar()

