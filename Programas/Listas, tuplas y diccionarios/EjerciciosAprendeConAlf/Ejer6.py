asigs=["Matématica","Fisica","Química","Historia","Lengua"]
aprovada=[]
for i in asigs:
    n=float(input("Ingrese la nota de "+i+":"))
    if n >=4:
        aprovada.append(i)
for i in aprovada:
    asigs.remove(i)
print("Tienes que repetir "+ str(asigs))