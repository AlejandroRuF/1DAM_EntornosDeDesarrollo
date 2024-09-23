from Cuenta_Bancaria import Cuenta_Bancaria
from Persona import Persona


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
    try:
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
    except Exception as e:
        print(e)
