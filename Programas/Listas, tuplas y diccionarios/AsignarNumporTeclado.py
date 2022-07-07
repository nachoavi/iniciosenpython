#Ingresar en una lista 5 numeros por teclado y finalmente visualizar el numero mayor dentro de la lista

num=[]
for i in range(0,5):
    num.append(int(input("Ingrese un numero: ")))
    if (i==0):
        mayor=num[i]
        menor=num[i]
    elif(num[i]>mayor):
        mayor=num[i]
    elif(num[i])<menor:
        menor=num[i]
    s=mayor+menor

print("El numero mayor es :", mayor)
print("El numero menor es ", menor)
print("La suma de las variables es: ",s)

