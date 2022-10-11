#getattr sirve para obtener el atributo de nuestra clase

class Persona:
    edad = 22
    nombre = "Luis"

programador = Persona()

print("La edad de",programador.nombre, "es de", programador.edad,"años")

print("La edad de",getattr(programador, "nombre"),"es de",getattr(programador, "edad"),"años")
#getattr = obtener atributo