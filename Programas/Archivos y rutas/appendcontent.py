#En el modo de escritura append, si el archivo no existe se crea.
#Si el archivo si existe, comenzara a agregar datos donde esté ubicado el puntero, es decir al final

archivo=open("Ruta Vacia/info2.txt","w")

paises=["Chile\n","Peru\n","Ecuador\n","El Salvador\n","Finlandia\n","Noruega\n"]
archivo.writelines(paises)


archivo.close()