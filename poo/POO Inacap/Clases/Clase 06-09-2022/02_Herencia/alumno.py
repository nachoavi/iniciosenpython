class Alumno:

    # Constructor: a este método llama Python cuando creamos un objeto de la clase (a = Alumno())
    # Está esperando recibir 4 parámetros (no debes contar el parámetro self)
    # De esta forma estamos definiendo los atributos de la clase, y a la vez
    # asignándole los valores que vendrán por los parámetros
    def __init__(self, id, nombre, apellido, edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad