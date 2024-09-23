import random


def dados():
    return int(random.randint(1, 6))


def veces(lanzamientos):
    resultados = []

    for i in range(0, lanzamientos, 1):
        resultados.append(dados())
    return resultados


def ganadores(jug1, jug2, ganad):
    pos = 1
    vecesj1 = 0
    vecesj2 = 0
    win = ""
    for i in ganad:
        if i % 2 == 0:
            print(f"Lanzamiento {pos} : El dado es un {i}")
            print(f"Gana {jug1}")
            vecesj1 += 1
            print(f"Marcador: {jug1} {vecesj1} - {jugador2} {vecesj2}\n")
        else:
            print(f"Lanzamiento {pos} : El dado es un {i}")
            print(f"Gana {jug2}")
            vecesj2 += 1
            print(f"Marcador: {jug1} {vecesj1} - {jugador2} {vecesj2}\n")
        pos += 1
    if vecesj1 > vecesj2:
        win = jug1
    elif vecesj1 < vecesj2:
        win = jug2
    print("Se han acabado todos los lanzamientos\n")

    if win == "":
        print(f"Empate\n"
              f"Marcador: {jug1} {vecesj1} - {jugador2} {vecesj2}\n")
    else:
        print(f"Ganador : {win}\n"
              f"Marcador: {jug1} {vecesj1} - {jugador2} {vecesj2}\n")


jugador1 = input("Cual es el nombre del jugador 1\n")
jugador2 = input("Cual es el nombre del jugador 2\n")
lanzamiento = int(input("Cuantas veces quieres lanzar el dado\n"))
gana = veces(lanzamiento)
ganadores(jugador1, jugador2, gana)
