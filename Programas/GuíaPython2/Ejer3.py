#Realice un ALGORITMO que permita el Ingreso de 3 notas académicas.
#- Validar notas entre 1,0 y 7,0, en caso contrario emitir mensaje de error
#“Fuera de rango permitido” y volver a ingresar. (use un ciclos)
#- Mostar promedio final de notas.

x=1
sum=0
while x <=3:
    n=float(input(f"Ingrese la nota {x}: " ))
    if n >=1 and n <=7:
        sum=sum+n
        x=x+1
        print("\nNota ingresada con exito\n")
    else:
        print("Nota fuera de rango, por favor vuelva a ingresar: ")
        x-1
p=sum/3
print("El promedio es: ",p)