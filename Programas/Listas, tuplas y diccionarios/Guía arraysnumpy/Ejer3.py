import numpy as np

v1=np.array([None]*5) #Creamos el primer vector vacio, con np.array y le pasamos como parametros None * 5 para crear 5 espacios vacios
v2=np.array([None]*5) #Creamos el segunfo vector vacio con las mismas condiciones anteriores
resul=np.array([None]*5)#y creamos el tercer vector donde se almacenarán los resultados, con las mismas condiciones de creacion del primero

print("Llenado vector 1\n")
for i in range(0,v1.size):
    v1[i]=int(input(f"Ingrese numero {i+1}: "))

print("\nLlenado vector 2\n")
for i in range(0,v2.size):
    v2[i]=int(input(f"Ingrese numero {i+1}: "))

print("\n Llenado del resultado")
for i in range(0,resul.size):
    resul=v1[i]+v2[i]
    print(v1[i],"+",v2[i] ,"=", resul)
