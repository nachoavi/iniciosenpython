from Trabajador import Trabajador
from alumno import Alumno
from cocinero import Cocinero
from garzon import Garzon
'''
x = 0
carrera = "Informática"
numeros = [1, 5, 7, 8, 43, 21, 10]

t = Trabajador()
t.nombre = "Juan"
t.apellido = "Pérez"
t.id = 1
t.rut = "111111-1"
t.telefono = 99995555

t2 = Trabajador()
t2.nombre = "Raquel"
t2.apellido = "Cisternas"
t2.id = 2
t2.rut = "22222-2"
t2.telefono = 99998888

print("NOMBRE TRABAJADOR 1:", t.nombre)
print("NOMBRE TRABAJADOR 2:", t2.nombre)

alu = Alumno(1, 'Franco', 'Cea', 20)
print("ID: " + str(alu.id) + ", Nombre: " + alu.nombre + ", Apellido: " + alu.apellido)
'''
g = Garzon()
g.nombre = "Pedro"
g.sumarDiaTrabajado()

c = Cocinero()
c.nombre = "Fernanda"
c.sumarDiaTrabajado()
c.sumarDiaTrabajado()

print("Garzón: " + g.nombre + ", Días Trabajados: " + str(g.diasTrabajados))
print("Cocinera:", c.nombre + ", Días Trabajados: " + str(c.diasTrabajados))