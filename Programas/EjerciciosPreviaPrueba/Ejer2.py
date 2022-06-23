def promedio():
    s=0
    for x in range(1,4):
        n=float(input(f"Ingrese el numero {x}: "))
        s=s+n
    prom=s/3
    return prom

print("El resultado es ", promedio())

