import time


class NauEspacial:
    __nombre: str
    __tipo: str
    __capacidadEnergia: int  # Entre 0 y 1000 MegaJulios capacidad total del deposito
    __nivelEnergia: int = 0  # Porcentaje entre 0 y 100

    def getNombre(self):
        return self.__nombre

    def getCapacidadEnergia(self):
        return self.__capacidadEnergia

    def getNivelEnergia(self):
        return self.__nivelEnergia

    def getTipo(self):
        if self.__tipo.upper() == "B":
            return "Batalla"
        elif self.__tipo.upper() == "R":
            return "Reconocimiento"
        elif self.__tipo.upper() == "T":
            return "Transporte"
        else:
            return "Bombardero"

    def getTipoSTR(self):
        return self.__tipo

    def setNombre(self, nom):
        if isinstance(nom, str) and len(nom) >= 1:
            self.__nombre = nom
        else:
            raise Exception("El nombre de la nave debe ser una cadena de caracteres de minimo 1 de longitud")

    def setCapacidadEnergia(self, num):
        if isinstance(num, int) and 0 < num < 1000:
            self.__capacidadEnergia = num
        else:
            raise Exception("La capacidad de energía debe ser un número entero superior a 0 e inferior a 1000")

    def modificarNivelEnergia(self, num):
        if (self.getNivelEnergia() + num) <= 100:
            self.__nivelEnergia += num
        else:
            raise Exception(
                f"El combustible esta al {self.getNivelEnergia()} elige un número entre el 1 y el "
                f"{100 - self.__nivelEnergia} para rellenar un porcentaje del deposito")

    def setTipo(self, tipo):
        if isinstance(tipo, str) and tipo.upper() in ["B", "R", "T", "O"]:
            self.__tipo = tipo
        else:
            raise Exception(
                "El tipo debe ser una de las siguientes opciones 'B'(Batalla), 'R'(Reconocimiento), "
                "'T'(Transporte), 'O'(Bombardero)")

    def getnumEnergia(self):
        return int((self.__nivelEnergia * self.__capacidadEnergia) / 100)

    def mostrarInformacion(self):
        rangoEnergia = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        contador = 0
        print(f"Nombre: {self.getNombre()}\n"
              f"Nave de {self.getTipo()}\n"
              f"Capacidad del deposito {self.getCapacidadEnergia()} MegaJulios\n"
              f"Energia: ")
        for lleno in range(self.__nivelEnergia):
            if lleno % 6 != 0:
                print("X", end="")
                time.sleep(5 / 60)

        contador2 = 0
        print(f"  ({self.__nivelEnergia}%)")
        for i in range(71):
            if i == 0 or contador2 == 7:
                print(rangoEnergia[contador], end="")
                if contador < len(rangoEnergia) - 1:
                    contador += 1
                    contador2 = 0

            else:
                print("-", end="")
            contador2 += 1
            # (30 x 360) / 100
        print(f"\nEnergia Disponible: {self.getnumEnergia()} MegaJulios")

    def __init__(self, nom, tipo, capacidad):
        self.__nombre = ""
        self.setNombre(nom)
        self.__tipo = ""
        self.setTipo(tipo)
        self.__capacidadEnergia = 0
        self.setCapacidadEnergia(capacidad)
        self.__nivelEnergia = 0
        self.modificarNivelEnergia(10)

    def mosEnergia(self):
        return f"Nave : {self.getNombre()} ({self.getnumEnergia()})"


if __name__ == "__main__":
    nav = NauEspacial("Enterprise", "B", 500)
    nav.mostrarInformacion()
    nav.modificarNivelEnergia(25)
    nav.mostrarInformacion()
