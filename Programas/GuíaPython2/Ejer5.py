x=1
sum=0
while x <=10:
    cod=input(f"Ingrese codigo de la venta {x}: ")
    pre=int(input("Ingrese el precio: "))
    sum=sum+pre

    op=input("Desea ingresar otra venta? [S/N]: ")
    while(op!="n" and op!="s" and op!="N" and op!="S"):
        print("Ingrese una opción correcta, vuelva a intentar!!")
        op=input("Desea ingresar otra venta? [S/N]: ")

    if(op=="S" or op=="s"):
        if(x==10):
            print("No se pueden ingresar mas entradas")
    else:
        x=10
    x+=1
if sum > 20000:
    des=sum*0.10/x
    des=int(des)
    tot=sum-des
    
else:
    des=0
    tot=sum-des
    
print("Total recaudado: ", sum)
print("Descuento: ", des)
print("Total pagar: ", tot)





