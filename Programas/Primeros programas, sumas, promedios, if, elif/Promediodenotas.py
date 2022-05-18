#Este es un programa que sacará nuestro promedio de notas

print("\033[4;33m" + "Este programa calculará tu promedio y te dira si aprovaste el ramo o no")
print("\033[2;33m" + "(Recuerda ingresar tus notas como enteros, ejemplo: 40, 50 o 70)")
student_name = input("\033[0;37m" + "Ingresa tu nombre: ")
clas1 = int(input(student_name + " ingresa tu primera nota: "))
clas2 = int(input(student_name + " ingresa tu segunda nota: "))
clas3 = int(input(student_name + " ingresa tu tercera nota: "))
clas4 = int(input(student_name + " ingresa tu cuarta nota: "))

promedy = (clas1 + clas2 + clas3 + clas4) / 4
promedy = int(promedy)


if promedy >= 39.95:
    print("\033[1;34m" + student_name + ", ¡Felicitaciones, Aprobaste! tu promedio es: ", promedy)
else:
    print("\033[1;31m" + student_name + ", lamentablemente reprobaste, tu promedio es: ", promedy)
