from xmlrpc.client import Boolean
from Trabajador import Trabajador

class Cocinero(Trabajador):
    def __init__(self,PlatosListos,PlatosMalos):
        self.PlatosListos = PlatosListos
        self.PlatosMalos = PlatosMalos
    
    def PrepararPlatos(self):
        return True
    
    def PicarFreir(self):
        return ""

    

