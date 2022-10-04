from mailbox import NoSuchMailboxError


class Alumno:
    def __init__(self,id,nombre,apellido,rut):
        self.id = id
        self.nombre = nombre 
        self.apellido = apellido
        self.rut = rut
