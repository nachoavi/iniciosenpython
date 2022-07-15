tupla1=(1,2,3,4,"hola","maria","andres","maria")

print("Mostrar datos de una tupla")
for i in range(0,len(tupla1)):
    print(tupla1[i])

print("\nBuscar valor en una tupla")
for i in range (0,len(tupla1)):
    if tupla1[i]=="maria":
        print(tupla1[i])


print("\nMostrar datos de una tupla de forma inversa")

for i in range (5,-1,-1):
    print((tupla1[i]))

cont=0
print("\n Buscar el valor de una tupla por teclado")
nomBuscar=input("Ingrese el nombre de la persona: ")
print("\nBuscar valor en una tupla")
for i in range (0,len(tupla1)):
    if tupla1[i]==nomBuscar:
        print(tupla1[i])
        cont=cont+1
print("La cantidad de valores encontrados son: ",cont)


print("\nRecorrido inverso de la tupla, desde el ultimo elemento hasta el segundo elemento")
for i in range(7,0,-1):
    print(tupla1[i])



