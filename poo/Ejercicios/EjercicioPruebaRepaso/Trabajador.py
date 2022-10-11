from dataclasses import dataclass
from xmlrpc.client import Boolean



@dataclass
class Trabajador:
    nombre: str
    apellido: str
    estadoSalud: True
    capital: int

    def enfermar(self):
        self.estadoSalud = False
    
    def recuperarse(self):
        if self.estadoSalud == False:
            self.estadoSalud = True
            print("El trabajador se ha recuperado")
        else:
            print("El trabajador no está enfermo")

