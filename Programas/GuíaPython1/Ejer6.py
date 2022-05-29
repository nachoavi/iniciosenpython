n1 = float(input("Ingrese nota 1: "))
if n1 >= 1 and n1 <=7:
    n2 = float(input("Ingrese nota 2: "))
    if n2 >= 1 and n2 <=7:
        n3 = float(input("Ingrese nota 3: "))
        if n3 >= 1 and n3 <=7:
            sum = n1 + n2 + n3
            prom = sum / 3
            print("El promedio de notas es: ",prom)
        else:
            print("Fuera de rango")    
    else:
        print("Fuera de rango")        
else:
    print("Fuera de rango")            
