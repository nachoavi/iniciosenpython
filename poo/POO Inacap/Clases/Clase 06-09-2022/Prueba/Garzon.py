from Trabajador import Trabajador

class Garzon(Trabajador):
    def __init__(self,mesasAtendidas,PlatosRotos):
        self.mesasAtendidas = mesasAtendidas
        self.PlatosRotos = PlatosRotos
    
    def __init__(self):
        self.tomarpedido = ""
        self.pedircuenta = 0

