def valorFuturo(capital,tipo,n):
    for i in range(n):
        print(f"Año {i}: ",capital*(1+tipo/100)**(i+1))
    return


def valorActual(va,tipo,n):
    for i in range(n):
        print(f"Año {-i}",capital/(1+tipo/100)**(i+1))



capital=float(input("Ingrese la inversión inicial: "))
tipo=float(input("Ingrese el tipo de interes: "))
n=int(input("Ingrese la cantidad de años: "))

print("Valor Futuro")
valorFuturo(capital, tipo, n)
print("Valor Actual")
valorActual(capital, tipo, n)