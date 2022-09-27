#Ejemplo de polimorfismo

class Animales:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def tipo_animal(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        print("Animal salvaje")

class Gato(Animales):
    def tipo_animal(self):
        print("Animal domestico")

animal1 = Gato('Arya',18)
animal1.tipo_animal()

animal2 = Leon("Mufasa", 20)
animal2.tipo_animal()