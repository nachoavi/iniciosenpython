interes=0.04

saldo=int(input("Ingrese la cantidad de dinero a la cuenta de ahorro: "))

año1=saldo*interes+saldo
print("El saldo del primero año es: ",round(año1,2))

año2=año1*interes+año1
print("El saldo del segundo año es: ",round(año2,2))

año3=año2*interes+año2
print("El saldo del tercer año es: ",round(año3,2))