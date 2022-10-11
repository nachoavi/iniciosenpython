#propiedades()

class Empleados:
    def __init__(self,nombre,salario):
        self.__nombre = nombre #anteponemos __ para dar a entender que estamos encapsulando el atributo
        self.__salario = salario

    def __getnombre(self): #establecemos metodos para obtener el atributo encapsulado
        return self.__nombre
    def __getsalario(self):
        return self.__salario

    def __setnombre(self,nombre): #establecemos otro metodo para setear el atributo encapsulado
        self.__nombre =  nombre
    def __setsalario(self,salario):
        self.__salario = salario

    def __delnombre(self): #y establecemos otro metodo para borrar el atributo encapsulado
        del self.__nombre
    def __delsalario(self):
        del self.__salario

    #para añadir propiedades a los atributos de una clase:
    #estos atributos los utilizaremos solo cuando sea necesario o lo requiera el programa
    nombre = property(fget= __getnombre,fset= __setnombre,fdel= __delnombre)
    salario = property(fget= __getsalario,fset= __setsalario,fdel= __delsalario)

trabajador1 = Empleados("Pepe",2000) #Como ejemplo cramos un objeto con el nombre pepe y 2000 de salario

trabajador1.nombre = "Victor" #Aqui modificamos el atributo nombre y pasará a ser "Victor" todo esto funcionando gracias a las propiedades

print(trabajador1.nombre)
