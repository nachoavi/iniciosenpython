from alumno import Alumno
from profesor import Profesor
from asignatura import Asignatura
from notas import Notas

print("PROGRAMA ESCUELA")
# Creo una lista vacía que se llenará por cada creación de alumno
listaAlumnos = []
listaProfesor = []
listaAsignaturas = []
listaNotas = []

# Creo opcion con un valor que no sea 0 (cualquiera), para que entre al WHILE al menos una vez
opcion = -1
while opcion != 0:
    # Mostramos menú para seleccionar alguna de las opciones
    print("Ingrese una opción: ")
    print("1. Crear Alumno")
    print("2. Crear Profesor")
    print("3. Mostrar Lista de Alumnos")
    print("4. Mostrar Lista de Profesores")
    print("5. Crear Asignatura")
    print("6. Mostrar Lista de Asignaturas")
    # Para insertar una nota, deben ser capaces de enlazar Alumno, Profesor y Asignatura.
    # Esto quiere decir que tendrán que mostrar una lista de datos al usuario para que elia..
    print("7. Insertar una nota")
    print("8. Mostrar las notas de todos los alumnos")
    print("9. Mostrar todas las notas de un alumno")
    print("0. Salir")
    # Capturamos lo que se ingrese por teclado y transformamos a número entero
    opcion = int(input())

    if opcion == 1:
        nombre = input("Ingrese nombre del alumno: ")
        apellido = input("Ingrese apellido del alumno: ")
        nivelConocimiento = int(input("Nivel conocimiento (1-100): "))
        # Creo el objeto con los valores capturados por teclado
        alu = Alumno(nombre, apellido, nivelConocimiento)
        print("Alumno creado exitosamente!")
        # Agregamos a la lista un objeto Alumno
        listaAlumnos.append(alu)
    elif opcion == 2:
        nombre = input("Ingrese nombre del profesor: ")
        apellido = input("Ingrese apellido del profesor: ")
        evaluacionDocente = float(input("Ingrese nota de evaluación docente: "))
        profe = Profesor(nombre, apellido, evaluacionDocente)
        print("Profesor creado exitosamente!")
        listaProfesor.append(profe)
    elif opcion == 3:
        # Para mostrar los datos de una lista SIEMPRE tenemos que recorrerla
        for alumnito in listaAlumnos:
            print("Nombre: {0}, Apellido: {1}, Conocimiento: {2}"
                  .format(alumnito.nombre, alumnito.apellido, alumnito.conocimiento))
    elif opcion == 4:
        for i in listaProfesor:
            print(f'Nombre: {i.nombre}\nApellido: {i.apellido}\nEvaluación Docente: {i.evaluacionDocente}',end="\n\n")
    
    elif opcion == 5:
        id = int(input("Ingrese la id de la asignatura: "))
        nombre = input("Ingrese el nombre de la asignatura: ")
        newAsignatura = Asignatura(id, nombre)
        listaAsignaturas.append(newAsignatura)
    elif opcion == 6:
        for i in listaAsignaturas:
            print(f'ID: {i.id}\nNombre: {i.nombre}',end="\n\n")

    elif opcion == 7:
        print('Selecciones un alumno de la lista con su numero asignado')
        indice = 0
        for i in listaAlumnos:
            print(f'{indice}) Nombre: {i.nombre} Apellido: {i.apellido}')
            indice += 1
        indiceSeleccionado = int(input("> "))
        alumnoSeleccionado = listaAlumnos[indiceSeleccionado]

        print("Selecciones el profesor de la lista con su numero asignado")
        indiceProfe = 0
        for i in listaProfesor:
            print(f'{indiceProfe}) Nombre: {i.nombre} Apellido: {i.apellido}')
            indiceProfe += 1
        indiceSeleccionado = int(input("> "))
        profesorSeleccionado = listaProfesor[indiceSeleccionado]

        print('Seleccione la asignatura correspondiente')
        indiceAsig = 0
        for i in listaAsignaturas:
            print(f'{indiceAsig}) Nombre: {i.nombre}')
            indiceAsig += 1
        indiceSeleccionado = int(input('> '))
        asignaturaSeleccionada = listaAsignaturas[indiceSeleccionado]

        nota1 = int(input("Ingrese la nota 1: "))
        nota2 = int(input("Ingrese la nota 2: "))
        nota3 = int(input("Ingrese la nota 3: "))

        notas = Notas(alumnoSeleccionado, profesorSeleccionado, asignaturaSeleccionada, nota1, nota2, nota3)
        listaNotas.append(notas)

    elif opcion == 8:
        for i in listaNotas:
            print(f'Alumno: {i.alumno.nombre,} / Profesor: {i.profesor.nombre} / Asignatura: {i.asignatura.nombre} / Nota 1: {i.nota1} / Nota 2: {i.nota2} / Nota 3: {i.nota3}',end='\n\n')

    elif opcion == 9:
        print("Seleccione el alumno con su numero correspondiente")
        indiceAlumno = 0
        for i in listaAlumnos:
            print(f'{indiceAlumno}) / Nombre: {i.nombre} / Apellido: {i.apellido}')
        indiceSeleccionado = int(input("> "))
        alumnoSeleccionado = listaAlumnos[indiceSeleccionado]

        for i in listaNotas:
            if i.alumno == alumnoSeleccionado:
                print(f'Alumno: {i.alumno.nombre} / Profesor: {i.profesor.nombre} / Asignatura: {i.asignatura.nombre} / Nota 1: {i.nota1} / Nota 2: {i.nota2} / Nota 3: {i.nota3}',end='\n\n')
        


    elif opcion == 0:
        pass
    else:
        print("Opción ingresada no válida")

print("FIN DEL PROGRAMA")
#print("Nombre: {0}, Apellido: {1}, Conocimiento: {2}".format(a.nombre, a.apellido, a.conocimiento))
 