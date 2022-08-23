def parimpar(a,b):
    if a !=0 and b != 0:
        if a %2==0 and b %2==0:
            r = ("{} y {} son pares".format(a,b))
            
        elif a %2==0 and b %2==1:
            r = ("{} es par y {} es impar".format(a,b))
            
        elif a %2==1  and b %2==0:
            r = ("{} es impar y {} es par".format(a,b))
    else:
        r = ("Es posible que uno de los numeros ingresados sea cero")
        
    return r
    
        

a=int(input("Ingrese el primer numero entero: "))
b=int(input("Ingrese el segundo numero entero: "))
parimpar(a, b)
print(parimpar(a, b))

