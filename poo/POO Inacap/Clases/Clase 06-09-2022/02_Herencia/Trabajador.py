# Dar un nombre a la clase
class Trabajador:
    # crear los atributos de la clase
    id = 0
    nombre = ""
    apellido = ""
    rut = ""
    telefono = 0
    diasTrabajados = 0

    def __init__(self):
        pass

    def sumarDiaTrabajado(self):
        self.diasTrabajados = self.diasTrabajados + 1