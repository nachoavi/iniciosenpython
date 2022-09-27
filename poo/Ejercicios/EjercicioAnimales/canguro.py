from animales import Animales


class Canguro(Animales):
    def __init__(self, nombre, raza, edad, peso, clase, distancia,golpesDados):
        super().__init__(nombre, raza, edad, peso, clase, distancia)
        self.golpesDados = 0
        

    def golpear(self,golpes):
        pass
