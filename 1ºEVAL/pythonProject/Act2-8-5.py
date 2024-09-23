import random

numero = int(random.randrange(0, 1000))
entrada = int(input("Adivina el nunero (Pista: Esta entre el 0 y el 1000)\n"))
contador = 1
while numero != entrada:
    if entrada < numero:
        print(f"El nunero es mayor")
        contador += 1

    if entrada > numero:
        print(f"El numero es menor")
        contador += 1

    entrada = int(input())

    if entrada == numero:
        print(f"Felicidades has advinado el numero y tan solo en {contador} intentos!!!")
