class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.divición = n1 / n2

n1=int(input("Num 1 = "))
n2=int(input("Num 2 = "))
operación = Calculadora(n1,n2)


print(operación.divición)
