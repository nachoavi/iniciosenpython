import numpy as np

curso=np.array(["Luis","Tiffani","Sebas","Franco","Maicol","Camilo","Bastian","Franco"])

ob=0
nomBuscar=input("Ingrese el nombre a buscar: ")
for i in range(0,curso.size):
    if curso[i]==nomBuscar:
        print("Encontrados: ",curso[i])
        ob=ob+1
print("Objetos encontrados: ",ob)