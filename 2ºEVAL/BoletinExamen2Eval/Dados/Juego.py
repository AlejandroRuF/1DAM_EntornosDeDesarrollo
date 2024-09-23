from Dado import Dado


class Juego:
    __nombre_Jugador1: str
    __nombre_Jugador2: str
    __total_Lanzamientos: int
    __dado1: Dado
    __dado2: Dado
    __dado3: Dado
    __resultadosJ1D1 = []
    __resultadosJ1D2 = []
    __resultadosJ1D3 = []
    __resultadosJ2D1 = []
    __resultadosJ2D2 = []
    __resultadosJ2D3 = []

    def __init__(self, nombre_Jugador1: str, nombre_Jugador2: str, total_Lanzamientos:int):
        self.set_nombre_Jugador1(nombre_Jugador1)
        self.set_nombre_Jugador2(nombre_Jugador2)
        self.set_total_Lanzamientos(total_Lanzamientos)
        self.__resultadosJ1D1 = []
        self.__resultadosJ2D1 = []
        self.__resultadosJ1D2 = []
        self.__resultadosJ2D2 = []
        self.__resultadosJ1D3 = []
        self.__resultadosJ2D3 = []

    def set_nombre_Jugador1(self, nombre1):
        if isinstance(nombre1, str) and len(nombre1) <= 20:
            self.__nombre_Jugador1 = nombre1
        else:
            raise Exception("El nombre del jugador no puede ser superior a 20 caracteres")

    def set_nombre_Jugador2(self, nombre2):
        if isinstance(nombre2, str) and len(nombre2) <= 20:
            self.__nombre_Jugador2 = nombre2
        else:
            raise Exception("El nombre del jugador no puede ser superior a 20 caracteres")

    def get_nombre_Jugador1(self):
        return self.__nombre_Jugador1

    def get_nombre_Jugador2(self):
        return self.__nombre_Jugador2

    def set_total_Lanzamientos(self, total_Lanzamientos):
        if isinstance(total_Lanzamientos, int) and 2 <= total_Lanzamientos <= 100:
            self.__total_Lanzamientos = total_Lanzamientos
        else:
            raise Exception("El total de lanzamientos debe ser un numero entero entre 2 y 100")

    def get_total_Lanzamientos(self):
        return self.__total_Lanzamientos

    def generar_dados(self, dado1, dado2, dado3):
        self.__dado1 = Dado(dado1)
        self.__dado2 = Dado(dado2)
        self.__dado3 = Dado(dado3)

    def generar_lanzamientos(self):
        for i in range(0, self.__total_Lanzamientos):
            self.__resultadosJ1D1.append(self.__dado1.lanzar())
            self.__resultadosJ2D1.append(self.__dado1.lanzar())
            self.__resultadosJ1D2.append(self.__dado2.lanzar())
            self.__resultadosJ2D2.append(self.__dado2.lanzar())
            self.__resultadosJ1D3.append(self.__dado3.lanzar())
            self.__resultadosJ2D3.append(self.__dado3.lanzar())

    def mostrar_resultadosIndividuales(self):
        for i in range(len(self.__resultadosJ1D1)):
            print(f"\nLanzamiento {i + 1}:\n"
                  f"{self.get_nombre_Jugador1()}: {self.__resultadosJ1D1[i]} {self.__resultadosJ1D2[i]} {self.__resultadosJ1D3[i]} ({self.__resultadosJ1D1[i] + self.__resultadosJ1D2[i] + self.__resultadosJ1D3[i]})\n"
                  f"{self.get_nombre_Jugador2()}: {self.__resultadosJ2D1[i]} {self.__resultadosJ2D2[i]} {self.__resultadosJ2D3[i]} ({self.__resultadosJ2D1[i] + self.__resultadosJ2D2[i] + self.__resultadosJ2D3[i]})\n")

    def mostrar_resultadosTotales(self):
        resultadoJ1 = 0
        resultadoJ2 = 0
        for i in range(len(self.__resultadosJ1D1)):
            resultadoJ1 += (self.__resultadosJ1D1[i] + self.__resultadosJ1D2[i] + self.__resultadosJ1D3[i])
            resultadoJ2 += (self.__resultadosJ2D1[i] + self.__resultadosJ2D2[i] + self.__resultadosJ2D3[i])

        print(f"Resultados en {self.get_total_Lanzamientos()} tiradas:\n"
              f"{self.get_nombre_Jugador1()} ---> {resultadoJ1} Puntos\n"
              f"{self.get_nombre_Jugador2()} ---> {resultadoJ2} Puntos\n\n"
              f"Ganador ---> ",end="")
        if resultadoJ1 > resultadoJ2:
            print(self.get_nombre_Jugador1())
        elif resultadoJ2 > resultadoJ1:
            print(self.get_nombre_Jugador2())
        else:
            print("Ninguno es empate")
