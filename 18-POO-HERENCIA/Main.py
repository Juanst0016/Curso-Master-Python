import Clases

persona = Clases.Persona()

persona.setnombre("Juan")
persona.setapellido("Torres")
persona.setaltura(1.70)
persona.setedad(22)

print(f"La persona es {persona.getnombre(), persona.getapellido()}")
print(persona.hablar())

print("-------------------------------------")

informatico = Clases.informatico()
informatico.setnombre("Juan")
informatico.setapellido("Torres2")
informatico.setedad(23)

print(f"El informatico es {informatico.getnombre(), informatico.getapellido()}")
print(informatico.getlenguajes())

print("--------------------")

tecnico = Clases.tecnicoRedes()
tecnico.setnombre("Juan")

print(tecnico.auditarRedes, tecnico.getnombre(), tecnico.getlenguajes())