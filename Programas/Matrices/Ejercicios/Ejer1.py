#Crear una matriz que permina el ingreso de 8 nombres, luego solicitar el nombre a buscar al usuario
#generando un reporte de los nombres econtrados, además visualizar la cantidad de nombres encontrados
import numpy as np
matriz=[]
columnas=2
filas=4


for i in range(columnas):
    matriz.append([None]*filas)

matriz=np.array(matriz)

for i in range(columnas):
    for j in range(filas):
        matriz[i][j]=input(f"Ingrese nombres {i+1}.{j+1}: ")


buscarnom=input("Ingrese el nombre a buscar: ")

for f in range(columnas):
    for c in range(filas):
        if matriz[f][c] == buscarnom:
            print(matriz[f][c])


