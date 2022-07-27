#2.- Crear un programa que permita resolver la siguiente fórmula, en donde desde el
#proceso principal, se debe enviar a una funcion llamada resolverFormula() los
#parámetros a y b (ingresados previamente por teclado en el proceso principal) , la
#función debe recibir los parámetros calcular y mostrar resultados.   a/b+1


def resolverFormula(a,b):
    resul=a/b+1
    print("El resultado es: ",resul)


print("Ingreso de numeros")
a=float(input("Ingrese a: "))
b=float(input("Ingrese b: "))
if b != -1 and b != 0:
    resolverFormula(a,b)
elif b == -1 or b == 0:
    print("El numero ingresado generaria una violación a las reglas aritmeticas")
