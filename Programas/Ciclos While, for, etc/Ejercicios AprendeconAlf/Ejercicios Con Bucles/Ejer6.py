n=int(input("Ingrese un numero: "))
for x in range(n):
    for j in range(x+1):
        print("*", end="")
    print("")