#Un metodo es una función que esta dentro de una clase

#Ejemplo de metodo.

class Matematicas:
    def suma(self):
        self.n1 = 2
        self.n2 = 3
      

s = Matematicas()
s.suma()
print(s.n1 + s.n2)

