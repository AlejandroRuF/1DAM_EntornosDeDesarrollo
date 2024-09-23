import hashlib


class Contrasenya:
    __contrasenya: str = ""
    __lonMinCarac: int = 1
    __numMinus: int = 1
    __numMayus: int = 0
    __numNums: int = 0
    __numSimb: int = 0

    def verificar_contrasnya(self, contrasenya):
        if len(contrasenya) > self.get_lonMinCarac():
            if self.__contador_Nums(contrasenya) >= self.get_numNums():
                if self.__contador_Minus(contrasenya) >= self.get_numMinus():
                    if self.__contador_Mayus(contrasenya) >= self.get_numMayus():
                        if self.__contador_Simb(contrasenya) >= self.get_numSimb():
                            return True
                        else:
                            raise Exception(
                                f"El numero minimo de simbolos que la contraseña debe contener es {self.get_numSimb()}")
                    else:
                        raise Exception(
                            f"El numero minimo de Mayusculas que la contraseña debe contener es {self.get_numMayus()}")
                else:
                    raise Exception(
                        f"El numero minimo de minusculas que la contraseña debe contener es {self.get_numMinus()}")
            else:
                raise Exception(f"El numero minimo de numeros que la contraseña debe contener es {self.get_numNums()}")

        else:
            raise Exception(f"La contraseña debe tener {self.get_lonMinCarac()} caracteres minimo")

    def set_contrasenya(self, contrasenya):
        if isinstance(contrasenya, str) and self.verificar_contrasnya(contrasenya):
            self.__contrasenya = contrasenya

    def get_contrasenya(self):
        return self.__contrasenya

    def set_lonMinCarac(self, minCarac):
        if isinstance(minCarac, int) and 30 > minCarac > 0 and self.verificar_suma():
            self.__lonMinCarac = minCarac
        else:
            raise Exception("El numero de caracteres introducido debe ser un entero superior a 0 e inferior a 30")

    def get_lonMinCarac(self):
        return self.__lonMinCarac

    def set_numMinus(self, numMinus):
        guardado=self.__numMinus
        if isinstance(numMinus, int) and 30 > numMinus > 0 and self.verificar_suma():
            self.__numMinus = numMinus
            if  not self.verificar_suma():
                self.__numMinus=guardado
                self.error_longitud()
        else:
            raise Exception("El numero de minusculas introducido debe ser un entero superior a 0 e inferior a 30")

    def get_numMinus(self):
        return self.__numMinus

    def set_numMayus(self, numMayus):
        guardado=self.__numMayus
        if isinstance(numMayus, int) and 30 > numMayus >= 0:
            self.__numMayus = numMayus
            if  not self.verificar_suma():
                self.__numMayus=guardado
                self.error_longitud()
        else:
            raise Exception("El numero de mayusculas introducido debe ser un entero igual o mayor a 0 e inferior a 30")

    def get_numMayus(self):
        return self.__numMayus

    def set_numNums(self, numNums):
        guardado=self.__numNums
        if isinstance(numNums, int) and 30 > numNums >= 0 and self.verificar_suma():
            self.__numNums = numNums
            if  not self.verificar_suma():
                self.__numNums=guardado
                self.error_longitud()
        else:
            raise Exception("El numero de numeros introducido debe ser un entero igual o mayor a 0 e inferior a 30")

    def get_numNums(self):
        return self.__numNums

    def set_numSimb(self, numSimb):
        guardado=self.__numSimb
        if isinstance(numSimb, int) and 30 > numSimb >= 0 and self.verificar_suma():
            self.__numSimb = numSimb
            if  not self.verificar_suma():
                self.__numSimb=guardado
                self.error_longitud()
        else:
            raise Exception("El numero de simbolos introducido debe ser un entero igual o mayor a 0 e inferior a 30")

    def get_numSimb(self):
        return self.__numSimb

    def __contador_Minus(self, contrasenya):
        minusculas = 0
        for i in contrasenya:
            if i in "qwertyuiopasdfghjklñzxcvbnm":
                minusculas += 1

        return minusculas

    def __contador_Mayus(self, contrasenya):
        mayus = 0
        for i in contrasenya:
            if i in "QWERTYUIOPASDFGHJKLÑZXCVBNM":
                mayus += 1
        return mayus

    def __contador_Nums(self, contrasenya):
        nums = 0
        for i in contrasenya:
            if i in "123456789":
                nums += 1
        return nums

    def __contador_Simb(self, contrasenya):
        simb = 0
        for i in contrasenya:
            if i in "!·$%&/()=¿¡?`^+*¨´-.:,;<>_{}[]ºª|@#~½¬":
                simb += 1
            if i in '"\\' or i in "'":
                raise Exception('Los simbolos "  \ y' + " ' no son aceptados")
        return simb

    def hash_sha256(self):
        hsha256 = hashlib.sha256()
        hsha256.update(self.get_contrasenya().encode("utf-8"))
        consha256= hsha256.hexdigest()
        return consha256

    def hash_md5(self):
        md5 = hashlib.md5()
        md5.update(self.get_contrasenya().encode("utf-8"))
        conshamd5 = md5.hexdigest()
        return conshamd5

    def __init__(self, lonMinCarac):
        self.set_lonMinCarac(lonMinCarac)

    def __str__(self):
        return "Que listo eres pero lo siento la contraseña no la puedes ver aqui"

    def verificar_suma(self):
        if 30 > (self.get_numMinus() + self.get_numMayus() + self.get_numNums() + self.get_numSimb()):
            return True
        else:
            return False

    def error_longitud(self):
        raise Exception("La suma de los requisitos no puede ser menor a la longitud maxima (30) de la contraseña")


