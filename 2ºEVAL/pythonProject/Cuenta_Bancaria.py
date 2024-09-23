from Persona1 import Persona


class Cuenta_Bancaria:
    __titular = None
    __saldo = 0
    __historial: float = [0]

    def __init__(self, titular: Persona, saldo: float):

        self.set_Persona(titular)
        self.set_saldo(saldo)

    def set_saldo(self, sald):
        if isinstance(sald, float) and sald >= 0:
            self.__saldo = sald
            self.historialCB()
        else:
            raise Exception("El numero introducido debe ser mayor o igual a 0")

    def set_Persona(self, titular: Persona):
        if isinstance(titular, Persona):
            self.__titular = titular
        else:
            raise Exception("El dato debe ser de tipo Persona")

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def ingresar(self, cantidad):
        if isinstance(cantidad, float) and cantidad > 0:
            self.__saldo += cantidad
            self.historialCB()
        else:
            raise Exception("La cantidad a ingresar debe ser mayor a 0")

    def retirar(self, cantidad):
        if isinstance(cantidad, float) and cantidad > 0:
            self.__saldo -= cantidad
            self.historialCB()
        else:
            raise Exception("La cantidad a retirar debe ser mayor a 0")

    def historialCB(self):
        self.__historial.append(self.get_saldo())

    def get_historial(self):
        return self.__historial

    def mostrar_Datos(self):
        print(f"La cuenta tiene los siguientes datos:"
              f"\nTitular: {self.get_titular()}"
              f"\nSaldo: {self.get_saldo()}")

    def __str__(self):
        return (f"La cuenta tiene los siguientes datos:"
                f"\nTitular: {self.get_titular()}"
                f"\nSaldo: {self.get_saldo()}")


if __name__ == "__main__":

    print("Para crear la cuenta bancaria del cliente introduce los siguientes datos")
    persona1 = None
    cuenta1 = None
    while True:
        error = False
        try:
            nombre = input("Introduce un nombre (Solo caracteres alfabeticos)\n")
            dni = input("Introduce tu DNI \n")
            edad = int(input("Introduce tu edad (Tiene que estar entre 0 y 99)\n"))
            persona1 = Persona(nombre, edad, dni)
            saldo = float(input("Introduce el saldo total del cliente\n"))
            cuenta1 = Cuenta_Bancaria(persona1, saldo)

        except Exception as e:
            print(f"{e}")
            error = True

        if not error:
            cuenta1.mostrar_Datos()
            break

    while True:
        opcion = int(input("Que quieres hacer?\n"
                           "1-Ingresar dinero\n"
                           "2- Retirar dinero\n"
                           "3- Mostrar Saldo\n"
                           "4-Mostrar historial\n"
                           "5-Salir\n"))

        if opcion == 1:
            cuenta1.ingresar(float(input("Introduce la cantidad a ingresar\n")))

        elif opcion == 2:
            cant_ret = float(input("Introduce la cantidad a retirar\n"))
            if cant_ret > cuenta1.get_saldo():
                print("No puede retirar una cantidad mayor al saldo de la cuenta")
            else:
                cuenta1.retirar(cant_ret)

        elif opcion == 3:
            print(cuenta1.get_saldo())

        elif opcion == 5:
            break

        elif opcion == 4:
            contador = 0
            temp = 0
            mov = 0
            for i in cuenta1.get_historial():
                if i < temp:
                    mov = (i - temp)
                elif i > temp:
                    mov = i - temp

                print(f"Saldo en movimiento {contador}:      ", end="")

                print(f"{mov} ---> {i}")

                contador += 1

                temp = i

        else:
            print("Introduce una opcion correcta")
