fecha = input("Ingresa tu fecha de nacimiento (dia/mes/año): ")
dia = fecha[:fecha.find("/")]
mesaño = fecha[fecha.find("/")+1:]
mes = mesaño[:mesaño.find("/")]
año = mesaño[mesaño.find("/")+1:]
print("Dia: ",dia)
print("Mes: ",mes)
print("Año: ",año)
