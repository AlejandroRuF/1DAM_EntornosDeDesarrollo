class Dado:
    """
    Esta clase representa un objeto de datos que devolvera un número entero entre 1 y el número de caras seleccionadas.
    """
    __caras = 6

    def __init__(self, fcaras):
        """

        :param fcaras: int en esta funcion se establece el número de caras que tiene un dado.
        """
        self.set_caras(fcaras)

    def lanzar(self):
        """
        Se genera y
        :return: se devuelve un entero aleatorio entre 1 y __caras
        """
        import random
        return random.randint(1, self.__caras)

    def get_caras(self):
        """
        En esta funcion se devuelve
        :return: el número de caras elegido.
        """
        return self.__caras

    def set_caras(self, fcaras):
        """
        En esta funcion se devuelve
        :param fcaras: número de caras que tiene un dado determinado en este caso por el
        programa. Este número de caras está limitado a los valores 4,6,8,10,12,20,120 que determina
        :param caras_permitidas: int está limitado a los valores 4,6,8,10,12,20,120
        :return: Devuelve el número de caras elegido o se genera un error en caso de no elegir
        dentro de las limitaciones.
        """
        caras_permitidas = [4, 6, 8, 10, 12, 20, 120]
        if fcaras in caras_permitidas:
            self.__caras = fcaras
        else:
            raise Exception("Numero de caras incorrecto")
