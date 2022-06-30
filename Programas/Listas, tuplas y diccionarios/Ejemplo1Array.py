option_1 = None
while option_1 not in ["A","B","C","D","a","b","c","d"]: #definimos dentro de un array o lista una serie de letras que seran nuestras opciones y mientras la variable option_1 tenga como valor alguna de esas opciones se repetira en bucle lo de abajo.
    option_1 = input("Ingrese una opción entre A y D: ")#Si la variable option_1 muestra un valor que esta dentro del array ["A", "B", ...] entonces el "not in" seria falso y nos sacaria del bucle.
    if option_1 == "A" or option_1 == "a":
        print("Elegiste muy bien")
    elif option_1 == "B" or option_1 == "b":
        print("Elegiste bien")
    elif option_1 == "C" or option_1 == "c":
        print("Elegiste mal")
    elif option_1 == "D" or option_1 == "d":
        print("Elegiste muy mal")

