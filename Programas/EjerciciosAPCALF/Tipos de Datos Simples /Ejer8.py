n1=int(input("Ingrese un numero entero: "))
n2=int(input("Ingrese el segundo numero entero: "))

cociente=n1/n2
resto=cociente-int(cociente)
restoreal=resto*n2
print(n1,"entre",n2,"da un cociente",cociente,"y el resto es: ",restoreal)