s=0
sint=0
for x in range(1,6):  
    n=int(input("Ingrese un numero: "))
    if n == 0:
        sint=sint+1
    elif n%2==0:
        s=s+1
    else:
        sint=sint+1
print("La cantidad de numero pares es: ",s)
print("La cantidad de numero impares e iguales a 0 es: ",sint)

    