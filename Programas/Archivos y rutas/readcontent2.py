#Metodo para leer el contenido completo del archivo

archivo=open("Ruta A/infoA.txt")

contenido=archivo.read().split("\n") #con .split podemos especificar lo que 
#queremos borrar, en este caso un salto de linea, esto hará que cada linea pase a 
#ser un elemento dentro de una lista

print(contenido)







archivo.close()