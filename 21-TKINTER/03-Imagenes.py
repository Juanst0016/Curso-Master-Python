from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()

ventana.geometry("700x500") 

Label(ventana, text="Hola soy Juan").pack(anchor = W)

imagen = Image.open("./21-TKINTER/imagenes/google.png")
render = ImageTk.PhotoImage(imagen)
Label(ventana, image=render).pack(anchor = E)


ventana.mainloop()