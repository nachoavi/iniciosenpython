sum = 0
n = 1
while n <= 3:
    n1 = float(input("Ingrese una nota: "))
    if n1 <= 7.0 and n1 >= 1.0:
        sum = sum + n1
        n = n+1
        print("Nota registrada exitosamente")
    else:
        print("Fuera de rango permitido")
prom=sum/3
print("El promedio es: ",prom)
