from Persona import Persona


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

