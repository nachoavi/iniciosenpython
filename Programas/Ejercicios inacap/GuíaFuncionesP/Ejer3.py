def sumar(a,b):
    su=a+b
    return su

def restar(a,b):
    re=a-b
    return re

def multiplicar(a,b):
    mul=a*b
    return mul

def dividir(a,b):
    return a/b

def salir():
    exit()


print("MENU PRINCIPAL\n")
print("1)Sumar \n2)Restar \n3]Multiplicar \n4)Dividir \n5)Salir \n")
ing_num = input('Ingrese un número (1-5): ')
while ing_num not in ["1","2","3","4","5"]:
    print("Error, ingrese una opción correcta")
    ing_num = input('Ingrese un número (1-5): ')

if ing_num == "1":
    print("\nPrograma que suma\n")
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    su=sumar(n1, n2)
    print("El resultado de la suma es: ",su)


elif ing_num == "2":
    print("\n Programa que resta\n")
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese la cantidad a restar: "))
    re=restar(n1, n2)
    print("El resultado de la resta es: ",re)

elif ing_num == "3":
    print("\nPrograma que multiplica\n")
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    mul=multiplicar(n1, n2)
    print("El resultado de la multiplicación es: ", mul)

elif ing_num == "4":
    print("\nPrograma que divide\n")
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    div=dividir(n1, n2)
    print("El resultado de la divición es: ", div)

elif ing_num == "5":
    salir()













