print("Elije una opción:")

opcion = None
while opcion != "A" and opcion != "B" and opcion != "C":
    opcion = str(input("A, B o C: "))
    if opcion == "A":
        print("Elejiste A")
    elif opcion == "B":
        print("Elejiste B")
    elif opcion == "C":
        print("Elejiste C")

print("Gracias por participar")