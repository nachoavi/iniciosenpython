from animales import Animales

class Delfin(Animales):
    def __init__(self, nombre, raza, edad, peso, clase, distancia,piruetas):
        super().__init__(nombre, raza, edad, peso, clase, distancia)
        self.piruetas = 0

    def hacerPirueta(self,pirueta):
        pass