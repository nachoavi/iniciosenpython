#Modo escritura o write

archivo=open("Ruta Vacia/info1.txt","w") #se agrega w para especificar el modo write
#si el fichero no existe se creara automaticamente uno vacio
#si el fichero si extiste python sobrescribira el archivo existente.



archivo.write("Hola mi gente\n") #con metodo .write podremos pasar solo "strings" al archivo

listacompras=["Cafe\n","Té\n","Pan\n","Helado\n","Cigarretes\n"]
archivo.writelines(listacompras) #con el metodo .writelines podremos pasar "str,listas,tuplas, etc"

archivo.writelines(["Mangos\n","Platano\n"]) #otra forma de incluir listas en el metodo writelines


archivo.close()