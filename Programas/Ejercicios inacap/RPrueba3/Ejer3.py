def validarUsuario(usr,pasw):
    x=1
    while x < 3:
        if usr == "administrador" and pasw == "info123":
            print("Sr Admin, bienvenido al sistema")
            break
        elif usr != "administrador" and pasw != "info123":
            print("Error, datos invalidos, vuelva a intentar.")
            print("Inicio de sesión")
            usr=input("Ingrese nombre de usuario: ")
            pasw=input("Ingrese contraseña: ")
            x=x+1
    if x >= 3:
        print("Numero de intentos maximo alcanzado, el sistema cerrará")

print("Inicio de sesión")
usr=input("Ingrese nombre de usuario: ")
pasw=input("Ingrese contraseña: ")
validarUsuario(usr,pasw)
