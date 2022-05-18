print("Hello world")
print("Este es el comienzo")
#Las variables pueden ser de tipo entero(int),decimal(float), y tambien pueden almacenar texto o strings(str)
#Python diferencia mayusculas, por ejemplo  num1=25 es diferente a Num1="Juan Perez"

num1=25 #Tipo entero o int
num2=2.5 #Tipo decumal o float
nombre1="Javier Altozano" #Tipo texto o strings(str)
num3=30

#Las variables se pueden sumar entre si, ejemplo:

resultado=num1+num3
print(resultado)
print("-----------------------------")
#La asignación: podemos asignar una variable a otra agragando el simbolo +, ejemplo:
print("Aquí realizamos una asignación:")
mensaje="Hola" #A la variable mensaje le asignamos un string "Hola"
mensaje+=" " #A la variable mensaje le sumamos un caracter de espacio
mensaje+="Ernesto" #A la variable mensaje le sumanos un string "Ernesto"
print(mensaje) #Imprimimos por pantalla la variable mensaje
print("-----------------------------")

#La concatenación: Podemos unir dos cadenas o más con una concatenación usando el simbolo +, ejemplo:
print("Aquí realizamos una concatenación:")
mensaje="Hola"
espace=" "
name="Ernesto"
print(mensaje+espace+name)
print("-----------------------------")

print("Aquí realizamos otra concatenación como ejemplo")
numberone=50 #A la variable numberone le asignamos el numero 50
numbertwo=40 #A la varuable numbertwo le asignamos el numero 40
resultadosuma=numberone+numbertwo #Aquí a la variable resultadosuma le asignamos la concatenación de numberone y numbertwo
resultadosuma=str(resultadosuma) #Aquí a la variable resultadosuma le decimos que se convierta de formato int a formato str o string para despues realizar una impresión entre dos strings correctamente.
print("Este es el resultado de una suma entre 50 y 40: " + resultadosuma)
print("-----------------------------")

#La busqueda: dentro de una cadena de caracteres podemos localizar una subcadena mas pequeña con el metodo find, ejemplo:
print("Aquí realizamos un ejemplo de busqueda:")
mensaje2="Hola Juan"
buscar_subcadena=mensaje2.find("Juan") #A la variable buscar_subcadena le asignamos la variable mensaje2 con el parametro .find("Juan") para que busque e indique el numero de caracter en el que se encuentra.
print(buscar_subcadena) #Aqui imprimimos por pantalla el resultado de buscar_subcadena.
print("-----------------------------")

#La extracción: se trata de sacar fuera de una cadena, una porción de la misma según su posición dentro de ella. Para ello es necesario indicar la posición a extraer [1:8]
print("Aquí realizaremos un ejemplo de extracción:")
mensaje3="Hola Juan Pablo"
extraer_subcadena=mensaje3[0:9]
print(extraer_subcadena)
print("-----------------------------")

#La comparación: se utiliza para comparar dos cadenas de caracteres. Para ello se utiliza el operador ==, ejemplo:
print("Aquí realizamos un ejemplo de comparación:")
sms1="Hello"
sms2="Hello"
print(sms1 == sms2)
print("-----------------------------")

