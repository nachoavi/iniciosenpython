from productos import Productos

class ProductosCongelados(Productos):
    def __init__(self, anyoCaducidad, nroLote,temperatura):
        self.temperatura = temperatura
        super().__init__(anyoCaducidad, nroLote)

    def comprobarTemperatura(self):
        if self.temperatura < -10:
            return True

    def descongelarProducto(self):
        self.temperatura -= self.temperatura / 2

        