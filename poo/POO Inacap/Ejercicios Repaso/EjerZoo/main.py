from animales import Animales
from canguro import Canguro
from leon import Leon
from zebra import Zebra
from cocodrilo import Cocodrilo
from jirafa import Jirafa

listaAnimalCanguros = []
listaAnimalCocodrilos = []
listaAnimalZebras = []
listaAnimalJirafas = []
listaAnimalLeon = []


def registrarAnimal():
    print("Menu de registro\n¿Que animal desea registrar?\n1)Canguro\n2)Cocodrilo\n3)Leon\n4)Zebra\n5)Jirafa")
    op = int(input("> "))
    if op == 1:
        numID = int(input("Ingrese la ID: "))
        nombre = input("Ingrese el nombre: ")
        sexo = input("Ingrese sexo (Macho/Hembra): ")
        edad = int(input("Ingrese edad en años: "))
        especie = input("Ingrese su especie: ")
        nuevoCanguro = Canguro(numID, nombre, sexo, edad, especie)
        listaAnimalCanguros.append(nuevoCanguro)
    elif op == 2:
        numID = int(input("Ingrese la ID: "))
        nombre = input("Ingrese el nombre: ")
        sexo = input("Ingrese sexo (Macho/Hembra): ")
        edad = int(input("Ingrese edad en años: "))
        especie = input("Ingrese su especie: ")
        numDientes = int(input("Cantidad de dientes: "))
        nuevoCocodrilo = Cocodrilo(numID, nombre, sexo, edad, especie, numDientes)
        listaAnimalCocodrilos.append(nuevoCocodrilo)

    elif op == 3:
        numID = int(input("Ingrese la ID: "))
        nombre = input("Ingrese el nombre: ")
        sexo = input("Ingrese sexo (Macho/Hembra): ")
        edad = int(input("Ingrese edad en años: "))
        especie = input("Ingrese su especie: ")
        alfa = (input("Es alfa? (Si/No): "))
        nuevoLeon = Leon(numID, nombre, sexo, edad, especie, alfa)
        listaAnimalLeon.append(nuevoLeon)

    elif op == 4:
        numID = int(input("Ingrese la ID: "))
        nombre = input("Ingrese el nombre: ")
        sexo = input("Ingrese sexo (Macho/Hembra): ")
        edad = int(input("Ingrese edad en años: "))
        especie = input("Ingrese su especie: ")
        numeroRayasNegras = int(input("Numero de rayas negras: "))
        nuevaZebra = Zebra(numID, nombre, sexo, edad, especie, numeroRayasNegras)
        listaAnimalZebras.append(object)
    
    elif op == 5:
        numID = int(input("Ingrese la ID: "))
        nombre = input("Ingrese el nombre: ")
        sexo = input("Ingrese sexo (Macho/Hembra): ")
        edad = int(input("Ingrese edad en años: "))
        especie = input("Ingrese su especie: ")
        tamaño = int(input("Ingrese tamaño en metros: "))
        nuevaJirafa = Jirafa(numID, nombre, sexo, edad, especie, tamaño)
        listaAnimalJirafas.append(nuevaJirafa)

def listarAnimales():
    print("Listar por: 1) Tipo\n 2)Especie\n 3)Todos")
    op = int(input("> "))
    if op == 1:
        print("1)Canguros\n2)Cocodrilos\n3)Zebras\n4)Jirafas\n5)Leones")
        op = int(input("> "))
        if op == 1:
            for i in listaAnimalCanguros:
                print(f"ID: {i.numID}\nNombre: {i.nombre}\nSexo: {i.sexo}\n")

def menu():
    x = 1
    while x !=0:
        print("Registro de Animales\n1) Registrar Animal\n2) Listar Animales\n3)Buscar Animal\n0) Salir")
        op = int(input("> "))
        if op == 1:
            registrarAnimal()
        elif op == 2:
            listarAnimales()
        elif op == 3:
            buscarAnimal()
        elif op == 0:
            print("Gracias por usar")
            x = 0

menu()
