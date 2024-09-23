import time


class Pokemon:
    __nombre: str
    __tipo: str
    __nivel: int
    __nivel_evolucion2: int
    __nombre_evolucion2: str
    __nivel_evolucion3: int
    __nombre_evolucion3: str
    __nombre_entrenador: str
    __evoluciones = 0

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise Exception("El nombre del pokemon debe ser una cadenba de caracteres")

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        if isinstance(tipo, str):
            if tipo.upper() in ["FUEGO", "AGUA", "PLANTA", "ELECTRICO", "DRAGON"]:
                self.__tipo = tipo
            else:
                raise Exception("El tipo del pokemon solo puede ser Fuego, Agua, Planta, Eléctrico o Dragon (No hacen "
                                "falta las tildes)")
        else:
            raise Exception("El tipo del pokemon debe ser una cadena de caracteres o String")

    def get_nivel(self):
        return self.__nivel

    def set_nivel(self, nivel):
        if isinstance(nivel, int) and 0 < nivel <= 100:
            self.__nivel = nivel
        else:
            raise Exception("El nivel debe ser un numero entero entre el 1 y el 100")

    def set_nivelEvolucion2(self, nivelEvolucion2):
        if isinstance(nivelEvolucion2, int) and self.get_nivel() < nivelEvolucion2 <= 100:
            self.__nivel_evolucion2 = nivelEvolucion2
        else:
            raise Exception(
                f"El nivel de la evolucion 2 debe ser un numero entero entre el {self.get_nivel() + 1} y el 100")

    def get_nivelEvolucion2(self):
        return self.__nivel_evolucion2

    def set_nivelEvolucion3(self, nivelEvolucion3):
        if isinstance(nivelEvolucion3, int) and self.get_nivelEvolucion2() < nivelEvolucion3 <= 100:
            self.__nivel_evolucion3 = nivelEvolucion3
        else:
            raise Exception(
                f"El nivel de la evolucion 3 debe ser un numero entero entre el {self.get_nivelEvolucion2() + 1} y el "
                f"100")

    def get_nivelEvolucion3(self):
        return self.__nivel_evolucion3

    def get_nombreEvolucion2(self):
        return self.__nombre_evolucion2

    def get_nombreEvolucion3(self):
        return self.__nombre_evolucion3

    def set_nombreEvolucion2(self, nombreEvolucion2):
        if isinstance(nombreEvolucion2, str):
            self.__nombre_evolucion2 = nombreEvolucion2
        else:
            raise Exception("El nombre del pokemon debe ser una cadenba de caracteres")

    def set_nombreEvolucion3(self, nombreEvolucion3):
        if isinstance(nombreEvolucion3, str):
            self.__nombre_evolucion3 = nombreEvolucion3
        else:
            raise Exception("El nombre del pokemon debe ser una cadenba de caracteres")

    def set_nombreEntrenador(self, nombreEntrenador):
        if isinstance(nombreEntrenador, str):
            self.__nombre_entrenador = nombreEntrenador
        else:
            raise Exception("El nombre del Entrenador debe ser una cadenba de caracteres")

    def subirNivel(self, niveles):
        if 0 < niveles <= (100):
            if (niveles + self.get_nivel()) >= self.get_nivelEvolucion3() and self.__evoluciones > 0:
                self.set_nivel(niveles + self.get_nivel())
                print("Tu Pokemon esta evolucionando")
                for i in range(40):
                    print(".", end="")
                    time.sleep(8 / 60)
                print(f"\nFelicidades tu {self.get_nombre()} se ha convertido en {self.get_nombreEvolucion3()}")
                self.set_nombre(self.__nombre_evolucion3)

            elif (niveles + self.get_nivel()) >= self.get_nivelEvolucion2():
                self.set_nivel(niveles + self.get_nivel())
                print("Tu Pokemon esta evolucionando")
                for i in range(40):
                    print(".", end="")
                    time.sleep(8 / 60)
                print(f"\nFelicidades tu {self.get_nombre()} se ha convertido en {self.get_nombreEvolucion2()}")

                self.set_nombre(self.__nombre_evolucion2)
                self.__evoluciones = +1
            else:
                self.set_nivel(niveles + self.get_nivel())
        else:
            raise Exception("Los niveles que sube tu pokemon debe ser un numero entre el 1 y el 99")

    def __init__(self, nombre, tipo, nivel, nivel_Evolucion2, nombre_Evolucion2, nivel_Evolucion3, nombre_Evolucion3,
                 entrenador):
        self.set_nombre(nombre)
        self.set_tipo(tipo)
        self.set_nivel(nivel)
        self.set_nivelEvolucion2(nivel_Evolucion2)
        self.set_nombreEvolucion2(nombre_Evolucion2)
        self.set_nivelEvolucion3(nivel_Evolucion3)
        self.set_nombreEvolucion3(nombre_Evolucion3)
        self.set_nombreEntrenador(entrenador)

    def __str__(self):
        return (f"Nombre: {self.get_nombre()}\n"
                f"Tipo: {self.get_tipo()}\n"
                f"Nivel: {self.get_nivel()}")
