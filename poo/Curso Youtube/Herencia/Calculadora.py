class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
    
    def ingresardato(self):
        self.datos = [int(input("ingresar dato "+str(i+1)+ " = "))for i in range(self.n)]

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def suma(self):
        a,b, = self.datos
        s = a+b
        print("el resultado es: ",s)

    def resta(self):
        a,b, = self.datos
        r = a-b
        print("el resultado es: ",r)
    
    def producto(self):
        a,b, = self.datos
        p = a*b
        print("el producto es: ",p)

    def divición(self):
        a,b, = self.datos
        d = a/b
        print("la divición es: ",d)

class raíz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    
    def cuadrada(self):
        import math
        a, = self.datos
        print("La raíz cuadrada es: ",math.sqrt(a))
        

ejemplo = op_basicas()
ejemplo.ingresardato()
ejemplo.suma()