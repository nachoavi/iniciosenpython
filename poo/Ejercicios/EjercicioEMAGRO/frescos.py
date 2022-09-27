from productos import Productos


class ProductosFrescos(Productos):
    def __init__(self, anyoCaducidad, nroLote,paisOrigen):
        self.paisOrigen = paisOrigen
        super().__init__(anyoCaducidad, nroLote)
    
    def comprobarVencimiento(self,añoActual):
        if añoActual > self.anyoCaducidad:
            print("El producto esta vencido")




