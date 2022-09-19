from Trabajadores import Trabajadores
from dataclasses import dataclass

@dataclass
class Cajero(Trabajadores):
    carrera: str

    def GenerarBoleta():
        pass

    def Pagar():
        pass


