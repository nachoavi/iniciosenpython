from dataclasses import dataclass

@dataclass
class Estudiantes:
    nombre: str
    apellido: str
    edad: int

estudiante1 = Estudiantes('Alfredo','Santana', 35)

print(estudiante1)