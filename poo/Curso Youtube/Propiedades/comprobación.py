class Trabajadores:
    def __init__(self,nombre,apellido,salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

trabajador1 = Trabajadores("Pepe","Takovic",2000)
trabajador1.nombre = "Victor"

print(trabajador1.nombre)