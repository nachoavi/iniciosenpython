#Ejemplo de sentencia continue

print("While con la sentencia continue \n")
x=0
while x <10:
    x+=1

    if x==5:
        continue
    print("El valor actual de la variable es: ", x)

print("Fin del programa, la sentencia break se ha ejecutado")