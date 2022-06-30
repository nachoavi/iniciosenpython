#definir una lista con elementos
lista1=["Juan","Andres","Cristina",1000]

#Visualizamos la lista
print(lista1)

#agregamos a Carlos al final de la lista
lista1.append("Carlos")
print(lista1[:])


#Insertar en la posición 1 de la lista a Ximena
lista1.insert(1,"Ximena")
print(lista1[:])

#Insertamos en la posición 0 de la lista a esteban
lista1.insert(0,"Esteban")
print(lista1[:])

#Agregar estos 3 elementos al final de la lista: "Auto","barco","avion"
lista1.extend(["Auto","Barco","Avión"])
print(lista1[:])

#Eliminar el elemento auto de la lista
lista1.remove("Auto")
print(lista1[:])