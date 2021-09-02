"""
DICCIONARIO:
ES UN TIPO DE DATO QUE ALMACENA UN CONJUNTO DE DATOS.
EN FORMATO CLAVE > VALOR.
ES PARECIDO A UN ARRAY ASOCIATIVO O UN OBJETO JSON  

"""
person = {
    "nombre":"Juan",
    "Apellido": "torres",
    "web":"Juantorres.es"
}
print(person["Apellido"])

#lISTA CON DICCIONARIOS 

contactos = [
    {
    'nombre': 'Agus',
    'email': 'agus@gmail.com'
    },
    {
        'nombre':'juan',
        'email':'juan@gmail.com'
    }
]

contactos[1]["nombre"] = "juancito"
print(contactos[1])

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"email de contacto: {contacto['email']}")
    print("--------------------------------")