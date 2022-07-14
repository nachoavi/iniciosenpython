##crear un programa que permita ingresar 5
#n° por teclado en un vector.  Después visualizar
#solo los pares. Luego visualizar solo ceros y
#visualizar todos los impares-
import numpy as np 



num=[]
e=[]
x=[]
cero=[]
for i in range (0,5):
    num.append(int(input("Ingrese un numero entero: ")))
for i in num:
    if i %2==0:
        e.append(i)
    elif i %2!=0:
        x.append(i)
    elif i == 0:
        cero.append(i)

print("Los numeros pares son: ",e)
print("Los numero impares son: ",i)
print("Los ceros son: ",cero)