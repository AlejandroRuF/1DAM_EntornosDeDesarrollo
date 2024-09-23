import random
import time

numero = 0
nombre = ""


def intro():
    global numero
    global nombre
    nombre = input("Dime tu nombre: ")
    print(nombre + ", vamos a jugar a un juego. Estoy pensando un número entre 1 y 200")
    numero = random.randint(1, 200)
    time.sleep(.5)
    print("Adelante. Adivínalo!")


def buscar():
    global numero, numJugado
    global nombre
    intentos = 0
    while intentos < 6:
        time.sleep(.25)
        enter = input("Adivina: ")
        try:
            numJugado = int(enter)

            if 200 >= numJugado >= 1:
                intentos = intentos + 1

                if numJugado != numero:
                    if numJugado < numero:
                        print("Demasiado bajo")
                    elif numJugado > numero:
                        print("Demasiado alto")
                    time.sleep(.5)
                    print("Inténtalo otra vez!")

                else:
                    intentos = str(intentos)
                    print('¡Enhorabuena ' + str(nombre) + '! Adivinaste el número en ' + intentos + ' intentos!')
                    break
            else:

                print("Ese número no está en el rango!")
                time.sleep(.25)
                print("Introduce un número entre 1 y 200")

        except:
            print("Creo que " + enter + " no es un número.")

    if numJugado != numero:
        print('Intentos terminados. El número era ' + str(numero))


otra = "sí"
while otra.upper() in ["S", "SÍ", "SI"]:
    intro()
    buscar()
    otra = input("¿Quieres jugar otra vez?")
