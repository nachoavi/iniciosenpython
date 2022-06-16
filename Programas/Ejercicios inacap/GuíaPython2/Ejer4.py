#4.- Crear un PROGRAMA que permita ingresar clientes
#de una empresa,Ingresar lo siguientes datos
#(Nombre, Fono y estado Civil). Dependiendo
#del estado civil, arrojar el mensaje en
#pantalla que muestre el nombre de la persona y
#su estado civil ej: “Ana es casada”. Al final
#preguntar si desea ingresar un nuevo cliente.
A="Soltero"
B="Casado"
C="Viudo"
D="Divorciado"

op="s"
while(op=="s"):
    nom=input("Ingrese nombre: ")
    fon=input("Ingrese fono:")
    print("Selecione el estdo civil: \n[A]soltero/a \n [B]casado/a \n [C]viudo/a \n [D]divorciado/a:")
    x=1
    while (x==1):
        ec=input("Ingrese Estado Civil: ")
        if(ec=="A" or ec=="a"):
            print(nom, " es " , A)
            x=2
        elif(ec=="B" or ec=="b"):
            print(nom, " es " , B)
            x=2
        elif(ec=="C" or ec=="c"):
            print(nom, " es " , C)
            x=2
        elif(ec=="D" or ec=="d"):
            print(nom, " es " , D)
            x=2
        else:
            print("ha ingresado una opción incorrecta, ingrese estado civil nuevamente")

    op=input("Desea ingresar otro cliente (s/n): ")
    
    while(op!="n" and op!="s" and op!="N" and op!="S"):
        print("Ingrese una opción correcta, vuelva a intentar!!")
        op=input("Desea ingresar otro cliente (s/n): ")


print("Fin del Programa")