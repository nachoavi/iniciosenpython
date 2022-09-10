from AnimalesPadre import Animales
from random import randint

class Cocodrilo(Animales):
    def __init__(self, nombre, raza, edad, peso, clase, distancia,cantDientes):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.clase = clase
        self.distancia = distancia
        self.dientes = cantDientes
    
    def morderPiedra(self,morder):
        if morder == "1":
            dientesRotos = randint(0,5)
            self.dientes = self.dientes - dientesRotos
            print(f"{self.nombre} mordió una piedra, ha perdido {dientesRotos} dientes.\nLe quedan: ",self.dientes,"dientes...")

        elif morder == "2":
            print(f"Sabia decisión {self.nombre} ha salvado sus dientes")
        
    