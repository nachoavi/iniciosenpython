renta = int(input("Ingrese su renta anual: "))

if renta < 10000:
    impuesto = 5
elif renta > 10000 and renta < 20000:
    impuesto = 15
elif renta > 20000 and renta < 35000:
    impuesto = 20
elif renta > 35000 and renta < 60000:
    impuesto = 30
elif renta > 60000:
    impuesto = 45

print("Su impuesto impositivo será de: ", renta * impuesto / 100, " Euros", sep="")