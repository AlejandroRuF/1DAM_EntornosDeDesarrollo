import re


class Persona:
    __edad = None
    __nom = None
    __DNI = None

    def __init__(self, nom, edadd, dNI):
        self.set_nom(nom)
        self.set_edad(edadd)
        self.set_DNI(dNI)

    def get_nombre(self):
        return self.__nom

    def get_edad(self):
        return self.__edad

    def get_DNI(self):
        return self.__DNI

    def __str__(self):

        return f"Nombre: {self.get_nombre()} edad: {self.get_edad()} DNI: {self.get_DNI()}"

    def set_edad(self, edads):
        patron = r"^[0-9]{1,2}"
        if re.match(patron, str(edads)):
            if edads < 0:
                raise Exception("Introduce solo numeros del 0 al 99")
            else:
                self.__edad = edads
        else:
            raise Exception("Introduce solo numeros del 0 al 99")

    def set_nom(self, nom):
        patron = r"^[A-Za-z\s]+$"
        if re.match(patron, nom):
            self.__nom = str(nom)
        else:
            raise Exception("El nombre solo puede contener caracteres alfabeticos o espacios")

    def set_DNI(self, dNI):
        patron = r"^[0-9]{8}[A-Za-z]$"
        if re.match(patron, dNI) and (dNI[-1].upper() == self.letra_dni(int(dNI[:-1]))):
            self.__DNI = dNI
        else:
            raise Exception("El DNI no es valido")

    @staticmethod
    def letra_dni(numero_dni):
        tabla_letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = tabla_letras[numero_dni % 23]
        return letra

    def EsMajorEdat(self):
        if self.__edad >= 18:
            return True
        else:
            return False

    def Mostrar_Dades(self):
        print(f"Nombre: {self.get_nombre()} edad: {self.get_edad()} DNI: {self.get_DNI()}")

