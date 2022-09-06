#Crean en un vector 




import numpy as np

vector1 = np.array([None] * 5)
vector2 = np.array([None] * 5)
resultado = np.array([None] * 5)


print('Ingresos del primer vector')
for i in range(0, vector1.size):
    vector1[i] = int(input(f'({i+1}/5) Ingrese numeros: '))

print('Ingresos del segundo vector')
for i in range(0, vector2.size):
    vector2[i] = int(input(f'({i+1}/5) Ingrese numeros: '))


for i in range(0,resultado.size):
    resultado[i]=vector1[i]*vector2[i]
    print(vector1[i],"*",vector2[i],"=",resultado[i])



