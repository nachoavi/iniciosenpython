producto=input("Ingrese producto: ")
precio=float(input("Ingrese su precio: "))
cantidad=int(input("Ingrese la cantidad: "))
print("{poducto}: {cantidad:3d} unidades x {precio:9.2f}E = {total:11.2f}").format(producto=producto,cantidad=cantidad, precio=precio, total=cantidad*precio)