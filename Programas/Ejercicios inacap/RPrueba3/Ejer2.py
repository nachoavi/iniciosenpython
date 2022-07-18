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
