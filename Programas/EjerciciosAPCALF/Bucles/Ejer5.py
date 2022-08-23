cantidad = float(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese el interes porcentual anual: "))
años = int(input("Ingrese la cantidad de años: "))

for i in range(años):
    cantidad *= 1 + interes / 100
    print("Capital tras ", i+1, "años: ", round(cantidad,2))