v1 = int(input("Ingrese el precio: "))
desc = float(input("Ingrese el descuento en decimal: "))
desctotal = v1 * desc
total = v1 - desctotal
print("El subtotal es de " + str(v1))
print("EL descuento es de: " + str(desctotal))
print("EL total es: " + str(total))
