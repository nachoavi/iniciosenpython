
listf=["Juan","Pablo","Lorena","Ignacio","Sebastían"] #Se crea la lista con nombres de participantes
print(listf) #Se muestra por pantalla

listf.append("Ana") #Se agrega a Ana al final de la lista con .append
print(listf[:])#Se muestra por pantalla [:] significa que mostraremos toda la lista desde el valor 0

listf.extend(["Alverto","Luis","Ivan","José"]) #Se añaden varios participantes al final de la lista con .extend
print(listf[:])

listf.insert(0, "Xímena") #Se agrega el dato Xímena en la pocisión 0 de la lista, vale decir al principio con .insert(0, Ximena) el parametro 0 es la posición dentro de la lista
print(listf[:])

listf.remove("José") #Se elimina el dato Jośe con .remove
print(listf[:])

print(listf.index("Ana")) #Mostramos por pantalla la posición o indice que ocupa el dato Ana dentro de la lista con .index

listf.remove("Ana") #Eliminamos el dato Ana de la lista con .remove
print(listf[:])

print(listf[0:3]) #Mostramos por pantalla los primeros 3 datos de la lista, donde 0 es el primer dato y 3 es hasta donde se mostrará :