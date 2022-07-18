import numpy as np

curso=np.array(["Felipe","Vicente","Sebas","Sebas","Cote","Tiffani","Ivan","Ivan"])

r=0
buscarn=input("Ingrese el nombre a buscar: ")
for i in range(0,curso.size):
    if buscarn == curso[i]:
        r=r+1
        print("Nombres encontrados: ",curso[i])
print(r)

