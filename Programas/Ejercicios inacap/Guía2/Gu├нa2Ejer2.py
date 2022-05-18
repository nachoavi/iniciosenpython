option = str(input("Desea comenzar a calcular el programa?[S/N] "))

while option == "S" or option == "s":
    n1 = float(input("Ingrese la primera nota: "))
    if n1 < 1.0 or n1 > 7.0:
        print("Fuera de rango")
        quit()
    n2 = float(input("Ingrese la segunda nota: "))
    if n2 < 1.0 or n1 > 7.0:
        print("Fuera de rango")
        quit()
    n3 = float(input("Ingrese la tercera nota: "))
    if n3 < 1.0 or n3 > 7.0:
        print("Fuera de rango")
        quit()
    prom = (n1 + n2 + n3) / 3
    print("El promedio es: ",prom)
    option = str(input("\nDesea calcular otro promedio?[S/N]: "))




