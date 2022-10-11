import numpy as np
from productos import Productos
from productosFrescos import ProductosFrescos
from ProductosCongelados import ProductosCongelados
from ProductosRefrigerados import ProductosRefrigerados


def ingresarFrescos(cantProductos):
    arrayFrescos = []
    anyoCaducidad = int(input("Ingrese el año de caducidad\n> "))
    nroLote = int(input("Ingrese el numero de lote\n> "))
    paisOrigen = input("Ingrese el pais de origen: ")
    sumador = 0
    while sumador != cantProductos:
        productoFresco1 = ProductosFrescos(anyoCaducidad,nroLote,paisOrigen)
        arrayFrescos.append(productoFresco1)
        sumador +=1
    for i in arrayFrescos:
        print(i.nroLote)


def ingresarRefrigerados(cantProductos):
    pass

    
def ingresarCongelados(cantProductos):
    pass



def menu():
    x=None
    while x != 0:
        print("MENU DE PRODUCTOS\n1)Productos Frescos\n2)Productos Refrigerados\n3)Productos Congelados\n0)Salir")
        eleccionProducto = int(input("Elija el tipo de producto que ingresara\n> "))
        if eleccionProducto == 1:
            cantProductos = int(input("Ingrese la cantidad de productos a ingresar\n> "))
            ingresarFrescos(cantProductos)
        elif eleccionProducto == 2:
            cantProductos = int(input("Ingrese la cantidad de productos a ingresar\n> "))
            ingresarRefrigerados(cantProductos)
        elif eleccionProducto == 3:
            cantProductos = int(input("Ingrese la cantidad de productos a ingresar\n> "))
            ingresarCongelados(cantProductos)
        else:
            exit()

menu()