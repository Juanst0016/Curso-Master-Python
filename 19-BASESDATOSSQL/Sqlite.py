#IMPORTAR MODULO 
import sqlite3
from sqlite3.dbapi2 import Connection, Cursor

#Conexion 

conexion = sqlite3.connect('./19-BASESDATOSSQL/pruebas.db')

#Crear cursor
cursor = conexion.cursor()
#Crear tabla 
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo VARCHAR(255), 
    descripcion text, 
    precio int(255)
);
""")

#GUARDAR CAMBIOS 
conexion.commit()

#INSERTAR DATOS 

cursor.execute("INSERT INTO productos VALUES (null, 'primer producto', 'Descripción de mi producto ', 550 )")
conexion.commit()

#BORRAR REGISTRO 
cursor.execute("DELETE FROM productos")
conexion.commit()

#INSERTAR MUCHOS REGISTROS DE GOLPE 
productos = [
    ("Ordenador portatil", "Buen Pc", 80),
    ("Telefono", "Rog", 900),
    ("TV", "Samsung 4k", 1200),
    ("Xbox ", "Consola ", 500)

]

cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)

conexion.commit()

#UPDATE 
cursor.execute("UPDATE productos SET precio =650 WHERE precio = 80" )

#LISTAR DATOS 
cursor.execute("SELECT * FROM productos WHERE precio >= 100 ;")

print(cursor)
productos = cursor.fetchall()

for producto in productos:
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripción:",  producto[2])
    print("Descripción:", producto[3])
    print("\n")

cursor.execute("SELECT TITULO FROM productos ;")
producto = cursor.fetchone()

print(producto)


#CERRAR CONEXIÓN 
conexion.close()