if __name__ == "__main__":
    contador=False
    patron1 = Contrasenya(5)

    print("Bienvenido al comprobador de contraseñas que necesitas introduce las caracteristicas que deben tener"
          "las contraseñas de tus programas y nosotros nos encargamos de verificarlas")

    while True:
        try:
            opcion = (input(f"Que opcion deseas modificar\n"
                            f"1- Longitud minima de la contraseña (Actual: {patron1.get_lonMinCarac()})\n"
                            f"2- Minimo de caracteres en minuscula (Actual: {patron1.get_numMinus()})\n"
                            f"3- Minimo de caracteres en mayuscula (Actual: {patron1.get_numMayus()})\n"
                            f"4- Minimo de numeros (Actual: {patron1.get_numNums()})\n"
                            f"5- Minimo de Simbolos (Actual: {patron1.get_numSimb()})\n"
                            f"6- Comprobar contraseña\n"
                            f"7- hash la contraseña en sha256\n"
                            f"8- hash la contraseña en mb5\n"
                            f"9- Salir\n"))

            if opcion == "1":
                longitud = int(
                    input(f"La longitud actual es {patron1.get_lonMinCarac()} que cantidad seria adecuada para "
                          f"usted? (max. 30 min.1)\n"))
                patron1.set_lonMinCarac(longitud)

            elif opcion == "2":
                longitud = int(input(f"El minimo de minisculas actual es {patron1.get_numMinus()} "
                                     f"que cantidad seria adecuada para "
                                     f"usted? (max. 30 min.1)\n"))
                patron1.set_numMinus(longitud)

            elif opcion == "3":
                longitud = int(input(f"El minimo de mayusculas actual es {patron1.get_numMayus()} "
                                     f"que cantidad seria adecuada para "
                                     f"usted? (max. 30 min.0)\n"))
                patron1.set_numMayus(longitud)

            elif opcion == "4":
                longitud = int(input(f"El minimo de numeros actual es {patron1.get_numNums()} "
                                     f"que cantidad seria adecuada para "
                                     f"usted? (max. 30 min.0)\n"))
                patron1.set_numNums(longitud)

            elif opcion == "5":
                longitud = int(input(f"El minimo de simbolos actual es {patron1.get_numSimb()} "
                                     f"que cantidad seria adecuada para "
                                     f"usted? (max. 30 min.0)\n"))
                patron1.set_numSimb(longitud)

            elif opcion == "6":
                lcontrasenya = input(f"Introduce una contraseña valida para comprobar el patron\n")
                patron1.set_contrasenya(lcontrasenya)
                print(f"Contraseña ---> {patron1.verificar_contrasnya(lcontrasenya)}")
                contador = True


            elif opcion == "9":
                break

            elif opcion == "7":
                if contador:
                    print(f"La contraseña {patron1.get_contrasenya()} en sha256 es {patron1.hash_sha256()}")
                else:
                    print("Introduce una contraseña primero por favor")

            elif opcion == "8":
                if contador:
                    print(f"La contraseña {patron1.get_contrasenya()} en mb5 es {patron1.hash_md5()}")
                else:
                    print("Introduce una contraseña primero por favor")

            else:
                print(f"Introduce una opcion valida")

        except Exception as e:
            print(e)
