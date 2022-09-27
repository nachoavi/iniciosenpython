from productos import Productos

class ProductoRefrigerado(Productos):
    def __init__(self, anyoCaducidad, nroLote,codigo):
        self.anyoCaducidad = anyoCaducidad
        self.nroLote = nroLote
        self.codigo = codigo

    
    