#3. Crear un PROGRAMA que ingrese cualquier número, a medida que se
#ingresa multiplique por 4, ese resultado lo divide en 2. El resultado final
#debe ser mostrado en pantalla. Una vez terminado el procedimiento, debe
#dar la posibilidad de ingresar un nuevo número.
# OTRA FORMA
op="s"
while (op=="s"):
    n=int(input("Ingrese Numero: "))
    mul= n*4
    div=mul/2
    print("El resultado es: ", div)

    op= input("Desea ingresar nuevamente (s/n):")
    while(op!="S" and op!="s" and op!="N" and op!="n"):
        print("La opción ingresada es incorrecta, vuelva a ingresar")
        op= input("Desea ingresar nuevamente (s/n):")

    
print("Fin del programa")
