from click import option


print("===============\n" "Conversor\n" "==========\n" "\n")
print("Menu de opciones\n")

print("Ingresa 1 para convertir de numero a palabra.")
print("Ingresa 2 para convertir de palabra a numero.\n")

option1 = None

while option1 != 1 and option1 != 2:
    option1 = int(input("\n¿Cual es tu opción deseada?: \n"))
    if option1 == 1:
        print("Conversor de numero a palabra\n")
        num_word = int(input("¿Cúal es el número que deseas convertir a palabra?: "))
        if num_word == 1:
            print("UNO")
        elif num_word == 2:
            print("DOS")
        elif num_word == 3:
            print("TRES")
        elif num_word == 4:
            print("CUATRO")
        elif num_word == 5:
            print("CINCO")
        elif num_word == 6:
            print("SEIS")
        elif num_word == 7:
            print("SIETE")
        else:
            print("Numero no resgistrado en el programa, lo sentimos")
    elif option1 == 2:
        print("Conversor de palabra a numero\n")
        word_num = str(input("¿Cual es la palabra que deseas convertir a numero?: "))
        word_num = word_num.lower()  #lower es una funcion que convertira los caracteres de mayuscula a minuscula, asi nuestro programa podra resgistrarlo correctamente.
        if word_num == "uno":
            print("El resultado es:", 1)
        elif word_num == "dos":
            print("El resultado es:", 2)
        elif word_num == "tres":
            print("El resultado es:", 3)
        elif word_num == "cuatro":
            print("El resultado es:", 4)
        elif word_num == "cinco":
            print("El resultado es:", 5)
        elif word_num == "seis":
            print("El resultado es:", 6)
        elif word_num == "siete":
            print("El resultado es:", 7)
        else:
            print("Numero no registrado en el programa, lo sentimos")

print("Gracias por usar")







