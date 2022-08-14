#Esta función se utiliza cuando queremos eliminar un atributo

class Persona():
    edad = 25
    nombre = "Jose"
    pais = "Suiza"

programador = Persona()

print(programador.edad) #ahora esta
delattr(programador, edad) 
#delattr(obj, name)
print(programador.edad) #ahora no esta
