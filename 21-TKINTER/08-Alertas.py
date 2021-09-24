from tkinter import *

from tkinter import messagebox as Messagebox

ventana = Tk()
ventana.geometry("400x400")
ventana.config(
    bd=70
)

def sacarAlerta():
    Messagebox.showwarning("Alerta", "Soy Juan torres")


Button(ventana, text="Mostrar Alerta ", command = sacarAlerta).pack()

def salir(nombre):
    resultado = Messagebox.askquestion("Salir", "¿Quieres continuar ejecutando la aplicación?")

    if resultado != "yes":
        Messagebox.showinfo("Chau", f"Adios {nombre}")
        ventana.destroy()


Button(ventana, text="Salir", command = lambda:salir("Juan torres")).pack()




ventana.mainloop()