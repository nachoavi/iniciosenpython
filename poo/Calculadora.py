class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 + n2
        self.producto = n1 * n2
        self.divición = n1 / n2

operación = Calculadora(2,3)

print(operación.producto)
