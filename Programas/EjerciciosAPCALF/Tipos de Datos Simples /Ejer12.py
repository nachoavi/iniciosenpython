pandeayer=int(input("Ingrese la cantidad de barras vendidas: "))

panfresco=3.49
descuento=panfresco*0.60
subtotal=panfresco-descuento
total=pandeayer*subtotal
print("El coste habitual de una barra es: ",panfresco)
print("El descuento por no ser fresco es: ",round(descuento,2))
print("El coste final es: ",round(total,2))