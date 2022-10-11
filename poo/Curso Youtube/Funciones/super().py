#La función super() se utiliza para llamar a atributos definidos

class Mamifero:
    def __init__(self,nombre):
        print(nombre,'es un animal de sangre caliente')

class Leon(Mamifero):
    def __init__(self):
        print("El leon un animal de cuatro patas")
        super().__init__('simba') #Super hace referencia a los atributos de la clase padre(Mamifero) y desde la función super le podemos
                                    #asignar un valor


nuevo_leon = Leon()