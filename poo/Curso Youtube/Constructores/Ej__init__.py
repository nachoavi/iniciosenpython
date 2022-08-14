class Persona:
    pass
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def descripcion(self):
        return "{} tiene {} años".format(self.nombre,self.edad)
    
    def comentario(self,frase):
        return "{} dice: {}".format(self.nombre,frase)

programador = Persona("Jose",26)
print(programador.descripcion())
print(programador.comentario("Hola mundo"))