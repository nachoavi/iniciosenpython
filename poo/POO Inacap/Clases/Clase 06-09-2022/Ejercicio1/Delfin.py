from random import randint
from AnimalesPadre import Animales

class Delfin(Animales):
    def __init__(self, nombre, raza, edad, peso, clase, distancia,saltos):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.clase = clase
        self.distancia = distancia
        self.saltos = saltos

    def saltar(self,saltar):
        if saltar > 1:
            print(f"{self.nombre} no puede hacer mas de un salto a la vez")
        else:
            suerte = randint(0, 10)
            if suerte >= 5:
                print(f"{self.nombre} ha logrado saltar, al fín es libre")
            else:
                print(f"{self.nombre} no ha logrado saltar, sigue cautivo :c")
            self.saltos += 1
        print(f"La cantidad de saltos de {self.nombre} es de: ",self.saltos)

        