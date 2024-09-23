import dado


class Juego:
    __jugador1 = ""
    __jugador2 = ""
    __lanzamientos = 0

    def __init__(self, jugador1, jugador2, caras1, caras2, caras3, lanzamientos, intermedios):
        # Valido los nombres de los jugadores y los números de lanzamientos en los setters
        self.set_jugador1(jugador1)
        self.set_jugador2(jugador2)
        self.set_lanzamientos(lanzamientos)
        # Creo 3 dados cada uno con las caras que haya indicado el usuario
        self.dado1 = dado.Dado(caras1)
        self.dado2 = dado.Dado(caras2)
        self.dado3 = dado.Dado(caras3)
        # Me guardo en un atributo booelano si necesito o no ver los datos intermedios
        self.__intermedios = (intermedios in ("S", "s"))
        self.resultados1 = 0
        self.resultados2 = 0

    def set_jugador1(self, fjugador1):
        if len(fjugador1) > 20:
            raise Exception("La longitud del nombre del jugador 1 no puede ser mayor de 20")
        else:
            self.__jugador1 = fjugador1

    def set_jugador2(self, fjugador2):
        if len(fjugador2) > 20:
            raise Exception("La longitud del nombre del jugador 2 no puede ser mayor de 20")
        else:
            self.__jugador2 = fjugador2

    def set_lanzamientos(self, flanzamientos):
        if not 2 < flanzamientos < 100:
            raise Exception("El número de lanzamientos debe de estar entre 2 y 100")
        else:
            self.__lanzamientos = flanzamientos

    def lanzamiento(self):
        # En estas variables acumulo los resultados de los dos jugadores
        self.resultados1 = 0
        self.resultados2 = 0

        # Bucle con el número de veces que hay que lanzar los dados
        for x in range(self.__lanzamientos):
            # Lanzamiento de los 3 dados para el jugador1
            salida1 = self.dado1.lanzar()
            salida2 = self.dado2.lanzar()
            salida3 = self.dado3.lanzar()
            self.resultados1 += (salida1 + salida2 + salida3)

            # Muestro los datos del lanzamiento del jugador 1
            # no es necesario guardarse los datos intermedios en ninguna
            # estructura de datos, simplemente los muestro
            # aunque evidentemente también es posible hacerlo
            if self.__intermedios:
                print(f"Lanzamiento {x + 1}:")
                print(
                    f"{self.__jugador1}: {salida1} {salida2} {salida3} ({(salida1 + salida2 + salida3)})")

            # Lanzamiento de los 3 dados para el jugador2
            salida1 = self.dado1.lanzar()
            salida2 = self.dado2.lanzar()
            salida3 = self.dado3.lanzar()
            self.resultados2 += (salida1 + salida2 + salida3)

            # Muestro los datos del lanzamiento del jugador 2
            # no es necesario guardarse los datos intermedios en ninguna
            # estructura de datos, simplemente los muestro
            if self.__intermedios:
                print(
                    f"{self.__jugador2}: {salida1} {salida2} {salida3} ({(salida1 + salida2 + salida3)})")
                print("")

    def mostrar(self):
        # Muestro los datos del resultado del juego
        print("Resultados:")
        print(f"Jugador 1: {self.__jugador1}")
        print(f"Jugador 2: {self.__jugador2}")
        print(f"Numero de lanzamientos: {self.__lanzamientos}")
        print(f"Dados: {self.dado1.get_caras()},{self.dado2.get_caras()} y {self.dado3.get_caras()} ")
        print(f"Puntos jugador 1: {self.resultados1}")
        print(f"Puntos jugador 2: {self.resultados2}")
        if self.resultados1 > self.resultados2:
            print(f"El GANADOR es {self.__jugador1} con {self.resultados1} puntos")
        elif self.resultados1 == self.resultados2:
            print("Ha habido un EMPATE")
        else:
            print(f"El GANADOR es {self.__jugador2} con {self.resultados2} puntos")
