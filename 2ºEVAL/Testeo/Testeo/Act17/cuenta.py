class Persona:

    def __init__(self, nombre, edad, dni):
        if not nombre.isalpha():
            raise Exception("El nombre solo puede admitir carácteres alfabéticos")
        self.nom = nombre
        if type(edad) != int:
            raise Exception("No es una edad válida")
        if edad < 0:
            raise Exception("No es una edad válida")
        self.edat = edad
        self.dni = dni
        self.comprobar_dni()

    def __str__(self):
        return f"Nombre: {self.nom}. Edad: {self.edat}. DNI: {self.dni}"

    def es_major_edat(self):
        if self.edat >= 18:
            print(f"{self.nom} es mayor de edad.")
        elif 18 > self.edat >= 0:
            print(f"{self.nom} no es mayor de edad.")

    def lletra_dni(self):
        contador = 0
        n_numero = int(self.dni[:8])
        for x in "TRWAGMYFPDXBNJZSQVHLCKE":
            if contador == (n_numero % 23):
                return x
            contador += 1

    def comprobar_dni(self):
        if len(self.dni) == 9:
            if len(self.dni) == 9 and self.dni[:8].isdecimal() and self.lletra_dni() == self.dni[8]:
                print(f"El DNI {self.dni} es válido")
            else:
                print(f"El DNI {self.dni} no es válido")
                print(f"La letra sería {self.lletra_dni()}")
                raise Exception("Formato del DNI incorrecto")
        else:
            raise Exception("La longitud del DNI es incorrecta")


class Compte:
    __historic = []

    def __init__(self, titular_c, saldo_c):
        if type(titular_c) != Persona:
            raise Exception("El parámetro no es el tipo Persona")
        self.titular_c = titular_c
        if type(saldo_c) != int:
            raise Exception("Saldo inicial incorrecto")
        self.saldo_c = saldo_c
        self.__historic.append(self.saldo_c)

    def resumen(self):
        print(f"{self.titular_c}. Saldo: {self.saldo_c}€")

    def agregar_saldo(self, ncantidad):
        if type(ncantidad) != int:
            raise Exception("Cantidad a agregar incorrecta")
        if ncantidad <= 0:
            raise Exception("El ingreso no puede ser negativo ni cero.")

        self.saldo_c += ncantidad
        self.__historic.append(self.saldo_c)
        print(f"Se ha añadido {ncantidad}€. Su cuenta ahora dispone de {self.saldo_c}€")

    def retirar_saldo(self, ncantidad):
        if type(ncantidad) != int:
            raise Exception("Cantidad a retirar incorrecta")
        if ncantidad <= 0:
            raise Exception("Debe de retirar una cantidad positiva.")
        if self.saldo_c < ncantidad:
            raise Exception("Operación imposible: No dispone de suficiente saldo.")

        self.saldo_c -= ncantidad
        self.__historic.append(self.saldo_c)
        print(f"Se ha retirado {ncantidad}€. Su cuenta ahora dispone de {self.saldo_c}€")

    def historic(self):
        print(self.__historic)
