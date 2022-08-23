num=int(input("Ingrese un numero entero positivo: "))

for x in range(num+1):
    if x %2 == 1:
        print(x,end=",")