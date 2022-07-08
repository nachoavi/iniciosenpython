def ingresarTemp():
    dia=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
    temp=[]
    for dia in dia:
        temp.append(float(input("Ingrese la temperatura del dia "+ dia +" :")))
    print(max(temp))
ingresarTemp()