class Calculadora:

    def __init__(self, num1, num2):
        self.numero1 = int(num1)
        self.numero2 = int(num2)

    def suma(self):
        return self.numero1 + self.numero2

    def resta(self):
        return self.numero1 - self.numero2

    def multiplicacion(self):
        return self.numero1 * self.numero2

    def division(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "No se puede dividir entre 0"

    def potencia(self):
        return self.numero1 ** self.numero2

    def resutados(self):
        return (f"Suma {self.suma()}\n"
                f"Resta {self.resta()}\n"
                f"Multiplicacion {self.multiplicacion()}\n"
                f"Division {self.division()}\n"
                f"Potencia {self.potencia()}\n")


print("----------Calculadora Basica----------")
while True:
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    calculadora = Calculadora(numero1, numero2)
    while True:
        opcion1 = int(input("Que quieres hacer\n"
                            "1.Introducir de nuevo los numeros\n"
                            "2.Ver las opciones de la calculadora\n"
                            "3.Salir del programa\n"))
        if opcion1 == 1:
            break
        elif opcion1 == 2:

            operacion = int(input("Ingrese la operacion deseada\n"
                                  "1. Suma \n"
                                  "2.Resta \n"
                                  "3. Multiplicacion \n"
                                  "4. Division \n"
                                  "5. Potencia \n"
                                  "6.Todo lo anterior\n"
                                  "7.Salir\n"))

            if operacion == 1:
                print(calculadora.suma())
            elif operacion == 2:
                print(calculadora.resta())
            elif operacion == 3:
                print(calculadora.multiplicacion())
            elif operacion == 4:
                print(calculadora.division())
            elif operacion == 5:
                print(calculadora.potencia())
            elif operacion == 6:
                print(calculadora.resutados())
            elif operacion == 7:
                print("Saliendo del apartado operaciopnes...")
            else:
                print("introduce la opcion correcta")
        elif opcion1 == 3:
            break
        else:
            print("Seleccione una opcion valida")

    if opcion1 == 3:
        break
