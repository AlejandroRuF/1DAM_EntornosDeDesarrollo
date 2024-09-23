from Estancia import Estancia
from Vivienda import Vivienda

creado = False
while True:
    try:

        opcion = input(f"**MENU DE OPCIONES**\n"
                       f"1- Crear vivienda \n"
                       f"2- Añadir estancia a la vivienda\n"
                       f"3- Borrar estancia de la vivienda\n"
                       f"4- Mostrar Estancias\n"
                       f"5- Mostrar resumen de la vivienda\n"
                       f"6- Salir\n")

        if opcion == "1":
            nombre = input(f"Selecciona un nombre para la vivienda que vamos a crear: ")
            num = int(input(f"Indica el número maximo de estancias que la vivienda puede albergar:  "))

            casa1 = Vivienda(nombre, num)
            creado = True

        elif opcion == "2":
            if creado:
                tipo = input("Indica el tipo de estancia (M(Comedor).H(Habitación),C(Cocina),B(Baño)): ")
                m2 = int(input("Indica el número de metros cuadrados: "))
                ventanas = input("Tiene ventanas? (S/N): ")
                if ventanas.upper() in ["SI", "S", "NO", "N"]:
                    if ventanas.upper() in ["SI", "S"]:
                        bVentanas = True
                    else:
                        bVentanas = False
                casa1.setEstancias(Estancia(tipo, m2, bVentanas))
            else:
                print("Para añadir una estancia debes crear primero una vivienda")

        elif opcion == "3":
            casa1.mostrar()
            bor = int(input("Elige la estancia que quieres borrar:  "))
            casa1.quitarestancia((bor - 1))

        elif opcion == "4":
            casa1.mostrar()

        elif opcion == "5":
            casa1.legalidad()

        elif opcion == "6":
            break

        else:

            print("Por favor selecciona una de las opciones indicadas")

    except Exception as e:
        print(e)
