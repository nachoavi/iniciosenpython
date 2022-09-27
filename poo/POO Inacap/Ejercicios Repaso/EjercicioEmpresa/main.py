from productos import Productos
from congelados import ProductoCongelado
from refrigerados import ProductoRefrigerado
from frescos import ProductoFresco

listaCongelado = []
listaRefrigerado = []
listaFresco = []

def ingresarCongelado():
    pingresados = int(input("Cuantos productos ingresará?\n> "))
    x = 0
    while x != pingresados:
        anyoCaducidad = int(input(f"\nIngrese año de caducidad del producto {x+1}: "))
        nroLote = int(input(f"\nIngrese numero de lote del producto {x+1}: "))
        temperatura = float(input(f"\nIngrese temperatura de congelación del producto {x+1}: "))
        congelado = ProductoCongelado(anyoCaducidad, nroLote, temperatura)
        listaCongelado.append(congelado)
        x += 1

def ingresarFresco():
    pingresados = int(input("Cuantos productos ingresará?\n> "))
    x = 0
    while x != pingresados:
        anyoCaducidad = int(input(f"\nIngrese año de caducidad del producto {x+1}: "))
        nroLote = int(input(f"\nIngrese numero de lote del producto {x+1}: "))
        paisOrigen = input(f"\nIngrese el pais de origen del producto {x+1}: ")
        fresco = ProductoFresco(anyoCaducidad, nroLote, paisOrigen)
        listaFresco.append(fresco)
        x += 1



def ingresarRefrigerado():
    pingresados = int(input("Cuantos productos ingresará?\n> "))
    anyoCaducidad = int(input(f"\nIngrese año de caducidad del producto: "))
    nroLote = int(input(f"\nIngrese numero de lote del producto: "))   
    codigo = int(input(f"\nIngrese el codigo del producto: "))
    x = 0
    while x != pingresados:
        refrigerado = ProductoRefrigerado(anyoCaducidad, nroLote, codigo+x)
        listaFresco.append(refrigerado)
        x += 1
    for i in listaFresco:
        print(f"Caducidad: {i.anyoCaducidad} / Lote: {i.nroLote} / Codigo: {i.codigo}")

def salir():
    print("Gracias por usar!!")
    return 0

def menu():
    x = None
    while x != 0:
        print("Menu de Productos\n1)Ingresar congelado\n2)Ingresar refrigerado\n3)Ingresar fresco\n0)Salir")
        op = int(input("> "))
        if op == 1:
            ingresarCongelado()
        elif op == 2:
            ingresarRefrigerado()
        elif op == 3:
            ingresarFresco()
        elif op == 0:
            x = salir()

op = int(input("Para ingresar al programa pulse 1, para salir 0...\n> "))
if op == 1:
    menu()
elif op == 0:
    print("Vuelva pronto")