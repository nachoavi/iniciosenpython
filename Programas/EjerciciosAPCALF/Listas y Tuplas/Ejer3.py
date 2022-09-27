asignaturas = ["Matematicas","Fisica","Química","Historia","Lengua"]
notas = []

for i in asignaturas:
    nota = float(input(f"Ingrese la nota que se ha sacado en {i}: "))
    notas.append(nota)

for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado ",notas[i])

