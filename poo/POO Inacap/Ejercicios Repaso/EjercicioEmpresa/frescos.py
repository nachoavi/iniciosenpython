from productos import Productos

class ProductoFresco(Productos):
    def __init__(self, anyoCaducidad,nroLote,paisOrigen):
        self.anyoCaducidad = anyoCaducidad
        self.nroLote = nroLote
        self.paisOrigen = paisOrigen
    
    def caducidad(self):
        añoCaducidad = 2010
        if self.anyoCaducidad > añoCaducidad:
            return True

