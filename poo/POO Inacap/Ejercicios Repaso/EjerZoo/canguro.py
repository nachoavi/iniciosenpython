from animales import Animales

class Canguro(Animales):
    def __init__(self,numID,nombre, sexo, edad, especie):
        self.numID = numID
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad
        self.especie = especie