def mensaje1(): #Definimos el nombre de nuestra función como "mensaje1"
    print("Bienvenido Luis") #Detallamos las acciones que realizara nuestra función, en este caso será un print
mensaje1() #Llamanos a la función mensaje 1

def mensaje2(nombre):  #Definimos el nombre de nuestra función, y entre parentesis le asignamos una variable
    print("Bienvenido", nombre) #detallamos que las acciones que realizara nuestra función será imprimir el mensaje de "Bienvenido" junto a la variable nombre

n=input("Ingrese su nombre: ") #a la variable "n" le asignamos el nombre del usuario que sera ingresado por el mismo
mensaje2(n) #llamamos a la función mensaje2 y entre parentecis le pasamos la variable n que contendra el nombre que ingreso el usuario
            #En la función la variable n sera reemplazada por la variable nombre, creando así correctamente el mensaje de bienvenida

def mensaje3(nombre):
    cadena = "Bienvenido " + nombre
    return cadena
    


       