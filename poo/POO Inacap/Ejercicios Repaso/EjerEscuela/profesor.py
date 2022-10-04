from persona import Persona

class Profesor(Persona):

    def __init__(self, nombre, apellido, evaluacionDocente):
        self.nombre = nombre
        self.apellido = apellido
        self.evaluacionDocente = evaluacionDocente 