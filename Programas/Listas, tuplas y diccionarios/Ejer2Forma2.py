#crear un programa que permita ingresar 5
#n° por teclado en un vector.  Después visualizar
#solo los pares. Luego visualizar solo ceros y
#visualizar todos los impares-

import numpy as np

numero=np.array([None]*5)
for i in range(0,numero.size):
    numero[i]=int(input("Ingrese un numero: "))

for i in range(0,numero.size):
    if numero[i] %2==0 and numero[i] !=0:
        print("Los pares son: ", numero[i])
for i in range(0,numero.size):
    if numero[i] %2==1 or numero[i] == 0:
        print("Los numeros impare o iguales a cero son: ",numero[i])
        
