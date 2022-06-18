#crear un programa que permita llamar una función (sin parámetros), la función
#debe permitir ingresar 5 números (sin ciclo) y finalmente retornar el número
#mayor al proceso principal para visualizarlo.




def nums():
    n1=int(input("Ingrese el numero 1: "))
    n2=int(input("Ingrese el numero 2: "))
    n3=int(input("Ingrese el numero 3: "))
    n4=int(input("Ingrese el numero 4: "))
    n5=int(input("Ingrese el numero 5: "))
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        return n1
    elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        return n2
    elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        return n3
    elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        return n4
    elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
        return n5


print("El numero mayor")
nummayor=nums()
print("El numero mayor es: ", nummayor)