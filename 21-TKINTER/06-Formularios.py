from tkinter import *

ventana = Tk()

ventana.geometry("700x400")

ventana.title("Formulario en Tkinter")

#TEXTO ENCABEZADO 
encabezado = Label(ventana, text= "formularios con Tkinters")
encabezado.config(
    fg = "white",
    bg = "darkgray",
    font = ("Open Sans", 18),
    padx = 10,
    pady = 10
)
encabezado.grid(row =0 , column = 0, columnspan = 12, sticky = W)

#LABEL PARA EL CAMPO 
label = Label(ventana, text= "Nombre")
label.grid(row=1, column = 0,sticky = W, padx = 5, pady =5)

#CAMPO DE TEXTO 
campo_texto = Entry(ventana)
campo_texto.grid(row = 1, column = 1, sticky = W, padx = 5, pady =5)
campo_texto.config(justify = "right", state = "normal")

#LABEL PARA EL CAMPO Apellidos 
label = Label(ventana, text= "Apellidos")
label.grid(row=2, column = 0,sticky = W, padx = 5, pady =5)

#CAMPO DE TEXTO  Apellidos 
campo_texto = Entry(ventana)
campo_texto.grid(row = 2, column = 1, sticky = W, padx = 5, pady =5)
campo_texto.config(justify = "left", state = "normal")

#LABEL PARA EL CAMPO descripcion
label = Label(ventana, text= "Descripción")
label.grid(row=3, column = 0,sticky = N, padx = 5, pady =5)

#CAMPO GRANDE TEXTO DESCRIPCION

campo_grande = Text(ventana)
campo_grande.grid(row=3, column = 1,)
campo_grande.config(
    width = 30,
    height = 5,
    font = ("Arial 12"),
    padx= 15,
    pady = 15
)

#BOTON EN TKINTER
Label(ventana).grid(row = 4, column = 1)

boton = Button(ventana, text = "Enviar")
boton.grid(row = 5, column = 1, sticky = W)
boton.config(
    padx=15,
    pady=15,
    bg ="black",
    fg = "white"
)



ventana.mainloop()