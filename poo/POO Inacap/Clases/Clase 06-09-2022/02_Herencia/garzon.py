from Trabajador import Trabajador
class Garzon(Trabajador):

    def __init__(self, mesasAtendidas, platosRotos):
        self.mesasAtendidas = mesasAtendidas
        self.platosRotos = platosRotos
    
    def tomarPedido(self):
        return ""

    def pedirCuenta(self):
        return 0