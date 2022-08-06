peso=float(input("Ingrese su peso en kg: "))
estatura=float(input("Ingrese su estatura en metros: "))

imc= round(peso/(estatura**2),2)

print("Tu indice de masa corporal es: ",imc)