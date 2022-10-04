from Trabajador import Trabajador

class Panadero(Trabajador):
    def __init__(self, nombre, apellido, estadoSalud, capital,diasTrabajados,valorDiaTrabajado):
        self.diasTrabajados = diasTrabajados
        self.valorDiaTrabajado = valorDiaTrabajado
        super().__init__(nombre, apellido, estadoSalud, capital)

    def trabajar(self):
        if self.estadoSalud == True:
            self.diasTrabajados += 1
        else:
            return False

    def pagarSueldo(self):
        if self.diasTrabajados > 0:
            self.capital = self.diasTrabajados * self.valorDiaTrabajado
            self.diasTrabajados = 0
        else:
            print("No hay dias trabajados por pagar")

    def despedir(self,añosdeAntiguedad):
        self.valorDiaTrabajado *= 20
        self.valorDiaTrabajado *= añosdeAntiguedad
        self.capital += self.valorDiaTrabajado

    def infoPanadero(self):
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEstado de Salud: {self.estadoSalud}")
        print(f"Capital: {self.capital}\nDias Trabajados: {self.diasTrabajados}\nValor dia trabajado: {self.valorDiaTrabajado}")