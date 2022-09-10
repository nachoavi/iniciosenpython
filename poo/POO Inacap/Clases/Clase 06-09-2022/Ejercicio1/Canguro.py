from AnimalesPadre import Animales

class Canguro(Animales):
    def __init__(self, nombre, raza, edad, peso, clase, distancia,estamina):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.clase = clase
        self.distancia = distancia
        self.estamina = estamina

    def darPuñetazo(self, fuerzaPuñetazo):
        if fuerzaPuñetazo > 10:
            print(f"{self.nombre} ha dado un puñetazo fuerte con una fuerza de {fuerzaPuñetazo}")
            self.estamina = self.estamina - fuerzaPuñetazo/2
            print(f"La estamina de {self.nombre} es de: ",self.estamina)
        else:
            print(f"{self.nombre} ha dado un puñetazo debil con una fuerza de {fuerzaPuñetazo}")
         
       
    