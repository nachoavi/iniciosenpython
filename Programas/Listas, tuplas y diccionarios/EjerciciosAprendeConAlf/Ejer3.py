asigs=["Matematicas","Química","Historia","Lengua"]
nota=[]
for asig in asigs:
    n=input("Ingrese la nota de "+asig+": ")
    nota.append(n)
for i in range(len(asigs)):
    print("En "+asigs[i]+"has sacado"+nota+":" [i])
    