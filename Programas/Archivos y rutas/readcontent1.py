archivo=open("Ruta A/infoA.txt") #A la variable archivo le asignaremos el contenido del fichero infoA.txt,
#con el operador open podremos especificar la ruta relativa

linea=archivo.readline().rstrip("\n") #a la variable "linea" le pasaremos la primera linea del fichero archivo, 
#con el parametro .readline(), despues esto hara que el "puntero" se posicione automaticamente 
#en la segunda linea, tambien podemos quitar el "enter" del final de la linea con readline().rstrip("\n")

print(linea) #mostraremos por pantalla el contenido de la variable linea


archivo.close() #con el parametro .close cerraremos el archivo

archivo2=open("Ruta B/infoB.txt")

datos=[]

linea1=archivo2.readline()
datos.append(linea1)
linea2=archivo2.readline()
datos.append(linea2)

print(datos)

archivo2.close()