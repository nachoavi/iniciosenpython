x=0
while x <=10:
    n=int(input("\nIngrese un numero: "))
    print("\nUsted ingreso el n°:",n)
    op=input("Desea ingresar otro numero? [S/N]: ")
    while op != "S" and op != "s" and op != "N" and op != "n":
        print("Opción incorrecta, vuela a intentarlo")
        op=input("Desea ingresar otro numero? [S/N]: ")
    if op == "S" or op == "s":
        if x==10:
            print("No se pueden ingresar más numeros")
    else:
        x=10                
    x+=1
if x==10:
    print("Los numeros se han registrado correctamente")
