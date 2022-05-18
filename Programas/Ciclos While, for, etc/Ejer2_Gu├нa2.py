n1 = None
n2 = None
n3 = None

while n1 > 7 or n1 < 1:
    n1 = input("Ingrese nota 1: ")
    if n1 >= 1 and n1 <=7:
        while n2 > 7 or n2 < 1:
            n2 = float(input("Ingrese nota 2: "))
            if n2 >= 1 and n2 <=7:
                while n3 > 7 or n3 < 1:
                    n3 = float(input("Ingrese nota 3: "))
                    if n3 >= 1 and n3 <= 7:
                        sum = n1 + n2 + n3
                        prom = sum / 3
                        print("El promedio de notas es: ", prom)

                            