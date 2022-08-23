ingredientesnormales=["Peperoni","Jamón","Salmón"]
ingredientesveggie=["Pimiento","Tofu"]

tipopizza = input("Tipo de pizza: Normal(N) o Veggie (V): ")

if tipopizza == "N" or tipopizza == "n":
    print("Elija un ingrediente: ")
    for i in range(0,len(ingredientesnormales)):
        print(f"{i+1}:",ingredientesnormales[i])
    ingredienteselec=int(input(":"))
    if ingredienteselec == 1:
        print("La pizza elejida es normal y us ingredientes són: Mozzarella,tomate y Peperoni")
    elif ingredienteselec == 2:
        print("La pizza elejida es normal y us ingredientes són: Mozzarella,tomate y Jamón")
    elif ingredienteselec == 3:
        print("La pizza elejida es normal y us ingredientes són: Mozzarella,tomate y Salmón")

elif tipopizza == "V" or tipopizza == "v":
    print("Elija un ingrediente: ")
    for i in range(0,len(ingredientesveggie)):
        print(f"{i+1}:",ingredientesveggie[i])
    ingredienteselec=int(input(":"))
    if ingredienteselec == 1:
        print("La pizza elejida es Veggie y us ingredientes són: Mozzarella,tomate y Pimiento")
    elif ingredienteselec == 2:
        print("La pizza elejida es Veggie y us ingredientes són: Mozzarella,tomate y Tofu")

              