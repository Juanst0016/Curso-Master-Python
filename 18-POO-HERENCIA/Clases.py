"""
ES LA POSIBILIDAD DE COMPARTIR ATRIBUTOS Y METODOS ENTRE CLASES 
Y QUE LAS CLASES HIJAS LA HEREDEN 

"""

class Persona:
    """
    nombre 
    apellido
    altura
    edad
    """

    def getnombre(self):
        return self.nombre 

    def getapellido(self):
        return self.apellido

    def getaltura(self):
        return self.altura

    def getedad(self):
        return self.edad

    def setnombre(self, nombre):
        self.nombre = nombre 

    def setapellido(self, apellido):
        self.apellido = apellido

    def setaltura(self,altura):
        self.altura = altura

    def setedad(self, edad):
        self.edad = edad 

    def hablar(self):
        return "Estoy hablando "

    def caminar(self):
        return "Estoy caminando "

    def dormir(self):
        return "Estoy durmiendo "

class informatico(Persona):
    """
    lenguajes 
    experencia
    """

    def __init__(self):
        self.lenguajes = "HTML, CSS, JS, PHP"
        self.experiencia = 5

    def getlenguajes(self):
        return self.lenguajes

    def aprenderlenguajes(self, lenguajes):
        self.lenguajes= lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando "

    def repararPc(self):
        return "He reparado tu ordenador "

class tecnicoRedes(informatico):
    def __init__(self):
        super().__init__() #HEREDA LAS COSAS DE LAS CLASE QUE NO ES PADRE O EN SU CASA LLAMA A SU INIT 
        self.auditarRedes = "Experto"
        self.experienciaRedes = 15

    def auditoria(self):
        return "Estoy auditando una red"
    