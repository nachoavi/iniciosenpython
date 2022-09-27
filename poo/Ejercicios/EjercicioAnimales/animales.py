

class Animales:
    def __init__(self,nombre,raza,edad,peso,clase,distancia):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.clase = clase
        self.distancia = distancia

    def avanzar(self,kms_avanzados):
        if kms_avanzados > 10:
            self.peso -= 1
        self.distancia += kms_avanzados    

    def comer(self,kg_comidos):
        if kg_comidos > self.peso * 0.05:
            print(f"{self.nombre} vomitó")
            kg_comidos -= kg_comidos * 0.90
        self.peso += kg_comidos