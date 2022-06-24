def validarUsuario(a,b):
    x=0
    while x<=2:
        if a != "admin" or b != "info1234":
            print("Error, usuario o contraseña incorrecta")
            a=input("Usuario: ")
            b=input("Cotraseña: ")
            x=x+1
        elif a == "admin" and b == "info1234":
            print("Bienvenido al sistema")
            x=4
    if x > 2:
        print("Ha sobrepasado la cantidad de ingresos permitidos")

print("Inicio sesión")
usr=input("Usuario: ")
pasw=input("Contraseña: ")
validarUsuario(usr, pasw)
