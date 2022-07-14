precios=[50,75,46,22,80,65,8]
for i in range (len(precios)):
    if i == 0:
        mayor=precios[i]
        menor=precios[i]
    elif precios[i] > mayor:
        mayor=precios[i]
    elif precios[i] < menor:
        menor=precios[i]
print("El numero mayor es: ",mayor)
print("El numero menor es: ",menor)
