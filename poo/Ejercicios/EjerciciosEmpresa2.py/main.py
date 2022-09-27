from producto import Productos
from frescos import ProductosFrescos
from congelados import ProductosCongelados
from refrigerados import ProductosRefrigerados

listaFresco = []
listaCongelados = []
listaRefrigerados = []


def ingresarFrescos(cantProductos):
    anyoCaducidad = int(input("Ingrese el año de caducidad: "))
    nroLote = int(input("\nIngrese el numero de lote: "))
    paisOrigen = input("\nIngrese el pais de origen: ")
    x = 0
    while x != cantProductos:
        productoFresco = ProductosFrescos(anyoCaducidad, nroLote, paisOrigen)
        listaFresco.append(productoFresco)
        x += 1   
    for i in listaFresco:
        print(f"Año de caducidad: {i.anyoCaducidad} Nuro de lote: {i.nroLote}\n") 


def ingresarCongelados(cantProductos):
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

def menu():
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
            x = 0


productoCOngelado1 = ProductosCongelados(2022, 12, -20)
productoCOngelado1.descongelar()


















