import random

def jugar():
    intentos = 0
    numero_aleatorio = random.randint(1,10)

    print("Bienvenido a Adivina el Numero")
    print("Estoy pensando en un numero del 1 al 10")
    print("Adivina cuál es")
    print("Solamente tienes 5 intentos")
    while intentos < 5:
        try:
            adivinanza = int(input("El numero es: "))
        except ValueError:
            print("Ese no es un numero valido")
        else:
            if adivinanza == numero_aleatorio:
                print("Adivinaste!!!")
                jugar_nuevamente = input("Jugar de nuevo? si/no: ")

                if jugar_nuevamente.lower() == "si":
                    jugar()
                else:
                    break
            elif numero_aleatorio > adivinanza:
                print("Fallaste, mi numero es mayor")
            else:
                print("Fallaste, mi numero es menor")

            intentos += 1
            print("Intento {}/5".format(intentos))
    else:
        print("Se te acabaron los intentos")
        print("Gracias por jugar")
        jugar_nuevamente = input("Jugar de nuevo? si/no: ")

        if jugar_nuevamente.lower() == "si":
            jugar()

jugar()