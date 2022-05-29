#Crear un programa. permita ingresar la venta anual de un negocio (1 por cada mes), estos deben ser ingresados por teclado. Después imprimir por el promedio anual. 
s=0
for x in range (1,13): 
    vta=int(input(F"Ingrese venta {x}:"))
    s=s+vta
prom=s/12
print("El promedio de las ventas es : ",prom)
