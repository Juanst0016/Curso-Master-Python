"""
Ejericio 5.
crear una lista con el contenido de esta tabla :
ACCION - AVENTURA - DEPORTE
GTA       AC        FIFA 
COD       CRASH      PRO
PUGB      PRINCE     MOTO GP
Mostrar esta informacion ordenada
"""

tabla = [
    {
        "CATEGORIA" : "ACCIÓN",
        "JUEGOS" : ["GTA", "PUBG", "COD"]
    },
    {
        "CATEGORIA" : "AVENTURA",
        "JUEGOS" : ["AC", "CRASH", "PRINCE"]
    },
    {
        "CATEGORIA" : "DEPORTE",
        "JUEGOS": ["FIFA", "PRO", "MOTO GP "]
    }
]

for categoria in tabla:
    print(f"------------{categoria['CATEGORIA']}--------------------") #SIEMPRE COMILLAS SIMPLES PARA ACCEDER AL DICCIONARIO 
    for juegos in categoria['JUEGOS']:
        print(juegos)

