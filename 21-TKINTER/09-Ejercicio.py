"""
calculadora que debe tener 
-dos campos de texto 
-4 botones para las operaciones 
-mostrar el resultado en una alerta

"""

from tkinter import *

from tkinter import messagebox 

ventana = Tk()
ventana.title("Ejercicio con Tkinter ")
ventana.geometry("400x400")
ventana.config(
    bd=25
)

def convertirFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("Error", "Introduce bien los datos ")

def sumar():
    try:
        resultado.set(float(numero1.get()) + float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos ")
    

def restar():
    try:
        resultado.set(float(numero1.get()) - float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos ")

def multiplicar():
    try:
        resultado.set(float(numero1.get()) * float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos ")

def dividir():
    try:
        resultado.set(float(numero1.get()) / float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos ")


def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operación es: {resultado.get()}")
    numero1.set("")
    numero2.set("")



numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=250, height = 200)

marco.config(
    padx = 15,
    pady=15,
    bd = 5,
    relief = SOLID,

)
marco.pack(side = TOP, anchor = CENTER)
marco.pack_propagate(False)

Label(marco, text= "Primer numero ").pack()
Entry(marco, textvariable = numero1, justify = CENTER).pack()

Label(marco, text= "Segundo numero ").pack()
Entry(marco, textvariable = numero2, justify = CENTER).pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command = sumar).pack(side = LEFT, fill=X, expand= YES)
Button(marco, text="Restar", command= restar).pack(side = LEFT, fill=X, expand= YES)
Button(marco, text="Multiplicar", command= multiplicar).pack(side= LEFT, fill=X, expand= YES)
Button(marco, text="Dividir", command= dividir).pack(side= LEFT, fill=X, expand= YES)










ventana.mainloop()

