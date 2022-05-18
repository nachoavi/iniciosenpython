#!/bin/python3
import os
from re import A
from turtle import clear

from regex import B


print()
print("Valle silencioso\n"
"-----------------------\n"
"\n"
"Despiertas en medio de un bosque, no recuerdas por qué terminaste en ese lugar y sientes un dolor punzante en la cabeza.\n"
"Parece que faltan un par de horas para que anochesca, te planteas si levantarte y explorar o quedarte y esperar.\n"
"¿Que decides, levantarte y explorar el lugar o quedarte y esperar?\n")

opcion = None

while opcion != "A" and opcion != "B":
    opcion = input("Opción A: Levantarte y explorar | Opción B: Quedarte y esperar: ")
    

if opcion == "A":
    print()
    print("Te levantas un poco mareado y te pones a caminar en un sendero que estaba proximo al lugar donde despertaste. \n"
    "No logras reconocer nada a tu alrededor pero sientes como si ya hubieces visitado este lugar antes. \n"
    "Continuas caminando y te encuentras al costado del sendero una cabaña entre los arboles que parece deteriorada. \n"
    "¿Te acercas a  pedir ayuda o continuas tu camino?. \n")
    opcion = None
    while opcion != "A" and opcion != "B":
        opcion = input("Opción A: Te acercas a pedir ayuda | Opción B: Continuas tu camino: ")
        
    if opcion == "A":
        print("Al acercarte más y más a la cabaña persibes algo siniestro en ella.\n"
        "Te das cuenta que la puerta principal está abierta, entras y sientes un fuerte estruendo,\n"
        "todo se vuelve blanco y tu cuerpo inerte cae al piso. Has muerto. \n Fin")
    elif opcion == "B":
        print()
        print("Continuas tu camino, la cabaña se ve muy siniestra. \n"
        "Despues de caminar por una hora divisas lo que pareciera ser una ciudad y una espesa niebla empieza a rodearte de a poco"
        "¿Continuas caminando a la ciudad o das media vuelta y vuelves a la cabaña?\n")
        opcion = None
        while opcion != "A" and opcion != "B":
            opcion = input("Opción A: Vuelves a la cabaña | Opción B: Continuas caminando a la ciudad: ")
            
        if opcion == "A":
            print("Al acercarte más y más a la cabaña persibes algo siniestro en ella.\n"
            "Te das cuenta que la puerta principal está abierta, entras y sientes un fuerte estruendo,\n"
            "todo se vuelve blanco y tu cuerpo inerte cae al piso. Has muerto")
        elif opcion == "B":
            print()
            print("Despues de caminar por algunos minutos ves cada vez mas cerca la misteriosa ciudad, divisas un cartel, \n"
            "te acercas y lees \033[1;31m" + "Bienvenidos a Silent Hill \n" "Fin")

elif opcion == "B":
    print("Te quedas dormido, al despertar te encuentras con que ya anocheció,te levantas y sientes que algo se te abalanza "
    "encima y te clava sus garras en tu cuerpo y sus dientes en el rostro. Has muerto \n" "Fin" )
