curso=["Iván","Joakin","Sebas","Xokas","Gerancio","Danilo","Bastian","Iván"]
find=[]
nomBuscar=input("Ingrese el nombre a buscar: ")
resul=0
for i in range (len(curso)):
    if curso[i] == nomBuscar:
        find.append(curso[i])
        resul=resul+1
print(find,"Cantidad de resultados obtenidos: ",resul)
