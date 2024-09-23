from nau import NauEspacial


class Flota:
    __nombre: str
    __naves: list = []

    def getNombre(self):
        return self.__nombre

    def getNaves(self):
        return self.__naves

    def setNombre(self, nom):
        if isinstance(nom, str) and 10 <= len(nom) <= 80:
            self.__nombre = nom
        else:
            raise Exception("El nombre de la flota debe ser una cadena entre 10 y 80 caracteres")

    def agregarNave(self, nave: NauEspacial):
        if isinstance(nave, NauEspacial):
            if len(self.__naves) < 100:
                self.__naves.append(nave)
            else:
                raise Exception(
                    "Se ha alcanzado la capacidad máxima de 100 naves en esta flota no se pueden añadir más")
        else:
            raise Exception("Solo las naves espaciales pueden ser agregadas a la flota")

    def mostrarFlota(self):
        contador = 1
        for nave in self.__naves:
            nave: NauEspacial
            print(f"Nave nº {contador}:\n")
            nave.mostrarInformacion()
            contador += 1

    def cuentasnav(self):
        b = 0
        r = 0
        t = 0
        o = 0
        for nave in self.__naves:
            nave: NauEspacial
            if nave.getTipoSTR().upper() == "B":
                b += 1
            elif nave.getTipoSTR().upper() == "R":
                r += 1
            elif nave.getTipoSTR().upper() == "T":
                t += 1
            else:
                o += 1

        if b == 1:
            print(f"Batalla: {b} nave")
        else:
            print(f"Batalla: {b} naves")
        if r == 1:
            print(f"Reconocimiento: {r} nave")
        else:
            print(f"Reconocimiento: {r} naves")
        if t == 1:
            print(f"Transporte: {t} nave")
        else:
            print(f"Transporte: {t} naves")
        if o == 1:
            print(f"Bombardero: {o} nave")
        else:
            print(f"Bombardero: {o} naves")

    def completa(self):
        b = 0
        r = 0
        t = 0
        o = 0
        for nave in self.__naves:
            nave: NauEspacial
            if nave.getTipoSTR().upper() == "B":
                b += 1
            elif nave.getTipoSTR().upper() == "R":
                r += 1
            elif nave.getTipoSTR().upper() == "T":
                t += 1
            else:
                o += 1

        if b > 0 and r > 0 and t > 0 and o > 0:
            return True
        else:
            return False

    def mostrarEnergia(self):
        concNaves = ""
        energia = 0
        for naves in self.__naves:
            naves: NauEspacial
            concNaves += naves.mosEnergia() + "\n"
            energia += naves.getnumEnergia()

        print(concNaves + f"Total {energia} MegaJulios")

    def __init__(self, nom):
        self.__nombre = ""
        self.setNombre(nom)


if __name__ == "__main__":
    nav = NauEspacial("Enterprise", "B", 500)
    nav1 = NauEspacial("naaa", "R", 999)
    nav2 = NauEspacial("Nbbb", "T", 400)
    nav3 = NauEspacial("NCCCC", "O", 250)
    nav.modificarNivelEnergia(80)

    f1 = Flota("Flotilladecaracteres10")

    f1.agregarNave(nav)
    print(f1.completa())
    print()
    print()

    f1.agregarNave(nav3)
    print(f1.completa())
    print()
    print()
    f1.mostrarFlota()
    f1.mostrarEnergia()
    f1.agregarNave(nav2)
    f1.agregarNave(nav1)
    f1.mostrarFlota()
    print(f1.completa())
    print()
    print()
    f1.mostrarEnergia()
