

class Trabajador:
    def __init__(self,nombre,apellido,estadoSalud,capital):
        self.nombre = nombre
        self.apellido = apellido
        self.estadoSalud = estadoSalud
        self.capital = capital


    def info(self):
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEstado de Salud: {self.estadoSalud}\n Capital: {self.capital}")
        


    def enfermar(self):
        self.estadoSalud = False

    def recuperarse(self):
        if self.estadoSalud == False:
            self.estadoSalud = True
            print("El trabajador se ha recuperado")
        else:
            print("No es necesario realizar una recuperación")


