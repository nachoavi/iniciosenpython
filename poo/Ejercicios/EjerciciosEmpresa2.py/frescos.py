from producto import Productos


class ProductosFrescos(Productos):
    def __init__(self, anyoCaducidad, nroLote,paisOrigen):
        self.paisOrigen = paisOrigen
        super().__init__(anyoCaducidad, nroLote)

    def verificarCaducidad(self):
        return self.anyoCaducidad > 2022








