import numpy as np

personas=np.array(["Sebas","Tofanni","NachoOE","ElTerriblepiante","Maicol","Camilo","Andres","Lorena","Lorena"])


nomBuscar=input("Ingrese el nombre a buscar: ")
resul=0
for i in range(0,personas.size):
    if personas[i]==nomBuscar:
        print(personas[i])
        resul=resul+1
        print("Resultados obtenidos: ",resul)
