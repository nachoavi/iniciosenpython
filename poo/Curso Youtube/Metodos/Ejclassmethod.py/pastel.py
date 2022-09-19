# Metodo de Clase 

class Pastel:
    def __init__(self,ingredientes):
        self.ingredientes = ingredientes #en lugar de crear los atributos de la manera tradicional usaremos @clasmethod


    def __repr__(self): #Nos sirve para trabajar con diferentes valores depositados en un solo atributo
        return f'pastel({self.ingredientes !r})' #colocamos el atributo principal en un f string  
                                        #usamos !r para especificar que la linea se ejecute con el metodo repr

    @classmethod
    def Pastel_Chocolate(cls): #en un metodo de clase utilizaremos cls para inicializar el metodo
        return cls(['harina','leche','chocolate'])
    
    @classmethod
    def Pastel_Vainilla(cls):
        return cls(['harina','leche','vainilla'])

print(Pastel.Pastel_Vainilla())