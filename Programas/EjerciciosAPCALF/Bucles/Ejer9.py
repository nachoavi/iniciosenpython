password="admin123"
tryy=input("Ingrese la contraseña: ")
while tryy != password:
    print("Error contraseña errada, intentelo de nuevo")
    tryy=input("Ingrese la contraseña: ")
print("Bienvenido al sistema")