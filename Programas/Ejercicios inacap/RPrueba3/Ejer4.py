p=0
i=0
c=0
for x in range(0,5):
    num=int(input("Ingrese un numero entero: "))
    if num %2==0:
        p=p+1
        
    elif num %2==1:
        i=i+1
        
    elif num==0:
        c=c+1

print("La cantidad de numeros pares es: ",p)
print("La cantidad de impares es: ",i)
print("La cantidad de ceros es: ",c)
        