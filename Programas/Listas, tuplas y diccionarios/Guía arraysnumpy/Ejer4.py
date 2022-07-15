import numpy as np
import math as math

v1=np.array([None]*5)
v2=np.array([None]*5)
v3=np.array([None]*5)

for i in range(0,v1.size):
    v1[i]=int(input(f"Ingrese el numero {i+1}: "))

for i in range(0,v2.size):
    v2[i]=v1[i]**2

for i in range(0,v3.size):
    v3[i]=math.sqrt(v1[i])

for i in range(0,v1.size):
    print(f"Numero {i+1} es",v1[i], "su cuadrado es: ",v2[i], "y su raiz es: ",v3[i])
