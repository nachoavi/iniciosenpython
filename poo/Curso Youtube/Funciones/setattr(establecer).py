#con setattr podemos cambiar el valor de un atributo estableciendo otro

class Persona:  #Definimos que queremos crear una clase con class despues le asignamos el nombre a la clase "Personas"  
    edad = 22 #creamos un atributo que tiene valor de 22
    nombre = "Luis" #creamos un atributo que tiene el valor de string "Luis"

programador = Persona() #creamos un objeto llamado programador y le asignamos la clase persona
print('Antes: ',programador.nombre) #realizamos un print del objeto programador con el atributo nombre
setattr(programador, "nombre", "Sebas") #Con la función setattr podemos establecer otro nombre al objeto programador
#setattr(obj, name, value)

print('Despues: ',programador.nombre) #mostramos con el nombre cambiado
