from random import randint #Importamos la función randint de la libreria random
import os


HPINICIAL_BERSERK = 150 #definimos en una constante la vida inicial de nuestro Berserker
HPINICIAL_WOLF = 120 #definimos en una constante la vida inicial de nuestro Lobo

hp_berserk = HPINICIAL_BERSERK
hp_wolf = HPINICIAL_WOLF

HP_BAR = 20


print("Eres un berseker que camina por el bosque y de la nada un lobo salvaje aparece y te ataca, empieza el combate:\n")
while hp_berserk >0 and hp_wolf >0: #Definimos que mientras las variables sean mayor a 0 el combate continua.
    attack_wolf = randint(1, 2) #Definimos que la variable attack_wolf (Ataque de lobo) sea un numero random entre 1 y 2
    if attack_wolf == 1:
        print("Lobo realiza un ataque normal\n")
        hp_berserk -= 7  #Definimos que el ataque normal quite 7 puntos de salud al berserker
    else:
        print("Lobo realiza un ataque potente\n")
        hp_berserk -= 15 #Definimos que el ataque potente 15 puntos de salud al berserker

    hpbar_wolf = int(hp_wolf * HP_BAR / HPINICIAL_WOLF) #Definimos una variable (hpbar_wolf) con el resultado del porcentaje hp_wolf * 10 / HPINICAL_WOLF para hacer una "barra de salud"
    print("HP Wolf:       [{}{}] ({}/{})".format("#" * hpbar_wolf, " " * (HP_BAR - hpbar_wolf), hp_wolf, HPINICIAL_WOLF)) #Mostramos por pantalla la "Barra de salud"

    hpbar_berserk = int(hp_berserk * HP_BAR / HPINICIAL_BERSERK)
    print("HP Berserk:    [{}{}] ({}/{})".format("#" * hpbar_berserk, " " * (HP_BAR - hpbar_berserk), hp_berserk, HPINICIAL_BERSERK))

    input("Pulsa enter para continuar...\n")
    os.system ("clear")

    attack_berserk = None
    while attack_berserk != "A" and attack_berserk !="B" and attack_berserk != "C" and attack_berserk != "D": #Definimos que mientras la variable attack_berserk sea diferente a A, B, C o D, ejecutara en bucle el codido debajo
        print("Es tu turno de atacar:")
        attack_berserk = str(input("Ataque normal (A), Ataque potente (B), Ataque debastador (C), Pasar ataque (D): "))
        if attack_berserk == "A":
            print("Realizaste un ataque normal\n")
            hp_wolf -= 15
        elif attack_berserk == "B":
            print("Realizaste un ataque potente\n")
            hp_wolf -= 25
        elif attack_berserk == "C":
            print("Realizaste un ataque devastador\n")
            hp_wolf -= 35
        elif attack_berserk == "D":
            print("Has decidido no atacar\n")
            hp_wolf -= 0

        hpbar_wolf = int(hp_wolf * HP_BAR / HPINICIAL_WOLF)
        print("HP Wolf:       [{}{}] ({}/{})".format("#" * hpbar_wolf, " " * (HP_BAR - hpbar_wolf), hp_wolf, HPINICIAL_WOLF))

        hpbar_berserk = int(hp_berserk * HP_BAR / HPINICIAL_BERSERK)
        print("HP Berserk:    [{}{}] ({}/{})".format("#" * hpbar_berserk, " " * (HP_BAR - hpbar_berserk), hp_berserk, HPINICIAL_BERSERK))

        input("Pulsa enter para continuar...\n")
        os.system ("clear")
if hp_berserk > hp_wolf: #Definimos que si la vida del berserker es mayor a la del lobo entonces imprimimos por pantalla el mensaje:
    print("\033[1;31m" + "Has decapitado al lobo")
else:
    print("El lobo te ha arrancado un brazo, has muerto desangrado")



