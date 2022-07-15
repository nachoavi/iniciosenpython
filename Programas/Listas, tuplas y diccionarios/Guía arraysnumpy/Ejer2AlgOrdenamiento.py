import numpy as np #Partimos importanto la libreria numpy con np

num=np.array([1,2,3,4,5,6,7,8,9,10]) #Para crear un nparray hay que hacerlo dentro de una variable, entre parentesis y el los vectores entre corchetes

for i in range(1,num.size): #Realizamos el primer bucle for que será nuestro recorrido partiendo de la posición 1 hasta la logitud de nuestro array
    for j in range(num.size - i):#Dentro del primer for realizamos un segundo bucle for que sera nuestra posición dentro del array, le restamos el recorrido cada vez que termine.
        if num[j] < num[j + 1]:#Comparamos si nuestro array en la posición(j) actual num[j] es menor a la posicion(j) siguiente num[j+1]
            temp = num[j] #Si es menor entonces asignamos el valor de la posición actual a una variable temporaria(temp)
            num[j] = num[j + 1] #despues hacemos el cambio, a la posición actual(num[j]) le asignamos el valor de la posición siguente(num[j+1])
            num[j + 1] = temp #y a la posición siguiente(num[j+1]) le asignamos el valor de la variable temporaria 
print(num) 
