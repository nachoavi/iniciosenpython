from AnimalesPadre import Animales
from Canguro import Canguro
from Cocodrilo import Cocodrilo
from Delfin import Delfin
from Gallo import Gallo



canguro = Canguro("Tony", "n/a", 5, 25, "mamífero", 32.5,100)
cocodrilo = Cocodrilo("Pepe", "n/a", 50, 950, "Réptil", 50.6,80)
delfin = Delfin("Wally", "Naris de botella", 11, 500, "Mamifero", 132.5,0)
gallo = Gallo("Claudio", "Broiler", 2, 4.3, "ave", 5.2,0)

    


print("Bienvenido.. para continuar pulse 1, si desea salir pulse 0")
x=0
while x == 0:
    op=input("> ")
    if op == "1":
        j=0
        while j == 0:
            print("Elija un animal:\n1. Canguro \n2. Cocodrilo\n3. Delfin\n4. Gallo\n5. Salir")
            op=input("> ")
            if op == "1":
                
                print("Elija una acción que quiera que realice: \n1. Avanzar\n2. Comer \n3. Dar puñetazo")
                op=input("> ")
                if op == "1":
                    kmavanzados = int(input("Ingrese la cantidad kms. que va a recorrer: "))
                    canguro.avanzar(kmavanzados)
                    
                elif op == "2":
                    kilogramosingeridos = int(input("Ingrese la cantidad kg. que va a comer: "))
                    canguro.comer(kilogramosingeridos) 

                elif op == "3":
                    puñetazo = int(input("Indique la fuerza del puñetazo: "))
                    canguro.darPuñetazo(puñetazo)
                     

            elif op == "2":
                print("Elija una acción que quiera que realice: \n1. Avanzar\n2. Comer\n3. Morder Piedra")
                op=input("> ")
                if op == "1":
                    kmavanzados = int(input("Ingrese la cantidad kms. que va a recorrer: "))
                    cocodrilo.avanzar(kmavanzados)
                elif op == "2":
                    kilogramosingeridos = int(input("Ingrese la cantidad kg. que va a comer: "))
                    cocodrilo.comer(kilogramosingeridos)  
                
                elif op == "3":
                    print("¿Seguro quieres que muerda una piedra? 1.Si/2.No")
                    elección=input("> ")
                    cocodrilo.morderPiedra(elección)

                    
            elif op == "3":
                print("Elija una acción que quiera que realice: \n1. Avanzar\n2. Comer\n3. Saltar")
                op=input("> ")
                if op == "1":
                    kmavanzados = int(input("Ingrese la cantidad kms. que va a recorrer: "))
                    delfin.avanzar(kmavanzados)
                elif op == "2":
                    kilogramosingeridos = int(input("Ingrese la cantidad kg. que va a comer: "))
                    delfin.comer(kilogramosingeridos) 
                elif op == "3":
                    salto = float(input("Ingrese la cantidad de saltos que dará el delfin: "))
                    delfin.saltar(salto)

            elif op == "4":
                print("Elija una acción que quiera que realice: \n1. Avanzar\n2. Comer\n3. Conquistar el Mundo")
                op=input("> ")
                if op == "1":
                    kmavanzados = int(input("Ingrese la cantidad kms. que va a recorrer: "))
                    gallo.avanzar(kmavanzados)
                elif op == "2":
                    kilogramosingeridos = int(input("Ingrese la cantidad kg. que va a comer: "))
                    gallo.comer(kilogramosingeridos)  
                
                elif op == "3":
                    gallo.conquistarelMundo()

            elif op == "5":
                print("Saliendo...")
                exit()
                                 
    elif op == "0":
        print("Saliendo...")
        x=1


_cls