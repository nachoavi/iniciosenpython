lote=[]
for i in range(7):
    lote.append(int(input(f"Ingrese el numero {i+1}: ")))
lote.sort()
print("Los numeros ganadores son: "+ str(lote))