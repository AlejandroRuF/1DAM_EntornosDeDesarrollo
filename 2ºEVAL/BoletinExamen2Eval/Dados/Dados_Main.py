from Juego import Juego





while True:
    opcion = input(f"Elige que quieres hacer:\n"
                   f"1- Partida Nueva\n"
                   f"2- Mostrar resultados individuales de la partida\n"
                   f"3- Mostrar resultados totales de la partida\n"
                   f"4- Salir\n")

    if opcion == "1":
        error = True
        while error:
            error=False
            try:
                print("Vamos a jugar a los dados ganara el que tenga la mayor puntuacion")

                nombre1 = input("Ingrese el nombre del jugador 1\n")
                nombre2 = input("Ingrese el nombre del jugador 2\n")

                total_Lanzamientos = int(input("Ingrese el total de lanzamientos\n"))
                juego1 = Juego(nombre1, nombre2, total_Lanzamientos)
                dado1 =int(input("Ingrese el numero de caras del dado 1  (4, 6, 8, 10, 12, 20 o 120)\n"))
                dado2 = int(input("Ingrese el numero de caras del dado 2  (4, 6, 8, 10, 12, 20 o 120)\n"))
                dado3 = int(input("Ingrese el numero de caras del dado 3  (4, 6, 8, 10, 12, 20 o 120)\n"))
                juego1.generar_dados(dado1, dado2, dado3)
                juego1.generar_lanzamientos()
            except Exception as e:
                print(e)
                error=True
    elif opcion=="2":
        juego1.mostrar_resultadosIndividuales()
    elif opcion=="3":
        juego1.mostrar_resultadosTotales()
    elif opcion=="4":
        break
    else:
        print("\nElige la opcion correcta\n")