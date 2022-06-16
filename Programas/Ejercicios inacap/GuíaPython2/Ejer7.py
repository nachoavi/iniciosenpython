#Solicitar datos de entrada
import math

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

#Proceso de aplicación de formula, comenzando con lo del interior de la raiz cuadrada
d = (b*b)-4*a*c

#Comprobación y resultado
if d<0:
    print("No hay solución para numeros negativos")
else:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print("Soluciones")
    print("Solución 1: ",x1)
    print("Solución 2: ",x2)
    



