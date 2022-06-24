can=float(input("Ingrese la cantidad a invertir "))
ia=float(input("Ingrese el intéres anual: "))
year=int(input("Ingrese la cantidad de años de la inversión: "))

for x in range(year):
    can *= 1 + ia / 100
    print("Capital tras " + str(x+1) + " años: " + str(round(can, 2)))

