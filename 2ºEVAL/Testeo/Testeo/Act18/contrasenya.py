import hashlib


class Contrasenya:
    __contrasena = ""
    __longitud = 0
    __minus = 0
    __mayus = 0
    __nums = 0
    __simbolos = 0

    # Constructor de la clase
    def __init__(self, ncontrasena, nlongitud, nminus, nmayus, nnums, nsimbolos):
        self.set_minus(nminus)
        self.set_mayus(nmayus)
        self.set_nums(nnums)
        self.set_simbolos(nsimbolos)
        self.set_longitud(nlongitud)
        self.set_contrasena(ncontrasena)

    # Setter número de símbolos mínimo
    def set_simbolos(self, nsimbolos):
        if type(nsimbolos) != int:
            raise Exception("El número de símbolos debe de ser un entero")
        if nsimbolos < 0:
            raise Exception("El número de símbolos tiene que ser mayor o igual que cero")
        self.__simbolos = nsimbolos

    # Getter número de símbolos mínimo
    def get_simbolos(self):
        return self.__simbolos

    # Setter número de números mínimo
    def set_nums(self, nnums):
        if type(nnums) != int:
            raise Exception("El número de números debe de ser un entero")
        if nnums < 0:
            raise Exception("El número de números tiene que ser mayor o igual que cero")
        self.__nums = nnums

    # Getter número de números mínimo
    def get_nums(self):
        return self.__nums

    # Setter número de mayúsculas mínimo
    def set_mayus(self, nmayus):
        if type(nmayus) != int:
            raise Exception("El número de mayúsculas debe de ser un entero")
        if nmayus < 0:
            raise Exception("El número de mayúsculas tiene que ser mayor o igual que cero")
        self.__mayus = nmayus

    # Getter número de mayúsculas mínimo
    def get_mayus(self):
        return self.__mayus

    # Setter número de minúsculas mínimo
    def set_minus(self, nminus):
        if type(nminus) != int:
            raise Exception("El número de minúsculas debe de ser un entero")
        if nminus < 0:
            raise Exception("El número de minúsculas tiene que ser mayor o igual que cero")
        self.__minus = nminus

    # Getter número de minúsculas mínimo
    def get_minus(self):
        return self.__minus

    # Setter longitud mínimo
    def set_longitud(self, nlongitud):
        if type(nlongitud) != int:
            raise Exception("La longitud debe de ser un entero")
        if nlongitud <= 0:
            raise Exception("La longitud de la contraseña tiene que ser un número positivo")
        if nlongitud < (self.__nums + self.__mayus + self.__minus + self.__simbolos):
            raise Exception("La longitud mínima de la contraseña no cumple requisitos")
        self.__longitud = nlongitud

    # Getter longitud mínimo
    def get_longitud(self):
        return self.__longitud

    # Setter contraseña
    def set_contrasena(self, ncontrasena):
        if type(ncontrasena) != str:
            raise Exception("La contraseña debe de ser una cadena")
        if ncontrasena == "":
            raise Exception("La contraseña no puede estar vacía")
        self.__contrasena = ncontrasena
        self.check_contrasena()

    # Getter contraseña
    def get_contrasena(self):
        return self.__contrasena

    # Comprobador que la contraseña tiene todos los requisitos mínimos
    def check_contrasena(self):
        if not self.check_longitud():
            raise Exception("La contraseña no tiene la lontigud mínima indicada")
        if not self.check_minus():
            raise Exception("La contraseña no tiene el número mínimo de minúsculas indicados")
        if not self.check_mayus():
            raise Exception("La contraseña no tiene el número mínimo de mayúsculas indicados")
        if not self.check_nums():
            raise Exception("La contraseña no tiene el número mínimo de números indicados")
        if not self.check_simbolos():
            raise Exception("La contraseña no tiene el número mínimo de símbolos indicados")

    # Comprobador longitud mínima
    def check_longitud(self):
        if len(self.__contrasena) < self.__longitud:
            return False
        else:
            return True

    # Contador número minúsculas
    def count_minus(self):
        contminus = 0
        for x in range(len(self.__contrasena)):
            if self.__contrasena[x].islower():
                contminus += 1
        return contminus

    # Comprobador longitud mínima minúsculas
    def check_minus(self):
        if self.count_minus() < self.__minus:
            return False
        else:
            return True

    # Contador número mayúsculas
    def count_mayus(self):
        contmayus = 0
        for x in range(len(self.__contrasena)):
            if self.__contrasena[x].isupper():
                contmayus += 1
        return contmayus

    # Comprobador longitud mínima mayúsculas
    def check_mayus(self):
        if self.count_mayus() < self.__mayus:
            return False
        else:
            return True

    # Contador número números
    def count_nums(self):
        contnums = 0
        for x in range(len(self.__contrasena)):
            if self.__contrasena[x].isdigit():
                contnums += 1
        return contnums

    # Comprobador longitud mínima números
    def check_nums(self):
        if self.count_nums() < self.__nums:
            return False
        else:
            return True

    # Contador número símbolos
    def count_simbolos(self):
        return len(self.__contrasena) - self.count_mayus() - self.count_minus() - self.count_nums()

    # Comprobador longitud mínima símbolos
    def check_simbolos(self):
        if self.count_simbolos() < self.__simbolos:
            return False
        else:
            return True

    # Cálculo hash sha256
    def sha256(self):
        hashsha256 = hashlib.sha256(self.__contrasena.encode())
        return hashsha256.hexdigest()

    # Cálculo hash sha512
    def sha512(self):
        hashsha512 = hashlib.sha512(self.__contrasena.encode())
        return hashsha512.hexdigest()

    # Cálculo hash md5
    def md5(self):
        hashmd5 = hashlib.md5(self.__contrasena.encode())
        return hashmd5.hexdigest()

    def __str__(self):
        print(f"Contraseña: {self.__contrasena}")
        print(f"Longitud: {len(self.__contrasena)} -> Mínima: {self.__longitud}")
        print(f"Número Minúsculas: {self.count_minus()} -> Mínimo: {self.__minus}")
        print(f"Número Mayúsculas: {self.count_mayus()} -> Mínimo: {self.__mayus}")
        print(f"Número Dígitos: {self.count_nums()} -> Mínimo: {self.__nums}")
        print(f"Número Símbolos: {self.count_simbolos()} -> Mínimo: {self.__simbolos}")
        print(f"Hash sha256: {self.sha256()}")
        print(f"Hash sha512: {self.sha512()}")
        print(f"Hash md5: {self.md5()}")
        return ""

