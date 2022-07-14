import numpy as np

#Definimos una variable "num" a la cual le asignamos un array con el valor None multiplicado 5 veces, 
#para asi generar 5 espacios
num=np.array([None]*5)

#Aquí se realiza la entrada de datos por teclado
#En este bucle for lo incrementamos desde el 0 hasta la variable num
#.size devuelve el número de elementos del array
for i in range(0,num.size): 
    num[i]=int(input("Ingrese numero: ")) #Entonces en los indices que va recorriendo el for ingresamos por teclado los numeros que queremos asignar

#Aquí mostramos por pantalla los numero antes ingresados haciendo un recorrido por el vector
for i in range(0,num.size):
    print("Numero: ", num[i])


#Procederemos a hacer un listado solo de los numero pares antes ingresados

for i in range(0,num.size): #En un ciclo for en el rago desde el 0 hasta la logitud del array mostraremos por pantalla solo los numeros pares
    if num[i]%2==0 and num[i]!=0:
        print("Numeros pares: ", num[i])

#Ahora haremos un listado solo de los numeros impares

for i in range(0,num.size):
    if num[i]%2==1:
        print("Numeros impares: ", num[i])

#Y aquí el listado de los 0
for i in range(0,num.size):
    if num[i]==0:
        print("Lista de 0: ",num[i])




