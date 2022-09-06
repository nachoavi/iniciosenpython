class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print("Llamando...")
    def ocupado(self):
        print("Ocupado...")

class Camara:
    def __init__(self):
        pass
    def fotos(self):
        print("Fotografiando..")
    def videos(self):
        print("Grabando...")

class Reproductor:
    def __init__(self):
        pass
    def musica(self):
        print("Reproduciendo Musica...")
    def audiovisual(self):
        print("Reproduciendo Contenido Audiovisual...")

#Esta clase "Smartphone usara la herencia multiple para usar los metodos de las clases que les pasemos"
class Smartphone(Telefono,Camara,Reproductor):
    def __del__(self):  #el metodo __del__ se usa esencialmente para limpiar y optimizar los recursos
        print("Telefono apagado")#en este caso la clase Smartphone ya no sera necesaria y la destruimos con el metodo __del__

movil = Smartphone()
print(dir(movil)) #Nos sirce para identificar los metodos especiales que podemos utilizar con el objeto que hemos creado.

print("Menú principal")
print("(1)Telefono\n(2)Camara\n(3)Reproductor")
opción = int(input(":"))
if opción == 1:
    numero = input("Ingrese el numero: ")
    print(movil.llamar(),numero)
elif opción == 2:
    print("(1)Foto\n(2)Video")
    opción = int(input(":"))
    if opción == 1:
        print(movil.fotos())
    elif opción == 2:
        print(movil.videos())
elif opción == 3:
    print("(1)Musica\n(2)Videos")
    opción = int(input(":"))
    if opción == 1:
        print(movil.musica())
    elif opción == 2:
        print(movil.audiovisual())