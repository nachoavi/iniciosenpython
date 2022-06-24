def sumar(a,b):
    r=a+b
    return r
def restar(a,b):
    r=a-b
    return r
def multiplicar(a,b):
    r=a*b
    return r
def dividir(a,b):
    if b == 0:
        print("No se puede dividir por 0")
    else:
        r=a/b
        return r


print("Menu principal\n")
print("1)Sumar\n2)Restar\n3)Multiplicar\n4)Dividir\n5)Salir\n")
op=input("Seleccione una opción: ")
while op not in ["1","2","3","4","5"]:
    print("Error, opción incorrcta")
    op=input("Seleccione una opción: ")
if op == "1":
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    resul=sumar(n1,n2)
    print("El resultado es: ",resul)
elif op == "2":
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    resul=restar(n1, n2)
    print("El resultado es: ",resul)