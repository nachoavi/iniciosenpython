##crear un programa que permita ingresar 5
#n° por teclado en un vector.  Después visualizar
#solo los pares. Luego visualizar solo ceros y
#visualizar todos los impares-
import numpy as np 

num=np.array([None]*5)

for i in range(0,num.size):
    num[i]=int(input("Ingrese un numero: "))

for i in range(0,num.size):
    if num[i] %2==0 and num[i] !=0:
        print("Los numeros pares son: ",num[i])

for i in range(0,num.size):
    if num[i] %2==1:
        print("Los numeros impares son:  ",num[i])

for i in range(0,num.size):
    if num[i] == 0:
        print("Los numeros ceros son: ",num[i])
