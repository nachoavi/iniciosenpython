#Otra forma de leer el contenido del archivo con FOR y WHILE

archivo=open("Ruta A/infoA.txt")

#con FOR
for linea in archivo:
    print(linea.rstrip("\n")) #con rstrip le decimos que borre los saltos de linea

#con WHILE


archivo.close()

archivo=open("Ruta A/infoA.txt")

linea=archivo.readline()
while linea != "":
    print(linea.rstrip("\n"))
    linea=archivo.readline()

archivo.close() 