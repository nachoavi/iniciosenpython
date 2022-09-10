from AnimalesPadre import Animales



class Gallo(Animales):
    def __init__(self, nombre, raza, edad, peso, clase, distancia,intentosdeConquista):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.clase = clase
        self.distancia = distancia
        self.intentosdeConquista = intentosdeConquista

    def conquistarelMundo(self):
        self.intentosdeConquista += 1
        print(f"{self.nombre} no ha logrado conquistar el mundo esta vez")
        if self.intentosdeConquista >= 500:
            print(f"Finalmente, {self.nombre} ha logrado conquistar el mundo")


        

    
