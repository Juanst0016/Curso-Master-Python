from tkinter import *

ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text="Bienevenido a mi programa ")
texto.config(
            fg = "white",
            bg = "#000000",
            padx= 50,
            pady = 20,
            font = ("Consolas", 30)

            
)

texto.pack()

def pruebas(nombre,apellido, pais):
    return f"hola {nombre} {apellido} veo que eres de {pais}"


texto = Label(ventana, text=pruebas(nombre ="Juan", apellido ="Torres", pais = "Argentina")) #Puedo cambiar el orden como yo quiera
texto.config(
    height = "100",
    bg = "orange",
    font = ("Arial", 20),
    cursor = "Spider"
)
texto.config(
    justify=RIGHT,
)

texto.pack(anchor = CENTER)



ventana.mainloop()
