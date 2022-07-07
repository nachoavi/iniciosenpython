#Para asignar valores a una lista desde teclado por el usuario debemos asignar una lista vacia a una variable.

print("LLenado de una lista desde el taclado\n")
nom=[]

for i in range (0,5):
    nom.append(input("Ingrese nombre: "))


#Aquí realizaremos una visualización de los datos ingresado a la lista por el usuario
print("\n Visualización de los datos")

for i in range (0,5):
    print(nom[i])


#aquí mostrara los datos al revez

for i in range(4,-1,-1):
    print(nom[i])

#aquí el usuario tendra que eliminar un nombre de la lista

nomElim=input("Ingrese el nombre a eliminar")
for i in nom:
    if (i==nomElim):
        nom.remove(i)
        print(nomElim,"fue eliminado exitosamente")