from Trabajador import Trabajador
from Panadero import Panadero


print("Prueba 1.2 de Programación")
print("Ingrese la siguiente información para crear un trabajador Panadero: ")
# realizar código para crear un Panadero según los datos ingresados por teclado..
nombre = input("Ingrese el nombre del trabajador: ")
apellido = input("Ingrese el apellido del trabajador: ")
estadoSalud = True
capital = 0
diasTrabajados = 10
valorDiaTrabajado = 15000
trabajador1 = Panadero(nombre, apellido, estadoSalud, capital, diasTrabajados, valorDiaTrabajado)
opcion = -1
while (opcion != 0):
    print("1. Enfermar al Trabajador")
    print("2. Recuperar salud del Trabajador")
    print("3. Trabajar")
    print("4. Pagar sueldo")
    print("5. Despedir")
    print("6. Mostrar Datos")
    print("0. Salir")
    opcion = int(input())

    if opcion == 1:
        trabajador1.enfermar()
    elif opcion == 2:
        trabajador1.recuperarse()
    elif opcion == 3:
        trabajador1.trabajar()
        if trabajador1.trabajar == False:
            print("El panadero no trabajó")
    elif opcion == 4:
        trabajador1.pagarSueldo()
    elif opcion == 5:
        añosdeAntiguedad= int(input("Ingrese años de antiguedad: "))
        trabajador1.despedir(añosdeAntiguedad)
    elif opcion == 6:
        trabajador1.infoPanadero()
    elif opcion == 0:
        print("Fin del programa")
    else:
        print("Opción ingresada incorrecta. Intente nuevamente")