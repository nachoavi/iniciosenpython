from Calculadora import *

objeto = op_basicas()
objeto.ingresardato()
objeto.suma()


#isinstance(obj, class_or_tuple) nos permite saber si el objeto esta trabajando con la clase
print(isinstance(objeto, op_basicas)) 

#issubclass(cls, class_or_tuple) nos permite saber si una clase es hija o pertenece a otra
print(issubclass(op_basicas, Calculadora))