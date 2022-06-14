#Crear un Programa, que permita ingresar 10 números(Estructura de control:
#While y For)
#- Cada vez que se ingrese un número mostrarlo en pantalla.
#- Una vez ingresados los 10 números emitir un mensaje “Los 10 números ya se
#han ingresado satisfactoriamente”

for x in range(1,11):
    n=int(input("\nIngrese un numero: "))
    print("\nUsted ingreso el numero: ", n)
    op=input("Desea ingresar otro numero? [S/N]: ")
    while op not in ["S","s","N","n"]:
        print("Opción incorrecta, intentelo nuevamente")
        op=input("Desea ingresar otro numero? [S/N]: ")
    if op == "S" or op =="s":
        if x == 10:
            print("No se pueden ingresar más numero")
    else:
        x=11
        break
        

if x>10:
    print("\nLos numeros han sido ingresados correctamente")