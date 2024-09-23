def cambio():
    print(f"Introduce el tamño de los dibujos")
    return int(input())


def triangulo(tamanyot):
    for i in range(0, tamanyot, 1):
        for x in range(0, i + 1, 1):
            print("*", end="")
        print()


def cuadrado(tamanyoc):
    for i in range(0, tamanyoc, 1):
        for x in range(0, tamanyoc + 1, 1):
            print("*", end="")
        print()


def menu():
    print(f"Elige una de las siguientes opciones\n1)Cambiar Tamaño\n2)Imprimir Triangulo\n3)Imprimir cuadrado\n4)Salir")
    opcionm = int(input())
    return opcionm


tamanyo = int(5)
opcion = 0
while opcion != 4:
    opcion = menu()
    if opcion == 1:
        tamanyo = cambio()
    elif opcion == 2:
        triangulo(tamanyo)
    elif opcion == 3:
        cuadrado(tamanyo)
