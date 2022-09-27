from animales import Animales
from canguro import Canguro
from delfín import Delfin


animalCanguro = Canguro("Pepe", "n/a", 5, 25, "mamifero", 32.5, 5)
animalDelfín = Delfin("Wally", "Nariz de botella", 11, 500, "mamifero", 132.5, 0)

def avanzar(animalElegido):
    if animalElegido == 1:
        kms_avanzados = float(input("Ingrese los kms que va a recorrer: "))
        animalCanguro.avanzar(kms_avanzados)
        print(f"El canguro lleva recorrido {animalCanguro.distancia}")
    elif animalElegido == 2:
        kms_avanzados = float(input("Ingrese los kms que va a recorrer: "))
        animalDelfín.avanzar(kms_avanzados)
        print(f"El delfin lleva recorrido {animalDelfín.distancia}")

def comer(animalElegido):
    if animalElegido == 1:
        kg_comidos = float(input("Ingrese la cantidad de kg que comerá"))
        animalCanguro.comer(kg_comidos)
        print(f"El canguro pesa {animalCanguro.peso}")
    elif animalElegido == 2:
        kg_comidos = float(input("Ingrese la cantidad de kg que comerá"))
        animalDelfín.comer(kg_comidos)
        print(f"El delfin pesa {animalDelfín.peso}")                
def menu():
    op = None
    while op != 0:
        op = int(input("Elija un animal:\n1.Canguro\n2.Delfin\n0.Salir\n> "))
        if op == 1:
            op = int(input("Elija una acción:\n1.Avanzar\n2.Comer\n> "))
            if op == 1:
                animalElegido = 1
                avanzar(animalElegido)
            elif op == 2:
                animalElegido = 1
                comer(animalElegido)
        elif op == 2:
            op = int(input("Elija una acción:\n1.Avanzar\n2.Comer\n> "))
            if op == 1:
                animalElegido = 2
                avanzar(animalElegido)
            elif op == 2:
                animalElegido = 2
                comer(animalElegido)

op = int(input("Bienvenido.. para continuar pulse 1, si desea salir pulse 0\n> "))     
if op == 1:    
    menu()
elif op == 2:
    pass



