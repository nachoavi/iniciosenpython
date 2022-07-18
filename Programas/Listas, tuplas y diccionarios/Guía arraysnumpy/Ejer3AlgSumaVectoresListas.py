import numpy as np

v1=np.array([None]*5)
v2=np.array([None]*5)
resul=np.array([None]*5)

print("\nLLenado vector 1: ")
for i in range(0,v1.size):
    v1[i]=int(input(f"Ingrese el numero {i+1}: "))

print("\nLLenado vector 2: ")
for i in range(0,v2.size):
    v2[i]=int(input(f"Ingrese el numero {i+1}: "))

for i in range(0,resul.size):
    resul[i]=v1[i]+v2[i]
    print(v1[i],"+",v2[i],"=",resul[i])

