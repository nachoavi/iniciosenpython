print("Calculadora")
print("Ingrese una de las siguentes opciones")
print("1.Sumas\n2.Restar\n3.Multiplicar\n4.Dividir\n")
opcion = int(input(": "))

def sumar(a,b):
    resultado = a + b
    return resultado

def restar(a,b):
    resultado = a - b
    return resultado 

def multiplicar(a,b):
    resultado = a * b
    return resultado 

def dividir(a,b):
    resultado = a / b
    return resultado



if opcion == 1:
    a = int(input("Ingrese numero 1: "))
    b = int(input("Ingrese numero 2: "))
    print(sumar(a,b))

elif opcion == 2:
    a = int(input("Ingrese numero 1: "))
    b = int(input("Ingrese numero 2: "))
    print(restar(a,b))

elif opcion == 3:
    a = int(input("Ingrese numero 1: "))
    b = int(input("Ingrese numero 2: "))
    print(multiplicar(a,b))

elif opcion == 4:
    a = int(input("Ingrese numero 1: "))
    b = int(input("Ingrese numero 2: "))
    print(dividir(a,b))

