#En este ejemplo crearemos una matriz de 3*4

matriz=[] #Asignamos a una variable una lista vacia

print("Elije el tamaño de la matriz")
columnas=3
filas=3

for i in range(columnas): #Iniciamos un bucle for con el rango de columnas que queramos para nuestra matriz
    matriz.append([None]*filas) #a nuestra variable que tiene la lista vacia, con la funcion append le asignamos un valor a las filas multiplicada por 4, la cantidad de veces que la multipliquemos sera la cantidad de filas que tendremos.

print("\nIngreso de estudiantes")

for i in range(columnas):
    for j in range(filas):
        matriz[i][j]=input(f"Elemento {i}-{j}: ")
