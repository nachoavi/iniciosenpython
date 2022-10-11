#Encapsulación

class Cliente:
    def __init__(self):
        self.__codigo = 4321 #Para encapsular un atributo antepondremos __ "dos barra baja" antes del nombre del atributo

    def __cuenta(self): #Tambien podemos encapsular un metodo, anteponiendo igual __ "dos barra baja" antes del nombre del metodo
        print("Cuenta de procesamiento") 

    #Una forma de devolver el atributo encapsulado es con un metodo
    def getcodigo(self):
        return self.__codigo  #este metodo simplemente retornará el atributo encapsulado

persona1 = Cliente()


#Para obtener el atributo encapsulado usaremos esta forma
#obeto._nombreclase__nombreatributo dentro de un print

print(persona1._Cliente__codigo)

#Para obtener un metodo encapsulado usatemos la forma
#objero._nombreclase__nombremetodo
persona1._Cliente__cuenta()