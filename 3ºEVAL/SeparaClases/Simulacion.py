from Dado import Dado


class Simulacion:
    __dado: Dado = None
    __num_lanzamientos: int = None
    __resultado: int = []

    def __str__(self):
        return f"El dado tiene {self.get_dados().get_caras()} caras y se lanzara {self.get_numLanzamientos()}"
    def set_Dados(self, dados: Dado):
        tipocorrecto = False
        if isinstance(dados, Dado):
            tipocorrecto = True
        else:
            print("Todos los objetos tipo dado deben ser creados correctamente")

        if tipocorrecto:
            self.__dado = dados
        else:
            raise Exception("Todos los objetos de la lista deben ser tipo Dado")

    def get_dados(self):
        return self.__dado

    def set_numLanzamientos(self, num_lanza):
        if isinstance(num_lanza, int) and num_lanza > 0:
            self.__num_lanzamientos = num_lanza
        else:
            raise Exception("El numero de lanzamientos debe ser un numero entero positivo")

    def get_numLanzamientos(self):
        return self.__num_lanzamientos

    def __init__(self, dados, num_lanz):
        self.set_Dados(dados)
        self.set_numLanzamientos(num_lanz)

    def generar(self):

        for j in range(self.get_numLanzamientos()):
            resultado = int(self.__dado.lanzar())
            self.__resultado.append(resultado)

    def get_resultado(self):
        return self.__resultado

    def mostrar_resultados(self):
        print(f"Estos son los resultados de tus lanzamientos:\n")
        contador = 0

        for i in range(self.get_dados().get_caras()):
            for j in (self.get_resultado()):
                if j == (i + 1):
                    contador += 1
            print(f"{(i + 1)} ---> {contador} ({round(((contador/self.get_numLanzamientos())*100),3)}%)")
            contador = 0

