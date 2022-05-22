print("Tabla del 10 forma 1")
print("-----------")

for x in range (1,11):
    result = x * 10
    print(x,"*","x","=",result)


print("Tabla del 10 forma 2")
print("-----------")
p=1 #la variable p es nuestro multiplicador
for x in range (10,110,10): #el tercer numero es el incremento
    print(x,"*",p,"=",x)
    p=p+1

print("Tabla del 10 inversa") #Aquí realizamos la tabla del 10 en forma inversa
print("-----------")
for x in range (10,0,-1): #Definimos que x comenzara en 10 y terminará en valor 0, definiendo que que el incremento sea de -1
    mul=10*x
    print("10 x ", x , " = ", mul)

print("Fin de algoritmo")