#Este metodo nos servirá para formatear textos string

class Estudiantes:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f"Hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años"

nuevo_estudiante = Estudiantes("Luis", "San Martín", 22)

print(nuevo_estudiante)