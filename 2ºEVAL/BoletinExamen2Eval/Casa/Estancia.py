class Estancia:
    __tipo_Estancia: str
    __met2: int
    __vent_Exterior: bool

    def gettipo_EstanciaStr(self):
        if self.__tipo_Estancia.upper() == "M":
            return "Comedor"
        elif self.__tipo_Estancia.upper() == "H":
            return "Habitacion"
        elif self.__tipo_Estancia.upper() == "C":
            return "Cocina"
        else:
            return "Baño"

    def gettipo_Estancia(self):
        return self.__tipo_Estancia

    def settipo_Estancia(self, tipo):
        if isinstance(tipo, str) and tipo.upper() in "MHCB":
            self.__tipo_Estancia = tipo.upper()
        else:
            raise Exception("El tipo de estantia solo puede ser 'M', 'H', 'C', 'B' («M» hace referència a «comedor»,"
                            " «H» hace referència a «Habitacion», «C» hace referència a «Cocina»"
                            " y «B» hace referència a «Baño»)")

    def getmet2(self):
        return self.__met2

    def setmet2(self, metros):
        if isinstance(metros, int) and 0 <= metros <= 50:
            if self.gettipo_Estancia().upper() == "M" and metros < 15:
                raise Exception("Un comedor debe tener al menos 15 metros cuadrados")

            elif self.gettipo_Estancia().upper() == "B" and metros < 5:
                raise Exception("Un baño debe tener al menos 5 metros cuadrados")

            elif self.gettipo_Estancia().upper() == "C" and metros < 5:
                raise Exception("Una cocina debe tener al menos 5 metros cuadrados")

            elif self.gettipo_Estancia().upper() == "H" and metros < 10:
                raise Exception("Una habitación debe tener al menos 10 metros cuadrados")

            else:
                self.__met2 = metros
        else:
            raise Exception("Los metros cuadrados debe ser un numero entero entre 5 y 50")

    def getVentExterior(self):
        return self.__vent_Exterior

    def setVentExteriores(self, tiene):
        if isinstance(tiene, bool):
            self.__vent_Exterior = tiene
        else:
            raise Exception("Este valor solo puede ser S/N")

    def __str__(self):
        return (f"Estancia tipo ---> {self.gettipo_EstanciaStr()}\n"
                f"Metros cuadrados ---> {self.getmet2()}\n"
                f"Ventanas Exteriores ---> {self.__vent_Exterior}\n")

    def mostrar(self):
        print(self.__str__())

    def __init__(self, tipo, metros, ventanas):
        self.settipo_Estancia(tipo)
        self.setmet2(metros)
        self.setVentExteriores(ventanas)


if __name__ == "__main__":
    e1 = Estancia("H", 5, True)
    e1.mostrar()
