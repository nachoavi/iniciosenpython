def contador(palabra):
    cont=0
    for caract in palabra:
        cont+=1
    return cont
pa=input("Ingrese la palabra a contar: ")
co=contador(pa)
print(co)