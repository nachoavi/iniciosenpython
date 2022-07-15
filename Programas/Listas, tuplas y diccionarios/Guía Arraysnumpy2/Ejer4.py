import numpy as np
import math as math

num=np.array([None]*5)
cuadrado=np.array([None]*5)
raiz=np.array([None]*5)

print("LLenado primer vector")
for i in range(0,num.size):
    num[i]=int(input(f"Ingrese el numero {i+1}: "))

for i in range(0,cuadrado.size):
    cuadrado[i]=num[i]**2

for i in range(0,raiz.size):
    if num[i]!=0:
        raiz[i]=math.sqrt(num[i])
    elif num[i]==0:
        print("La opción ingresada es invalida, ingrese un numero mayor a 0")

for i in range(0,num.size):
    print(f"Numero {i+1} es ",num[i],", su cuadrado es ",cuadrado[i],"y su raíz es ",raiz[i])
