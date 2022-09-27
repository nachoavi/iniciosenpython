class Persona:
    def __init__(self,nombre,edad,rut):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut
    
    def mostrar(self):
        print(f"Nombre:{self.nombre}\nEdad:{self.edad}\nRut:{self.rut}")
    
    def esMayorDeEdad(self):
        if self.edad > 18:
            print("Es mayor de edad, se puede tomar un cubata")

class Estudiante(Persona):
    def __init__(self, nombre, edad, rut, escuela):
        self.escuela = escuela

estudiante = Estudiante("Luis", 19, "222-2", "Escuela 2")

print(estudiante.escuela)
        
