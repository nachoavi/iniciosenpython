divisas={'Euros':'€','Dollar':'$','Yen':'¥'}

print("Signos de divisas\n")
print("A)Euros\nB)Dolares\nC)Yenes\n")
op=input("Seleccione la divisa: ")
if op == "A" or op == "a":
    print("El signo es:",divisas['Euros'])
elif op == "B" or op == "b":
    print("El signo es: ",divisas['Dollar'])
elif op == "C" or op == "c":
    print("El signo es: ",divisas["Yen"])
else:
    print("Opción ingresada invalida") 