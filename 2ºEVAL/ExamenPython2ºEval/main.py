from flota import Flota
from nau import NauEspacial

creada = False
while True:
    try:
        print("**Menú de opciones**")
        opcion = input("1 - Crear Flota\n"
                       "2 - Agregar nave a la flota\n"
                       "3 - ¿Esta completa?\n"
                       "4 - Mostrar lista d naves\n"
                       "5 - Mostrar Energia total de la flota\n"
                       "6 - Salir\n")

        if opcion == "1":
            try:
                nom = input("Introduce el nombre de la flota (Mínimo 10 caracteres máximo 80)\n")
                f1 = Flota(nom)
                print("Flota creada")
                creada = True
            except Exception as e:
                print(e)

        elif opcion == "2" and creada:
            navok = False
            while not navok:
                try:
                    nom = input("Introduce el nombre de la nave introduce 000 para salir\n")
                    if nom == "000":
                        break
                    tipo = input("Introduce el tipo de nave a agregar 'B'(Batalla), 'R'(Reconocimiento), "
                                 "'T'(Transporte), 'O'(Bombardero)\n")
                    capacidad = int(input("Introduce la capacidad de la nave en MegaJulios mínimo 1 máximo 1000\n"))
                    comb = int(input("Cual es el porcentaje de deposito lleno de la nave(Todas las naves recien"
                                     " salidas del concesionario vienen con un 10% del deposito lleno"
                                     " por lo tanto el máximo a rellenar seria el 90%)\n"))

                    f1.agregarNave(NauEspacial(nom, tipo, capacidad))
                    f1.getNaves()[-1].modificarNivelEnergia(comb)
                    navok = True

                except Exception as e:
                    print(e)

        elif opcion == "3" and creada:
            f1.cuentasnav()
            if f1.completa():
                print("La flota es una flota completa")
            else:
                print("La flota no está completa")

        elif opcion == "4" and creada:
            f1.mostrarFlota()

        elif opcion == "5" and creada:
            f1.mostrarEnergia()

        elif opcion == "6":
            break
        elif not creada and opcion in "2345":
            print("Para acceder a esa opcion debes crear primero una flota")
        else:
            print("Elige una opcion válida por favor")

        # nav = NauEspacial("Enterprise", "B", 500)
        # nav1 = NauEspacial("naaa", "R", 999)
        # nav2 = NauEspacial("Nbbb", "T", 400)
        # nav3 = NauEspacial("NCCCC", "O", 250)
        # f1.agregarNave(nav1)
        # f1.agregarNave(nav2)
        # f1.agregarNave(nav3)
        # f1.agregarNave(nav)

    except Exception as e:
        print(e)
