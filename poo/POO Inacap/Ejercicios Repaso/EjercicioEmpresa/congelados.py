from productos import Productos
from dataclasses import dataclass

class ProductoCongelado(Productos):
    def __init__(self, anyoCaducidad, nroLote,temperatura):
        self.anyoCaducidad = anyoCaducidad
        self.nroLote = nroLote
        self.temperatura = temperatura

    def congelacion(self):
        if  self.temperatura < -10:
            return True

    def descongelar(self):
        if self.temperatura < -10:
            self.temperatura /=2
            print(f'El producto se descongeló y quedó a {self.temperatura} °C')
        elif self.temperatura >= -10:
            print("El producto ya está descongelado")
        

#producto1 = ProductoCongelado(12, 14, -15)
#producto1.descongelar()




