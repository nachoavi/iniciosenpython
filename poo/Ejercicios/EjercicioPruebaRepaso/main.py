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
valorDiaTrabajo = 15000


trabajadorPanadero = Panadero(nombre,apellido,estadoSalud,capital,diasTrabajados,valorDiaTrabajo)

opcion = -1
while (opcion != 0):
    print("1. Enfermar al Trabajador")
    print("2. Recuperar saludos del Trabajador")
    print("3. Trabajar")
    print("4. Pagar sueldo")
    print("5. Despedir")
    print("6. Mostrar Datos")
    print("0. Salir")
    opcion = int(input())

    if opcion == 1:
        trabajadorPanadero.enfermar
    elif opcion == 2:
        trabajadorPanadero.recuperarse
    elif opcion == 3:
        trabajadorPanadero.Trabajar
    elif opcion == 4:
        trabajadorPanadero.pagarSueldo
    elif opcion == 5:
        trabajadorPanadero.despedir
    elif opcion == 6:
        trabajadorPanadero.infoPanadero
    elif opcion == 0:
        print("Fin del programa")
    else:
        print("Opción ingresada incorrecta. Intente nuevamente")