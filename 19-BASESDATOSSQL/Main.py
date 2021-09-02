import mysql.connector
from mysql.connector.utils import print_buffer

#Conexion 
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd ="",
    database = "master_python"
)

#LA CONEXION HA SIDO CORRECTA? 

#print(database)

#CURSOR 

cursor = database.cursor(buffered=True)

#CREAR BASE DE DATOS 
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)
"""
#CREAR TABLAS

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10, 2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")
"""
cursor.execute("SHOW TABLES ")

for table in cursor:
    print(table)
"""
#cursor.execute("INSERT INTO vehiculos VALUES (null, 'Opel', 'Astra', 18500)")

coches = [
    ('Seat', 'Ibiza', 1200),
    ('renault', 'oroch', 1400),
    ('ford', 'ecosport', 3500),
    ('ferrari', 'vento', 9500),
    ('fort', 'focus', 2500)
]

cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)",coches)

database.commit()

cursor.execute("SELECT * FROM vehiculos")

result = cursor.fetchall()

print("------------------Todos los coches--------------------")

for coche in result:
    print(coche[1],coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()

print(coche)

#BORRAR COSAS DE UNA TABLA 

cursor.execute("DELETE FROM vehiculos WHERE marca = 'ford'")

database.commit()

#Ver los registros borrados 

print(cursor.rowcount, "Borrados")


#ACTUALIZAR

cursor.execute("UPDATE vehiculos SET modelo='aire' WHERE marca='ferrari'  ")

database.commit()

print(cursor.rowcount, "Actualizados ")


