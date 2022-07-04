def validarUsuario(usr,pasw):
    x=1
    while x <3:
        if usr=="Administrador" and pasw=="info123":
            print("Sr. Administrador bienvenido al sistema")
            x=4
        elif usr!="Administrador" or pasw!="info123":
            print("Datos incorrectos, intente nuevamente")
            usr=input("Ingrese nombre de usuario: ")
            pasw=input("Ingrese contraseña: ")
            x=x+1
    if x ==3:
        print("Ha sobrepasado el numero de intentos, el sistema cerrará")

       
        





usr=input("Ingrese nombre de usuario: ")
pasw=input("Ingrese contraseña: ")
validarUsuario(usr,pasw)