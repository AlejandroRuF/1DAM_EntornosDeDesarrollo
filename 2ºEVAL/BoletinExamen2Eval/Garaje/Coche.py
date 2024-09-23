import datetime


class Coche:
    __matricula: str
    __modelo: str
    __anyo: int
    __marca: str
    __combustible: str
    __clasEcologica: str

    def get_matricula(self):
        return self.__matricula

    def get_modelo(self):
        return self.__modelo

    def get_anyo(self):
        return self.__anyo

    def get_marca(self):
        return self.__marca

    def get_combustible(self):
        return self.__combustible

    def get_combustibleStr(self):
        if self.__combustible == 'D':
            return "Diesel"
        elif self.__combustible == 'G':
            return "Gasolina"
        else:
            return "Eléctrico"

    def set_matricula(self, matricula: str):
        if isinstance(matricula, str) and len(matricula) == 7:
            letras = 0
            numeros = 0
            for i in range(len(matricula)):
                if matricula[i].isalpha() and 0 <= i <= 2 and matricula[i] not in 'AEIOUabcdefghijklmnñopqrstuvwyxz':
                    letras += 1
                if matricula[i].isdigit() and 3 <= i < 7:
                    numeros += 1
            if numeros == 4 and letras == 3:
                self.__matricula = matricula

            else:
                raise Exception("La matricula introducida es invalida ejemlo correcto --> ABC1234")

        else:
            raise Exception("La matricula debe ser una cadena de 7 caracteres")

    def set_modelo(self, modelo: str):
        if isinstance(modelo, str):
            self.__modelo = modelo
        else:
            raise Exception("El modelo del coche debe ser una cadena de caracteres")

    def set_marca(self, marca: str):
        if isinstance(marca, str):
            self.__marca = marca
        else:
            raise Exception("La marca debe ser una cadena de caracteres")

    def set_anyo(self, anyo: int):
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        if isinstance(anyo, int) and 1886 < anyo < date.year:
            self.__anyo = anyo
        else:
            raise Exception(f"El año debe ser un entero entre 1886 y {date.year}")

    def set_combustible(self, combustible: str):
        if isinstance(combustible, str) and combustible.upper() in "DGE":
            self.__combustible = combustible.upper()
        else:
            raise Exception("El combustible debe ser 'D' para Diesel, 'G' para Gasolina o 'E' para Eléctrico")

    def clasificaionEcologica(self):
        if self.__combustible == "E":
            self.__clasEcologica = "A"
        elif (self.__combustible == "G" and self.__anyo >= 2015) or (self.__combustible == "D" and self.__anyo >= 2017):
            self.__clasEcologica = "B"
        else:
            self.__clasEcologica = "C"

    def get_clasEcologica(self):
        return self.__clasEcologica

    def __str__(self):
        return (f"{self.get_matricula()} {self.get_marca()} {self.get_modelo()} ({self.get_anyo()})"
                f" {self.get_combustibleStr()} - {self.get_clasEcologica()}")

    def __init__(self, matricula: str, marca: str, modelo: str, anyo: int, combustible: str):
        self.set_matricula(matricula)
        self.set_marca(marca)
        self.set_modelo(modelo)
        self.set_anyo(anyo)
        self.set_combustible(combustible)
        self.clasificaionEcologica()


if __name__ == "__main__":
    c1 = Coche("BBC1234", "Skoda", "Octavia", 2015, "G")

    print(c1)
