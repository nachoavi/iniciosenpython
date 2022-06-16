prod=input("Ingrese el producto: ")
pre=int(input("Ingrese el precio: "))
can=int(input("Ingrese la cantidad: "))
sub=pre*can
desc=sub*0.075
tot=sub-desc
print("El subtotal es de: ",sub)
print("EL descuento es de: ",desc)
print("EL total es: ",tot)
