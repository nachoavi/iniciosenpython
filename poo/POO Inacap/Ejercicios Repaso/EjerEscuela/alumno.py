from persona import Persona


class Alumno(Persona):

    def __init__(self, nombre, apellido, conocimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.conocimiento = conocimiento 