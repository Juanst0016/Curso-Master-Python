from tkinter import *

ventana = Tk()
#ventana.geometry("700x500")

texto = Label(ventana, text="Bienevenido a mi programa ")
texto.config(
            fg = "white",
            bg = "#000000",
            padx= 50,
            pady = 20,
            font = ("Consolas", 30)

            
)

texto.pack(side=TOP)


texto = Label(ventana, text="Soy Juan")
texto.config(
    height = "3",
    bg = "yellow",
    font = ("Arial", 20),
    padx =10,
    pady = 10,
    cursor = "Spider"
)
texto.pack(side= TOP, fill = X, expand=YES)#CON FILL RELLENO Y CON EXPAND EXPANDO TODO 

texto = Label(ventana, text="Basico")
texto.config(
    height = "3",
    bg = "orange",
    font = ("Arial", 20),
    padx =10,
    pady = 10,
    cursor = "Spider"
)
texto.pack(side = LEFT, fill = X, expand = YES)

texto = Label(ventana, text="Basico")
texto.config(
    height = "3",
    bg = "red",
    font = ("Arial", 20),
    padx = 10,
    pady = 10,
    cursor = "Spider"
)
texto.pack(side= LEFT, fill = X, expand = YES)

texto = Label(ventana, text="Basico")
texto.config(
    height = "3",
    bg = "green",
    font = ("Arial", 20),
    padx = 10,
    pady = 10,
    cursor = "Spider"
)
texto.pack(side = LEFT, fill = X, expand= YES)



ventana.mainloop()
