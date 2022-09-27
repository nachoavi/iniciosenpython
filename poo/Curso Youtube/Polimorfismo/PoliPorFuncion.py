#Polimorfismo por función

class Tomate:           
    def tipo(self):
        print("Vegetal") #Creamos la clase Tomate con los metodos tipo y color
    def color(self):        
        print("Rojo")

class Manzana:
    def tipo(self):
        print("Fruta") #Creamos la clase Manzana tambien con los metodos tipo y color
    def color(self):
        print("Verde")

def funcion(objeto): #Creamos una función que nos permitira acceder a ambos metodos antes creados
    objeto.tipo()
    objeto.color()

ortaliza1 = Tomate() #Creamos el objeto ortaliza1 que será una instancia de Tomate()
funcion(ortaliza1) #Llamamos a la función llamada función y le pasamos en parametros el objeto antes creado
                    #Esto nos mostrara por pantalla los metodos que tiene.

 