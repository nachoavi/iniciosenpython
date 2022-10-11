from productos import Productos

class ProductosFrescos(Productos):
    def __init__(self, anyoCaducidad, nroLote,paisOrigen):
        self.paisOrigen = paisOrigen
        super().__init__(anyoCaducidad, nroLote)


    def Caducidad(self):
        if self.anyoCaducidad < 2022:
            return True

            