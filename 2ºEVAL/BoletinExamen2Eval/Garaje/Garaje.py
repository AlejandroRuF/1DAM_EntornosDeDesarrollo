from Coche import Coche


class Garaje:
    __descripcion: str
    __capacidad: int
    __electricos: int
    __coches: list = []
    __combustible = [0, 0, 0]
    __clas = [0, 0, 0]

    def getDescripcion(self):
        return self.__descripcion

    def getCapacidad(self):
        return self.__capacidad

    def getElectricos(self):
        return self.__electricos

    def getCoches(self):
        return self.__coches

    def setDescripcion(self, descripcion):
        if isinstance(descripcion, str) and len(descripcion) <= 40:
            self.__descripcion = descripcion
        else:
            raise Exception("La descripción debe ser una cadena de caracteres de hasta 40 de longitud")

    def setCapacidad(self, capacidad):
        if isinstance(capacidad, int) and capacidad > 5:
            self.__capacidad = capacidad
        else:
            raise Exception("La capacidad debe ser un numero entero mayor que 5")

    def setElectricos(self, electricos):
        if isinstance(electricos, int) and electricos <= self.getCapacidad():
            self.__electricos = electricos
        else:
            raise Exception(f"Las plazas de carga de electricos no puede ser mayor a {self.getCapacidad()}")

    def setCoches(self, coches):
        if len(self.getCoches()) < self.getCapacidad():
            if isinstance(coches, list):
                if len(coches) > 0:
                    for c in coches:
                        c: Coche
                        self.estad2()
                        if (self.getElectricos() > self.__combustible[2]
                            and c.get_combustible() == "E") or c.get_combustible() in "GD":
                            matrepetida = False
                            if isinstance(c, Coche):
                                if len(self.getCoches()) > 0:
                                    for m in self.getCoches():
                                        m: Coche
                                        if m.get_matricula() == c.get_matricula():
                                            matrepetida = True
                                    if not matrepetida:
                                        self.__coches.append(c)
                                        self.estad2()
                                    else:
                                        raise Exception(f"Ya existe un coche con la matricula {c.get_matricula()}")
                                else:
                                    self.__coches.append(c)
                                    self.estad2()
                            else:
                                raise Exception("Todos los eelementos de la lista deben ser coches")
                        else:
                            raise Exception("Ya no caben más coches eléctricos")
                else:
                    raise Exception("La longitud de la lista debe ser mayor a 0")

            elif isinstance(coches, Coche):
                self.estad2()
                if (self.getElectricos() > self.__combustible[
                    2] and coches.get_combustible() == "E") or coches.get_combustible() in "GD":
                    matrepetida = False
                    if len(self.getCoches()) > 0:
                        for m in self.getCoches():
                            m: Coche
                            if m.get_matricula() == coches.get_matricula():
                                matrepetida = True
                        if not matrepetida:
                            self.__coches.append(coches)
                            self.estad2()
                        else:
                            raise Exception(f"Ya existe un coche con la matricula {coches.get_matricula()}")
                    else:
                        self.__coches.append(coches)
                        self.estad2()
                else:
                    raise Exception("Ya no caben más coches eléctricos")
            else:
                raise Exception("El elemento debe ser un coche")
        else:
            raise Exception("Este garaje ya esta lleno")

    def agregarCoches(self, coches: Coche):
        if isinstance(coches, Coche):
            self.setCoches(coches)

    def sacarCocheNum(self, num):
        if isinstance(num, int) and len(self.getCoches()) > num:
            self.getCoches().pop(num)
        else:
            raise Exception(f"Debes introducir un numero menor o igual a {len(self.getCoches())}")

    def resumen(self):
        listacoches: str = ""
        contador = 1
        for coches in self.getCoches():
            coches: Coche
            listacoches += f"     {contador}: {coches.__str__()}\n"
            contador += 1
        print(
            f"Garaje: {self.getDescripcion()}\n Capacidad: {self.getCapacidad()}\nCargadores para Eléctricos:"
            f" {self.getElectricos()}\nCoches en el garaje:\n{listacoches}")

    def sacarCocheMatricula(self, matricula: str):
        matok = False
        for coches in self.getCoches():
            coches: Coche
            if coches.get_matricula() == matricula:
                matok = True
                self.getCoches().remove(coches)

        if not matok:
            raise Exception(f"En nuestro garaje no existe ningun coche con la matricula {matricula}")

    def estad2(self):
        combustible = [0, 0, 0]
        clas = [0, 0, 0]

        for coches in self.getCoches():
            coches: Coche
            if coches.get_combustible() == "D":
                combustible[0] += 1
            elif coches.get_combustible() == "G":
                combustible[1] += 1
            elif coches.get_combustible() == "E":
                combustible[2] += 1
            if coches.get_clasEcologica() == "A":
                clas[0] += 1
            elif coches.get_clasEcologica() == "B":
                clas[1] += 1
            elif coches.get_clasEcologica() == "C":
                clas[2] += 1
        self.__combustible = combustible
        self.__clas = clas

    def estadistica(self):
        self.estad2()

        print(f"Garaje: {self.getDescripcion()}\n"
              f"Capacidad: {self.getCapacidad()}\n"
              f"Cargadores para Eléctricos: {self.getElectricos()}\n"
              f"Coches en el garaje:\n"
              f"  Por combustible:\n"
              f"        Diesel: {self.__combustible[0]}\n"
              f"        Gasolina: {self.__combustible[1]}\n"
              f"        Eléctrico: {self.__combustible[2]}\n"
              f"  Por Clasificacion Ecologica:\n"
              f"        A: {self.__clas[0]}\n"
              f"        B: {self.__clas[1]}\n"
              f"        C: {self.__clas[2]}\n")

    def __init__(self, descripcion, capacidad, electricos):
        self.setDescripcion(descripcion)
        self.setCapacidad(capacidad)
        self.setElectricos(electricos)


if __name__ == "__main__":
    c1 = [Coche("BBB1234", "Skoda", "Octavia", 2010, "E"), Coche("BBC1234", "Skoda", "Octavia", 2015, "G"),
          Coche("BBD1234", "Skoda", "Octavia", 2000, "D"), Coche("BBC1235", "Skoda", "Octavia", 2015, "G"),
          Coche("BBC1245", "Skoda", "Octavia", 2015, "G")]
    c2 = Coche("BBF1234", "Skoda", "Octavia", 2015, "G")
    c3 = Coche("BBG1234", "Skoda", "Octavia", 2015, "D")
    g1 = Garaje("Garaje Godelleta", 7, 1)
    print(c3.get_combustible())
    g1.setCoches(c1)
    g1.resumen()
    g1.agregarCoches(c2)
    g1.agregarCoches(c3)
    g1.resumen()
    g1.estadistica()
    g1.sacarCocheMatricula("BBB1234")
    g1.resumen()
    g1.sacarCocheNum(0)
    g1.resumen()
