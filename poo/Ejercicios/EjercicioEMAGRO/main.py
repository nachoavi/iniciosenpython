from productos import Productos
from frescos import ProductosFrescos
from refrigerados import ProductosRefrigerados
from congelados import ProductosCongelados

listaFresco = []
listaRefrigerados = []
listaCongelados = []


def ingresarFrescos(cantProductos):
    anyoCaducidad = int(input("Ingrese el año de caducidad: "))
    nroLote = int(input("\nIngrese el numero de lote: "))
    paisOrigen = input("\nIngrese el pais de origen: ")
    x = 0
    while x != cantProductos:
        productoFresco = ProductosFrescos(anyoCaducidad, nroLote, paisOrigen)
        listaFresco.append(productoFresco)
        x += 1

def ingresarCongelado(cantProductos):
    anyoCaducidad = int(input("Ingrese el año de caducidad: "))
    nroLote = int(input("\nIngrese el numero de lote: "))
    temperatura = float(input("\nIngrese la temperatura de congelamiento: "))
    x = 0
    while x != cantProductos:
        productoCongelado = ProductosCongelados(anyoCaducidad, nroLote, temperatura)
        listaCongelados.append(productoCongelado)
        x += 1

def ingresarRefrigerados(cantProductos):
    anyoCaducidad = int(input("Ingrese el año de caducidad: "))
    nroLote = int(input("\nIngrese el numero de lote: "))
    codigo = int(input("\nIngrese el codigo del primer producto: "))
    x = 0
    while x != cantProductos:
        ProductoRefrigerado = ProductosRefrigerados(anyoCaducidad, nroLote, codigo+x)
        listaRefrigerados.append(ProductoRefrigerado)
        x += 1


def salir():
    pass

def menuIngreso():
    x = None
    while x != 0:
        print("Menu de ingreso de productos\nSeleccione el tipo de producto\n")
        opProducto = int(input("1.Fresco\n2.Refrigerado\n3.Congelado\n0.Salir\n> "))
        cantProductos = int(input("Ingrese la cantidad de productos que ingresará\n> "))
        if opProducto == 1:
            ingresarFrescos(cantProductos)
        elif opProducto == 2:
            ingresarRefrigerados(cantProductos)
        elif opProducto == 3:
            ingresarCongelados(cantProductos)
        elif opProducto == 0:
            exit()

def menuListar():
    pass

menuIngreso()
