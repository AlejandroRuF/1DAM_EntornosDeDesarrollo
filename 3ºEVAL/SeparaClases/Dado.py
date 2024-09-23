import random


class Dado:
    __caras: int = None

    def __init__(self, caras):
        self.set_Caras(caras)

    def set_Caras(self, caras):
        if isinstance(caras, int):
            self.__caras = caras
        else:
            raise Exception("El valor caras debe ser un numero entero")

    def get_caras(self):
        return self.__caras

    def lanzar(self):
        if self.__caras is not None:
            return random.randint(1, self.get_caras())
        else:
            raise Exception("Se debe ficar el numero de caras primero")

    def __str__(self):
        return f"El dado tiene {self.get_caras()} caras"

