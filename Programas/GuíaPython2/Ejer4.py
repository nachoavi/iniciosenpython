print("Registro de clientes \n")
x=2
while x ==2:
    nom=input("Nombre cliente: ")
    tel=input("Teléfono: ")
    es=input("Estado civil: ")
    print(nom, " es ", es)
    x=x-2
    p=input("Desea ingresar otro cliente?[S/N]: ")
    if p == "S" or p =="s":
        x+=2
