#Polimorfismo con Herencia

class Aves:
    def volar(self):
        print("La mayoria de las aves pueden volar pero otras no")

class Aguila(Aves):
    def volar(self):
        print("La aguila por ejemplo si puede volar")

class Avestruz(Aves):
    def volar(self):
        print("La avestruz no puede volar")

obj_aves = Aves()
obj_aves.volar()

obj_aguila = Aguila()
obj_aguila.volar()

obj_avestruz = Avestruz()
obj_avestruz.volar()

#Como conclución podemos decir que el metodo volar tiene diferente sentido en las diferentes clases aunque se llamen igual
#Que se llamen igual no quiere decir que hagan lo mismo.