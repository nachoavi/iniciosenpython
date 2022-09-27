from productos import Productos


class ProductosCongelados(Productos):
    def __init__(self, anyoCaducidad, nroLote,temperatura):
        self.temperatura = temperatura
        super().__init__(anyoCaducidad, nroLote)

    def congelamiento(self):
        if self.temperatura > 10:
            return True

    def descongelar(self):
        self.temperatura -= self.temperatura/2
        print(f"El producto de descongeló y quedó a {self.temperatura}°C")



