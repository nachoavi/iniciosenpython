#Ejemplo de sentencia continue

print("While con la sentencia continue \n")
x=0
while x <10:
    x+=1

    if x==5:
        continue #En este caso el continue volvera a ejecutar el bucle while, lo que hara que omita el print de abajo.
    print("El valor actual de la variable es: ", x)

print("Fin del programa, la sentencia break se ha ejecutado")