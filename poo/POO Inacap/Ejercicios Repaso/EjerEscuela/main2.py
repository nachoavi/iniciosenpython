listaNumeros = []

opcion = -1
while opcion != 0:
    print("1. Ingresar un número.. ")
    print("2. Ver números ingresados..")
    print("0. Salir")
    opcion = int(input())

    if opcion == 1:
        num = int(input("Ingrese un número: "))
        listaNumeros.append(num)
    elif opcion == 2:
        for numero in listaNumeros:
            print(numero)
    elif opcion == 0:
        pass
    else:
        print("Opción no válida")