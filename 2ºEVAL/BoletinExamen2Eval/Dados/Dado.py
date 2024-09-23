import random


class Dado:
    __caras:int

    def set_caras(self,caras):
        if isinstance(caras,int) and caras in [4,6,8,10,12,20,120]:
            self.__caras = caras
        else:
            raise Exception("El numero de caras solo puede ser uno de los siguientes 4,6,8,10,12,20,120")

    def get_caras(self):
        return self.__caras

    def lanzar(self):
        return random.randint(1,self.get_caras())

    def __init__(self, caras):
        self.set_caras(caras)

    
