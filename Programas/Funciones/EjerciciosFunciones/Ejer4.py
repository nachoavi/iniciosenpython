def totalFactura(cantidad,iva):
    totalfinal=0
    totaliva=0
    if iva != 0:
        totaliva=cantidad*iva/100
        totalfinal=totaliva+cantidad
        return totalfinal
    else:
        totaliva=cantidad*21/100
        totalfinal=cantidad+totaliva
        return totalfinal

print("Calculadora de IVA")
cantidad=int(input("Ingrese la cantidad: "))
iva=int(input("Ingrese el IVA correspondiente %: "))
total=totalFactura(cantidad, iva)
print("El total es de: ",total)