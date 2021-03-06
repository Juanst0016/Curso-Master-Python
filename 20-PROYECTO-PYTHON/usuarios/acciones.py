import usuarios.usuario as modelo
import notas.acciones
 
class Acciones:
 
    def registro(self):
        print("\nOk¡¡ Vamos a registrarte en el sistema...")
 
        nombre = input("¿Cual es tu nombre?: ")
        apellido = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")
 
        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()
 
        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}" )
        else:
            print("No te has registrado correctamente¡¡¡")
 
    def login(self):
        print("\nVale¡¡ Identificate en el sistema...")
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:
                 print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]} ")
                 self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto, intentalo mas tarde ")


    def proximasAcciones(self, usuario ):
        print(""" 
        Acciones disponibles:
        -Crear nota (crear)
        -Mostrar tus notas (mostrar)
        -Eliminar nota (eliminar)
        -Salir (salir) 


        """)

        accion = input("¿Que quieres hacer?: ")
        HazEl = notas.acciones.Acciones()
        if accion == "crear":
            HazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            print("Vamos a mostrar ")
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            print("Vamos a eliminar ")
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"Hasta pronto {usuario[1]}")
            exit()

        return None
        