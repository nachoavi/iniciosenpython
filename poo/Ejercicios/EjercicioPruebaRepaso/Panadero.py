from Trabajador import Trabajador
from dataclasses import dataclass

@dataclass
class Panadero(Trabajador):
    diasTrabajados: int
    valorDiaTrabajo: int

    def Trabajar(self):
        if self.estadoSalud == True:
            self.diasTrabajados += 1
        else:
            print("El trabajador está enfermo, no trabajó")

    def pagarSueldo(self):
        if self.diasTrabajados > 0:
            self.capital = self.diasTrabajados * self.valorDiaTrabajo
            self.diasTrabajados = 0
        else:
            print("No hay dias trabajados para pagar sueldo")

    def despedir(self,añosAntiguedad):
        pass

    def infoPanadero(self):
        print(self.nombre,self.apellido)
