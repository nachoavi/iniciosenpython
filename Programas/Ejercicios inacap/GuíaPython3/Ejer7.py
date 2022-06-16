#7.- Crear un Programa. que permita ingresar 10 ticket de entradas (código,
#precio), para un evento. Al finalizar los ingresos visualizar la suma total de
#precios de la venta. Si la venta total asciende los $20.000 aplicar un descuento
#de 8,5% mostrar el resultado de la venta final con descuento aplicado.
#(Debe controlar la cantidad de ingresos mediante una estructura de control.)
sum=0
for x in range (1,11):
    cod=input(f"Ingrese el codigo de la venta {x}: ")
    pre=int(input("\nIngrese el precio: "))
    op=input("Desea ingresar otra venta?[S/N] ")
    while op not in ["S", "s", "N", "n"]:
        print("Opción incorrecta, intentelo de nuevo")
        op=input("Desea ingresar otra venta?[S/N] ")
    if op in ["S", "s"]:
        if x == 10:
            print("Se ha alcanzado el numero maximo de ventas")
    else:
        sum+=pre
        break
    sum+=pre
if sum >20000:
    des=sum*0.85/10
    des=int(des)
    tot=sum-des
else:
    des=0
    tot=sum-des
print("El descuento es de: ", des)
print("El total es de: ", tot)