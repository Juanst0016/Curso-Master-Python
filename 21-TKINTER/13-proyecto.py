"""

CREAR UN PROGRAMA QUE  TENGA UNA VENTANA
-QUE TENGA UNA VENTANA TAMAÑO FIJO 
-DIFERENTES PANTALLAS
-A LAS CUALES ACCEDER MEDIANTE MENU
-UN MENU
-FORMULARIO AÑADIR PRODUCTOS 
-GUARDAR DATOS TEMPORADOS 
-MOSTRAR DATOS LISTADOS EN LA PANTALLA PRINCIPAL
-OPCION DE SALIR
"""

from tkinter import *

from tkinter import ttk

#DEFINIENDO VENTANA

ventana = Tk()
#ventana.geometry("500x500")
ventana.minsize(400,400)
ventana.title("Proyecto Tkinter")
ventana.resizable(0, 0)

#PANTALLAS 
def home():
    home_label.config(
        fg = "white",
        bg = "black",
        font = ("Arial 30"),
        padx = 180,
        pady= 20,
    )

    home_label.grid(row=0, column = 0)

    products_box.grid(row=2)

    #LISTAR PRODUCTOS

    """
    for product in products:
        if len(product) == 3:
            product.append("Añadido")
            Label(products_box, text = product[0]).grid()
            Label(products_box, text = product[1]).grid()
            Label(products_box, text = product[2]).grid()
            Label(products_box, text = "-------------").grid()

    """

    for product in products:
        if len(product) == 3:
            product.append("Añadido")
            products_box.insert("",0,text=product[0], values = (product[1]))


    #Ocultar pantalla   
    add_label.grid_remove()
    boton.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()




def add():    
    #ENCABEZADO 

    add_label.config(
    fg = "white",
    bg = "black",
    font = ("Arial 30"),
    padx = 60,
    pady= 20
    )
    add_label.grid(row = 0, column = 0, columnspan = 10)

    #CAMPOS DEL FORMULARIO 
    add_frame.grid(row = 1)
    add_name_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)
    add_name_entry.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)


    add_price_label.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = E)
    add_price_entry.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)

    add_description_label.grid(row = 3, column = 0, padx=5, pady = 5, sticky =NW)
    add_description_entry.grid(row=3, column = 1, padx = 5, pady = 5, sticky = NW)
    add_description_entry.config(
        width = 20,
        height = 8,
        font = ("Consolas", 12),
        padx = 15,
        pady = 15,

    )


    boton.grid(row=5, column= 0, sticky =N)
    boton.config(
        padx = 15,
        pady = 5,
        bg = "green",
        fg = "white",
    )

    products_box.grid_remove()
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()


    add_label.grid(row=0, column = 0)


def info():
    info_label.config(
    fg = "white",
    bg = "black",
    font = ("Arial", 30),
    padx = 100,
    pady= 20
    )
    info_label.grid(row=0, column = 0, )
    data_label.grid(row = 1, column = 2)


    add_label.grid_remove()
    boton.grid_remove()
    add_frame.grid_remove()
    home_label.grid_remove()
    products_box.grid_remove()
    
    

    data_label.grid(row=1, column = 0)

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    

    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0",END)

    home()

#Variables IMPORTANTES
products = []
name_data = StringVar()
price_data = StringVar()



#DEFINIR CAMPO DE PANTALLAS 
home_label = Label(ventana, text= "Incio")
products_box = Frame(ventana, width=250)
Label(ventana).grid(row=1)

Label(products_box).grid(row=0)
products_box = ttk.Treeview(height = 12, columns = 2, )

products_box.grid(row=1,column = 0, columnspan = 2)
products_box.heading("#0", text="Producto", anchor = W)
products_box.heading("#1", text="Precio", anchor = W)


#DEFINIR CAMPO DE  PANTALLA (ADD)
add_label = Label(ventana, text= "Añadir producto")

#CAMPOS DE FORMULARIO 
add_frame = Frame(ventana)
add_name_label = Label(add_frame, text = "Nombre del producto :")
add_name_entry = Entry(add_frame,textvariable = name_data)

add_price_label = Label(add_frame, text = "Precio del producto :")
add_price_entry = Entry(add_frame,textvariable = price_data)

add_description_label = Label(add_frame, text = "Descripción :")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame)

boton = Button(ventana, text= "Guardar", command = add_product)



#DEFINIR CAMPO DE PANTALLA (INFO)
info_label = Label(ventana, text= "Información")
data_label = Label(ventana, text= "Creado por Juan torres")



#CARGAR PANTALLA DE INICIO 
home()

#MENU SUPERIOR 
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command = home)
menu_superior.add_command(label= "Añadir", command = add)
menu_superior.add_command(label="Información", command = info)
menu_superior.add_command(label = "Salir", command=ventana.quit)

#CARGAR MENU 
ventana.config(menu = menu_superior)

#CARGAR VENTANA
ventana.mainloop()