#Crear un programa que envia una "lista" de nombres ingresados por teclado al archivo de la ruta C

infoc=open("Ruta C/infoC.txt","w")


for i in range(5):
    infoc.write(input(f"Ingrese el nombre numero {i+1}: ")+"\n")


infoc.close()