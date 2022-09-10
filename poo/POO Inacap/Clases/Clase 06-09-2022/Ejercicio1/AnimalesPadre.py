
class Animales:
    def __init__(self,nombre,raza,edad,peso,clase,distancia):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.clase = clase
        self.distancia = distancia
    
    def avanzar(self,kmavanzados):
        self.distancia = self.distancia + kmavanzados
        if kmavanzados > 10:
            self.peso = self.peso - 1
        print(f"{self.nombre} lleva recorrido: ",self.distancia)
        print(f"{self.nombre}  pesa: ",self.peso)

    def comer(self,kilogramosingeridos):
        if kilogramosingeridos > (self.peso*5)/100:
            print(f"{self.nombre} vomita")
            self.peso = self.peso + kilogramosingeridos
            self.peso = self.peso - (kilogramosingeridos * 90)/100
            print(f"{self.nombre}  pesa: ",self.peso)
        else:
            self.peso = self.peso + kilogramosingeridos
            print(f"{self.nombre}  pesa: ",self.peso)
