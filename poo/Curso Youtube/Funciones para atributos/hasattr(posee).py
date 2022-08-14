#La función hasattr sirve para verificar si la variable posee un atributo


class Persona:
    edad = 22
    nombre = "Luis"

doctor = Persona()
print("el doctor tiene nombre?", hasattr(doctor, "edad")) #hasattr = poseeatributo?