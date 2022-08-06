ci=int(input("Ingrese la cantidad a invertir: "))
interesanual=float(input("Ingrese el interés anual: "))
años=int(input("Ingrese la cantidad de años de inversión: "))

print("El capital obtenido es: ",round(ci*(interesanual/100+1)**años,2))

