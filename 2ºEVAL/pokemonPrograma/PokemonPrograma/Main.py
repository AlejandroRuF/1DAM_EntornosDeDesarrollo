from Pokemon import Pokemon
from Entrenador import Entrenador
from Almacen import Almacen

lista_Entrenadores = []
lista_Almacen = []
lista_Pokemon = []

print(f"Bienvenido entrenador vamos a crear tu ficha. Para registrarte en el sistema por favor introduce tu nombre"
      f" acontinuacion")
nombre_entrenador = input()

en1 = Entrenador(nombre_entrenador)

print(f"Muy bien {nombre_entrenador} ya tienes acceso al sistema de almacenes y cajas que deseas realizar primero:")

lista_pokk = [Pokemon("Dratini", "DRAGON", 18, 30, "Dragonair", 50, "Dragonite", "en1.get_nombre()"),
Pokemon("Cubone", "Fuego", 28, 40, "Marowak", 50, "Alolan Marowak", en1.get_nombre())]
al1 = Almacen(en1, lista_pokk)
pokemon_Salvajes = [Pokemon("Charmander", "Fuego", 15, 16, "Charmeleon", 45, "Charizard", en1.get_nombre()),
                                Pokemon("Bulbasaur", "PLANTA", 18, 32, "Ivysaur", 50, "Venusaur", en1.get_nombre()),
                                Pokemon("Squirtle", "AGUA", 15, 35, "Wartortle", 45, "Blastoise", en1.get_nombre()),
                                Pokemon("Jigglypuff", "AGUA", 20, 30, "Wigglytuff", 40, "Wigglytuff Gigantamax",
                                        en1.get_nombre()),
                                Pokemon("Eevee", "FUEGO", 22, 35, "Vaporeon", 50, "Jolteon", en1.get_nombre()),
                                Pokemon("Gastly", "DRAGON", 25, 36, "Haunter", 45, "Gengar", en1.get_nombre())]

while True:
    print(f"Elige una de las siguientes opciones:\n"
          f"1- Subir nivel de un pokemon\n"
          f"2- Capturar pokemon\n"
          f"3- Sacar pokemon\n"
          f"4- Dejar Pokemon\n"
          f"5- Mostrar pokemon en el almacen\n"
          f"6- Mostrar pokemon del entrenador\n"
          f"7- Salir\n")

    try:

        opcion = input()
        if opcion == "1":

            print("Cual de los pokemon que llevas encima quieres evolucionar\n")
            en1.mostrar_lista()
            num = input(f"Selecciona el numero del pokemon elegido\n")
            if num.isnumeric():
                nivel = input("Cuantos niveles quiere que suba tu pokemon\n")
                if nivel.isnumeric():
                    en1.get_lista_pokemon()[int(num) - 1].subirNivel(int(nivel))

            else:
                print("El dato introducido no es valido")
        elif opcion == "2":

            while True:
                op2 = input(f"1- Buscar tu propio pokemon\n"
                        f"2- Comprar uno de los pokemon disponibles\n"
                        f"3- Salir\n")

                if op2 == "1":
                    print("Has encontrado un pokemon podrias decirme sus datos?")

                    nomp = input("Nombre del pokemon: ")
                    tipo = input("Introduce el tipo del pokemon solo puede ser (FUEGO, AGUA, PLANTA, ELECTRICO, "
                                 "DRAGON): ")
                    nivel = int(input("Introduce el nivel del pokemon: "))
                    nivel_Evolucion2 = int(input("Introduce el nivel de la 2º Evolucion (No puede ser inferior al "
                                                 "nivel actual): "))
                    nombre_Evolucion2 = input("Introduce el nombre de la 2º Evolucion del Pokemon: ")
                    nivel_Evolucion3 = int(input("Introduce el nivel de la 3º Evolucion (No puede ser inferior al "
                                                 "nivel de la 2º Evolucion): "))
                    nombre_Evolucion3 = input("Introduce el nombre de la 3º Evolucion del Pokemon: ")

                    al1.capturar_pokemon(
                        Pokemon(nomp, tipo, nivel, nivel_Evolucion2, nombre_Evolucion2, nivel_Evolucion3,
                                nombre_Evolucion3, en1.get_nombre()))

                elif op2 == "2":
                    print(f"Que pokemon quieres comprar")
                    for i in range(len(pokemon_Salvajes)):
                        print(f"{i + 1}: {pokemon_Salvajes[i]}")
                    pok = int(input("Introduce el numero del pokemon que quieres\n"))
                    al1.capturar_pokemon(pokemon_Salvajes[pok-1])
                    pokemon_Salvajes.pop(pok-1)

                elif op2 == "3":
                    break
                else:
                    print("Seleciona una de las opciones disponibles")

        elif opcion == "3":
            print(f"Elige el pokemon que quieres sacar de la caja")
            al1.mostrar_Alacen()
            ind = int(input("Que pokemon quieres sacar\n"))
            al1.sacar_pokemon(ind)

        elif opcion == "4":
            print(f"Elige el pokemon que quieres guardar en la caja")
            al1.mostrar_pokemonEntrenador()
            ind = int(input("Que pokemon quieres sacar\n"))
            al1.dejar_pokemon(ind)

        elif opcion == "5":
            al1.mostrar_Alacen()

        elif opcion == "6":
            al1.mostrar_pokemonEntrenador()

        elif opcion == "7":
            break

        else:
            print("Elige bien la opcion")


    except Exception as e:
        print(e)
