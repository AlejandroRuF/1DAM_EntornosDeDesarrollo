class Dado:
    __caras = 6

    def __init__(self, fcaras):
        # En el constructor solo necesito asignar el número de caras (obligatorio)
        # Utilizo el setter así sólo hago la validación una vez
        self.set_caras(fcaras)

    def lanzar(self):
        # Devuelvo un número aleatorio entre 1 y el número de caras del objeto
        import random
        return random.randint(1, self.__caras)

    def get_caras(self):
        return self.__caras

    def set_caras(self, fcaras):
        # Realizo la validación del número de caras válido
        # si no se cumple lanzo una excepción
        caras_permitidas = [4, 6, 8, 10, 12, 20, 120]
        if fcaras in caras_permitidas:
            self.__caras = fcaras
        else:
            raise Exception("Numero de caras incorrecto")
