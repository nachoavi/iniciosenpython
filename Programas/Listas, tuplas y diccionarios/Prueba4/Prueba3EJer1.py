import numpy as np 

v1=np.array([None]*10)

for i in range(0,v1.size):
    v1[i]=int(input(f"Ingrese el numero {i+1}: "))

print("Los datos ingresados fueron: ")
for i in range(0,v1.size):
    print(v1[i])

for i in range(0,v1.size):
    v1[i]=v1[i]**2
print("Los numeros elevados al cuadrado son: ")
for i in range(0,v1.size):
    print(v1[i])