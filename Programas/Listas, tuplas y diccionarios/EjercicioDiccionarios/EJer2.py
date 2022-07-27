print("Datos personales")
nombre=input('Ingrese su nombre: ')
edad=input('Ingrese su edad: ')
direccion=input('Ingrese su ciudad: ')
persona={'nombre':nombre,'edad':edad,'direccion':direccion}

print(persona['nombre'],'tiene',persona['edad'],"y vive en",persona['direccion'])

