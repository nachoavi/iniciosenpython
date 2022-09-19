from Trabajadores import Trabajadores
from Cocinero import Cocinero
from Garzón import Garzon
from Cajero import Cajero
from random import randint

global trabajadores
trabajadores = []


def registrarTrabajador(a):
    if a == 1:
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        rut = input("Ingrese rut: ")
        telefono = input("Ingrese telefono: ")
        xpCocina = int(input("Ingrese años de xp en cocina: "))
        TrabajadorCocinero = Cocinero(nombre, apellido, rut, telefono, xpCocina)
        trabajadores.append(TrabajadorCocinero)
    elif a == 2:
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        rut = input("Ingrese rut: ")
        telefono = input("Ingrese telefono: ")
        rango = input("Ingrese años de xp en cocina: ")
        TrabajadorGarzón = Garzon(nombre, apellido, rut, telefono, rango)
        trabajadores.append(TrabajadorGarzón)
    elif a == 3:
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        rut = input("Ingrese rut: ")
        telefono = input("Ingrese telefono: ")
        carrera = input("Ingrese años de xp en cocina: ")
        TrabajadorCajero = Cajero(nombre, apellido, rut, telefono, carrera)
        trabajadores.append(TrabajadorCajero)
def listarTrabajador():
    print("Lista de trabajadores")
    for i in trabajadores:
        print(f'Nombre: {i.nombre} Apellido: {i.apellido}',sep="\n")

def buscarTrabajador():
    rut = input("Ingrese el rut del tabajador: ")
    for i in trabajadores:
        if i.rut == rut:
            print(f'Nombre: {i.nombre}\nApellido: {i.apellido}\nTelefono: {i.telefono}')
        else:
            print("Trabajador no existe o el rut es erroneo")

def salir():
    print("Gracias por usar")
    exit()

def menu():
    op = None
    
    while op != salir:
        print("Menú de registro\n1) Registrar Trabajador\n2) Listar Trabajadorer\n3) Buscar Trabajador\n0) Salir")
        op = int(input("> "))

        if op == 1:
            print("Elija cargo\n1) Cocinero\n2) Garzón\n3) Cajero")
            op = int(input("> "))
            registrarTrabajador(op)
        elif op == 2:
            listarTrabajador()
        elif op == 3:
            buscarTrabajador()
        elif op == 0:
            salir()

menu()

