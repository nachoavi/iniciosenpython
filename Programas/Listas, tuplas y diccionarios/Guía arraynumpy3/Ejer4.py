import numpy as np
import math as math

num=np.array([None]*5)
cuadrado=np.array([None]*5)
raiz=np.array([None]*5)

for i in range(0,num.size):
    num[i]=int(input(f"Ingrese numero {i+1}: "))

for i in range(0,cuadrado.size):
    cuadrado[i]=num[i]**2

for i in range(0,raiz.size):
    raiz[i]=math.sqrt(num[i])

for i in range(0,num.size):
    print(f"Numero {i+1} es ",num[i],"su cuadrado es ",cuadrado[i],", y su raiz es ",raiz[i])