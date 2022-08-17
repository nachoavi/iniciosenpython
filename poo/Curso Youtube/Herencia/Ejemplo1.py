class Pokemon:
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    def descripción(self):
        return "{} es de tipo {} ".format(self.nombre,self.tipo)

class Pikachu (Pokemon):
    def ataque(self,tipoataque):
        return "{}, su tipo de ataque es: {} ".format(self.nombre,tipoataque)

class Charmander (Pokemon):
    def ataque(self,tipoataque):
        return "{}, su tipo de ataque es: {} ".format(self.nombre,tipoataque)

class Squirtle (Pokemon):
    def ataque(self,tipoataque):
        return "{}, su tipo de ataque es: {} ".format(self.nombre,tipoataque)

nuevo_pokemon = Pikachu("Pepito" , "electrico")
print(nuevo_pokemon.descripción())
print(nuevo_pokemon.ataque("placaje"))