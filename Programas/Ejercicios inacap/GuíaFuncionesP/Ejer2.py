def promedio():
    s=0
    for x in range(1,4):
        n=float(input(f"Ingrese el numero {x}: "))
        s+=n
    prom=s/3
    return prom


resul=promedio()
print("El promedio es ", resul)

   
