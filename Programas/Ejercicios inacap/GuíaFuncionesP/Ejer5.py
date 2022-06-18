#5.- Crear un programa que permita ingresar 5 números (sin ciclo), después llamar
#una función (con parámetros), se le debe enviar los 5 números, la función debe
#permitir identificar el número mayor y retornarlo al proceso principal para su
#visualización.



def nummayor(n1,n2,n3,n4,n5):
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
        

print("Numero mayor")

num1=int(input("Ingrese el numero 1: "))
num2=int(input("Ingrese el numero 2: "))
num3=int(input("Ingrese el numero 3: "))
num4=int(input("Ingrese el numero 4: "))
num5=int(input("Ingrese el numero 5: "))
mayor=nummayor(num1,num2,num3,num4,num5)
print("El numero mayor es: ",mayor)
