from dataclasses import dataclass
from xmlrpc.client import Boolean

@dataclass
class Trabajador:
    nombre: str
    apellido: str
    estadoSalud: True
    capital: int

trabajador1 = Trabajador("Luis","San Martín",True,80000)

print(trabajador1.nombre)