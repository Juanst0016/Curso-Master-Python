#CAPTURAR EXCEPCIONES Y MANEJAR ERRORES DE CODIGO 
#SUCEPTIBLE A FALLOS O ERRORES 
"""
try:
    nombre = input("¿Cual es tu nombre ?:")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es  " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, introduce de forma correcta el nombre ")
else:
    print("Todo a funcionado correctamente ")
finally:
    print("Fin de la iteración")
    """

#MULTIPLES EXCEPCIONES 
"""
try:
    numero = int(input("Dime el numero para elevarlo al cuadrado :"))
    print("El cuadrado es :" + str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros en el código !!!")
#except ValueError:
#    print("Introduce un numero correcto ")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name__) #La E es para detectar un tipo de dato y asi mostrar el error 

"""

#EXCEPCIONES PERSONALIZADAS O LANZAR EXCEPCION
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad :"))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real ")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo ")
    else:
        print(f"Bienvenido al Master de python {nombre}")
except ValueError:
    print("Introduce los dato correctamente ")
except Exception as e:
    print("Existe un error ", e) 
    #FORMA MUY LINDA DE MANEJAR ERRORES 

    

