from Estancia import Estancia


class Vivienda:
    __estancias: list = []
    __nombre: str
    __maxiNumEstancias: int

    def getMaxNumEstancias(self):
        return self.__maxiNumEstancias

    def setMaxNumEstancias(self, num):
        if isinstance(num, int) and  num >= 4:
            self.__maxiNumEstancias = num
        else:
            raise Exception ("El numero minimo de estancias para legalizar una casa es de 4")

    def getEstancias(self):
        return self.__estancias

    def setEstancias(self, estancias):
        if isinstance(estancias, list):
            if len(self.__estancias) + len(estancias) <= self.getMaxNumEstancias():
                for estancia in estancias:
                    if isinstance(estancias, Estancia):
                        self.getEstancias().append(estancia)
                    else:
                        raise Exception("El contenido de la lista debe ser de tipo enstancia")
            else:
                raise Exception(f"La capacidad de estancias maxima de estancias de esta vivien da es de "
                                f"{self.getMaxNumEstancias()} y no puedes superarla")

        elif isinstance(estancias, Estancia):
            if self.getMaxNumEstancias() > len(self.getEstancias()):
                self.getEstancias().append(estancias)
            else:
                raise Exception(f"La capacidad de estancias maxima de estancias de esta vivien da es de "
                                f"{self.getMaxNumEstancias()} y no puedes superarla")
        else:
            raise Exception("Solo se pueden añadir objetos de tipo estancia")

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nom):
        if isinstance(nom, str):
            self.__nombre = nom
        else:
            raise "El nombre debe ser una cadena de caracteres"

    def anyadirenstancia(self, estancia: Estancia):
        if isinstance(estancia, Estancia):
            self.setEstancias(estancia)
        else:
            raise Exception("Solo puedes añadir obejos de tipo estancia")

    def mostrar(self):
        contador = 0
        for estancia in self.getEstancias():
            print(f"{contador + 1}:\n{estancia}")
            contador += 1

    def quitarestancia(self, num):
        self.__estancias.pop(num)

    def legalidad(self):
        cocina = 0
        comedor = 0
        banyo = 0
        hab = 0
        meTotales = 0
        ventanas = 0
        for estancias in self.getEstancias():
            estancias: Estancia

            if estancias.gettipo_Estancia() == "C":
                cocina += 1
            elif estancias.gettipo_Estancia() == "H":
                hab += 1
            elif estancias.gettipo_Estancia() == "B":
                banyo += 1
            elif estancias.gettipo_Estancia() == "M":
                comedor += 1
            meTotales += estancias.getmet2()
            if estancias.getVentExterior():
                ventanas += 1

        print(f"Resumen vivienda:\n"
              f"Habitaciones: {hab}\n"
              f"Comedores: {comedor}\n"
              f"Cocinas: {cocina}\n"
              f"Baños: {banyo}\n"
              f"Metros Cuadrados: {meTotales}\n"
              f"Ventanas Exteriores: {ventanas}")

        if comedor == 0 or cocina == 0 or banyo == 0 or hab == 0 or ventanas == 0 or meTotales < 50:
            print("Casa ilegal debido a :")
            if comedor == 0:
                print(f"     Esta casa no tiene ningun comedor")
            if cocina == 0:
                print(f"     Esta casa no tiene ninguna cocina")
            if banyo == 0:
                print(f"     Esta casa no tiene ningun baño")
            if hab == 0:
                print(f"     Esta casa no tiene ninguna habitacion")
            if ventanas == 0:
                print(f"     Esta casa no tiene ninguna ventana exterior")
            if meTotales < 50:
                print(f"     Esta casa no supera los metros cuadrados habitables mínimos necesarios de 50m2")
        else:
            print("Esta Casa es legal")

    def mostrarEstancias(self):
        for estancias in self.getEstancias():
            estancias: Estancia
            estancias.mostrar()

    def __init__(self, nombre, maxi):
        self.setNombre(nombre)
        self.setMaxNumEstancias(maxi)
