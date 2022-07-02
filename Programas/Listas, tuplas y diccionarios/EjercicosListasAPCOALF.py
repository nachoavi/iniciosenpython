#Ejercicio 1
#Escribir un programa que almacene las asignaturas de un curso (por
#ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y
#la muestre por pantalla.
from this import s


asig1=["Matemáticas","Física","Química","Historia","Lenguaje"]
for x in asig1:
    print(x)

#Ejercicio 2
#Escribir un programa que almacene las asignaturas de un curso (por
#ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y
#la muestre por pantalla el mensaje Yo estudio <asignatura>, donde
#<asignatura> es cada una de las asignaturas de la lista.
asig2=["Matemáticas","Física","Química","Historia","Lenguaje"]
for asig2 in asig2:
    print("Yo estudio " + asig2)




asig3=["Matemáticas","Física","Química","Historia","Lenguaje"]
nota=[]
for asig3 in asig3:
    nota = input("Ingrese la nota de "+ asig3 + ":")
    nota.append(nota)
for x in range(len(asig3)):
    print("En "+asig3[x]+" has sacado" + nota[x])

    

