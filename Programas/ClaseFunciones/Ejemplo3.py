#Función sin retorno
def mensaje():
    print("Hola esta es una función sin parametros y sin retorno")


def sumar():
    x=10
    y=5
    s=x+y
    print("La suma es", s)

#Función con paŕametros y sin retorno
def restar(a,b):
    res=a-b
    print("La resta de los numeros es ", res)

#Función sin parametros y con retorno
def multiplicar():
    x=10
    y=7
    mul=x*y
    return mul

#Función con parametros y con retorno
def dividir(a,b):
    divi=int(a/b)
    return divi



#Inicio del programa
print("Programa principal")

#Llamamos a la funcioń sin parametros y sin retorno
mensaje() #Invocamos a la función mensaje() previamente definida
sumar() #Invocamos a la función sumar() previamente definida

#Llamar función con parametros y sin retorno
print("Resta de dos numeros")
n1=int(input("Ingrese el primer numero: ")) #El usuario asigna valor a n1
n2=int(input("Ingrese el numero para restar: ")) #El usuario asigna valor a n2 
restar(n1,n2) #Llamamos a la función restar y le pasamos los parametros n1 y n2


#Llamar función sin parametros y con retorno
print("Multiplicación de 2 numeros internos \n")
resul=multiplicar()
print("La multiplicación de los numeros es ", resul)  #Forma 1
print("La multiplicación de los nuemeros es", multiplicar()) #Forma 2


#Llamar función con parametros y con retorno
print("Divición de 2 numeros \n")
p=100
q=30
resul=dividir(p, q)
print("El resultado de la divición 100/30 es ", resul) #Forma 1
print("El resultado de la divición 100/30 es ", dividir(p, q)) #Forma 2



