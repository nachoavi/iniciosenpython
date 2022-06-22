#Crear un PROGRAMA que ingrese 2 números cualquiera, mostrar en
#pantalla; su suma, resta, multiplicación, división y la raíz cuadrada del
#primer número. Validar el ingreso para ciertas operaciones.
from math import sqrt

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

s=n1+n2
print(s)
r=n1-n2
print(r)
m=n1*n2
print(m)

if n2 == 0:
    print("Error, no se puede dividir por 0")
else:
    d=n1/n2
    print("div: ",d)
ra=sqrt(n1)
print("La raiz del primer numero es: ", ra)