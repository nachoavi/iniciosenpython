#Crear un ALGORITMO que permita ingresar ticket de entradas (código,
#precio), para un evento. Los ingresos no deben exceder las 10 entradas
#Finalmente mostrar el total recaudado. 
sum=0
x=0
while x <3:
    cod=input("Ingrse el codigo: ")
    pre=int(input("Ingrese el precio: "))
    sum=sum+pre
    x=x+1
print("\nEl total recaudado es: ",sum)