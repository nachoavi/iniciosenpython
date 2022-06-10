#4.- Crear un PROGRAMA que permita ingresar clientes
#de una empresa,Ingresar lo siguientes datos
#(Nombre, Fono y estado Civil). Dependiendo
#del estado civil, arrojar el mensaje en
#pantalla que muestre el nombre de la persona y
#su estado civil ej: “Ana es casada”. Al final
#preguntar si desea ingresar un nuevo cliente.


op="s"
while(op=="s"):
    nom=input("Ingrese nombre: ")
    fon=input("Ingrese fono:")
    print("Ingrese estado Civil: soltero/a, casado/a, viudo/a o divorciado/a:")
    x=1
    while (x==1):
        ec=input("Ingrese Estado Civil: ")
        if(ec=="soltero" or ec=="soltera"):
            print(nom, " es " , ec)
            x=2
        elif(ec=="casado" or ec=="casada"):
            print(nom, " es " , ec)
            x=2
        elif(ec=="viudo" or ec=="viuda"):
            print(nom, " es " , ec)
            x=2
        elif(ec=="divorciado" or ec=="divorciada"):
            print(nom, " es " , ec)
            x=2
        else:
            print("ha ingresado una opción incorrecta, ingrese estado civil nuevamente")

    op=input("Desea ingresar otro cliente (s/n): ")
    while(op!="n" and op!="s" and op!="N" and op!="S"):
        print("Ingrese una opción correcta, vuelva a intentar!!")
        op=input("Desea ingresar otro cliente (s/n): ")


print("Fin del Programa")
        
        
                


            
            
            
            
