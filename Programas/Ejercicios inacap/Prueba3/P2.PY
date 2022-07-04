def resolverFormula(a,b):
    resul=a/b+1
    print("El resultado de la formula es: ",resul)

a=int(input("Ingrese a: "))
b=int(input("Ingrese b: "))
if b != -1 and b != 0:
    resolverFormula(a, b)
else:
    print("Error, el numero ingresado genera una divición por 0")
