class Ip:
    __dirIP = []
    __IPc: str

    def set_ip(self, IP):
        dir = []

        if isinstance(IP, str):
            dir1 = []
            dir1 = IP.split(".")
            dir = []
            IPstr = ""
            contador1 = 0
            for i in dir1:
                temp = i
                temp = int(temp)
                dir.append(temp)
                IPstr += str(temp)
                if contador1 != 3:
                    IPstr += "."
                contador1 += 1

            if len(dir) == 4:
                octeto = 0
                for i in dir:
                    if i > 255 or i < 1 and octeto == 0:
                        raise Exception("Los numeros del primer octeto de la ip solo puede ser un rango entre 1 y 255")
                    elif i > 255 or i < 0 and octeto != 0:
                        raise Exception("Los numeros de cada octeto de la ip solo puede ser un rango entre 0 y 255")
                    else:
                        self.__dirIP = dir
                        self.__IPc = IPstr
                        octeto += 1

            else:
                raise Exception("La direccion ip no esta dividida en 4 bloques")

        else:
            raise ("La IP debe ser una cadena de numeros entre el 0 y 255 divididos en 4 bloques por un punto")

    def get_ip(self):
        return self.__dirIP

    def get_IPstr(self):
        return self.__IPc

    def __init__(self, dirIP):
        self.set_ip(dirIP)

    def claseIP(self):
        if 0 <= self.get_ip()[0] <= 126:
            return "Clase A"
        elif 128 <= self.get_ip()[0] <= 191:
            return "Clase B"
        elif 192 <= self.get_ip()[0] <= 223:
            return "Clase C"
        elif 224 <= self.get_ip()[0] <= 239:
            return "Clase D"
        elif 240 <= self.get_ip()[0] <= 255:
            return "Clase E"
        elif self.get_ip()[0] == 127:
            return "La direccion IP esta reservada para el lootpack de la propia maquina y no tiene clase como tal"

    def publica_Privada(self):
        # 10.0.0.0 — 10.255.255.255; 172.16.0.0 — 172.31.255.255; 192.168.0.0 — 192.168.255.255
        if self.get_ip()[0] == 10 or (self.get_ip()[0] == 172 and 16 <= self.get_ip()[1] <= 31) or (
                self.get_ip()[0] == 192 and self.get_ip()[1] == 168):
            return "Privada"
        else:
            return "Publica"

    def privada(self):
        if self.publica_Privada() == "Privada":
            return True
        else:
            return False

    def octet(self, num_Octeto):
        return self.get_ip()[num_Octeto]

    def __str__(self):
        dircom: str = ""
        for i in range(len(self.get_ip())):
            if self.get_ip() != 3:
                dircom += str(self.get_ip()[i]) + "."
            else:
                dircom += str(self.get_ip()[i])

        return f"Tu direccion IP es {dircom} su clase es {self.claseIP()} y pertenece al tipo {self.publica_Privada()}"


class Red:
    __nombre: str
    __IPs: list = []

    def set_nombre(self, nom):
        if isinstance(nom, str):
            self.__nombre = nom

    def get_nombre(self):
        return self.__nombre

    def set_IPs(self, IP):

        if isinstance(IP, str) and self.contarIP() == 0:
            nuIP = Ip(IP)
            self.__IPs.append(nuIP.get_IPstr())

        elif isinstance(IP, str) and self.contarIP() != 0:
            ip = []
            temp = str(self.get_IPs()[0])
            ip = temp.split(".")
            ip0 = IP.split(".")
            if (ip[0] == ip0[0] and ip[1] == ip0[1]
                    and ip[2] == ip0[2]):
                for i in self.get_IPs():
                    temp2 = str(i)
                    if temp2 == IP:
                        raise Exception("Esa IP ya existe en tu red")

                nuIP = Ip(IP)
                self.__IPs.append(nuIP.get_IPstr())
            else:
                raise Exception("Las IP deben pertenecer a la misma red siendo los 3 primeros octetos iguales")

        else:
            raise Exception("La IP debe ser una cadena")

    def get_IPs(self):
        return self.__IPs

    def contarIP(self):
        return len(self.get_IPs())

    def mostrar_red(self):
        for i in self.get_IPs():
            print(i)

    def __init__(self, nombre):
        self.set_nombre(nombre)


if __name__ == "__main__":
    print("Vamos a crear una red privada para casa y almacenar las ip para ello vamos a crear una serie de IP de las "
          "cuales te diremos si son correctas o no")

    red1 = Red("1")

    while True:
        try:
            opcion = input("Elija la opcion que desee:\n"
                           "1- Comprobar las caracteristicas de una IP candidata\n"
                           "2- Nombrar  nuestra red\n"
                           "3- Guardar IPs compatibles en nuestra red\n"
                           "4- Mostrar la red que hemos creado\n"
                           "5- Salir\n")

            if opcion == "1":
                ipn = Ip(input("Escribe la IP que quieres comprobar\n"))
                print(ipn)

            elif opcion == "2":
                red1.set_nombre(input("Escribe el nombre que quieres darle a tu red\n"))
                print(f"El nobre de tu red se ha establecido como: {red1.get_nombre()}")

            elif opcion == "3":
                num = 1
                while True:
                    red1.set_IPs(
                        input("Escribe la IP que quieres utilizar si quieres comprobar sus caracteristicas usa la "
                              "opcion 1 del menu anterior\n"))

                    while True:
                        fuera = False
                        repetir = input("Quieres introducir otra ip para tu red?(S/N)\n")
                        if repetir.upper() == "N":
                            fuera = True
                            break
                        elif repetir.upper() == "S":
                            num += 1
                            print(f"Escribe la ip nº {num}")
                            break
                        else:
                            print("Introduce S/N")
                    if fuera:
                        break

            elif opcion == "4":
                if len(red1.get_IPs()) == 0:
                    print("Primero debes introducir alguna IP")
                elif len(red1.get_IPs()) > 0:
                    red1.mostrar_red()

            elif opcion == "5":
                break
            else:
                print("Escribe una opcion valida")
        except Exception as e:
            print(e)
