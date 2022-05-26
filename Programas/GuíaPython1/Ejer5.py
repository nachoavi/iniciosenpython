nom=input("Nombre: ")
ape=input("Apellido: ")
date=input("Fecha: ")
prod=input("Producto: ")
pre=int(input("Precio: "))
can=int(input("Cantidad: "))
neto=pre*can
iva=neto*0.19
total=neto+iva
print("Precio Neto: ",neto)
print("El iva es: ",iva)
print("El total es: ",total)