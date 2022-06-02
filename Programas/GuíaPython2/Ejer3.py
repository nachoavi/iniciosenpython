from re import S


x=1
while x==1:
    n=int(input("Ingrese un numero: "))
    n*=4
    n/=2
    print(n)
    x=x-1
    re=input("Desea ingresar un nuevo numero?[S/N]: ")
    if re =="S":
        x=x+1