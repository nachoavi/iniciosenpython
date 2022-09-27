from producto import Productos

class ProductosRefrigerados(Productos):
    def __init__(self, anyoCaducidad, nroLote,codigo):
        self.codigo = codigo
        super().__init__(anyoCaducidad, nroLote)


