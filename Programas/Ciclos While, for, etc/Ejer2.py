pasww="contraseña"

x=0
while x < 3:
    print("Admin")
    con=input("Ingrese la contraseña: ")
    if con == pasww:
        print("Bienvenido al sistema")
        x=4
    elif con != pasww:
        print("Contraseña incorrecta, intentelo nuevamente")
        x+=1
if x == 3:
    print("Has sobrepasado los intentos, el sistema cerrará")
