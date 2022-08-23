nombre=input("Ingrese su nombre: ")
sexo=input("Ingrese su sexo (M/F): ")

if sexo == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"

else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Tu grupo es el: ",grupo)