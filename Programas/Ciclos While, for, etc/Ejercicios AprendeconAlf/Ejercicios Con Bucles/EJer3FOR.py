num=int(input("Ingrese un numero entero positivo: "))

if num > 0:
    for x in range(1, num+1,2):
        print(x, end=", ") #El parametro "end=" sirve para agregar algún dato al final de mostrar la variable x, en este caso es una str (", ")