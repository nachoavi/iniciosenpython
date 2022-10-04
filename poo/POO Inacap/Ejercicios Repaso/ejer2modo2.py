
from calculadora import sumar,restar,multiplicar,dividir

opcion = None

while opcion != 5:
    print("Calculadora")
    print("Ingrese una de las siguentes opciones")
    print("1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.Salir\n")
    opcion = int(input(":"))
    if opcion == 5:
        exit()
    else:
        a=int(input("Ingrese el primer numero: "))
        b=int(input("Ingrese el segundo numero: "))
        
    resultado = None

    if opcion == 1:
        resultado = sumar(a,b)

    elif opcion == 2:
        resultado = restar(a,b)
  
    elif opcion == 3:
        resultado = multiplicar(a,b)

    elif opcion == 4:
        resultado = dividir(a,b)

    print("El resultado es: ",resultado,"\n")

