num = int(input("Ingrese un numero entero: "))

for i in range(num):
    for j in range(i+1):
        print("*", end="")
    print("")