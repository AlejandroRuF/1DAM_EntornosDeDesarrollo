def func1(num1, num2, num3, car1, car2, car3):
    if (type(num1) != int) or (type(num2) != int) or (type(num3) != int):
        print("Tipo incorrecto esperado para num")
        return False

    if (type(car1) != str) or (type(car2) != str) or (type(car3) != str):
        print("Tipo incorrecto esperado para car")
        return False

    if len(car1) != 1:
        print("Longitud incorrecta para car1")
        return False

    if len(car2) != 1:
        print("Longitud incorrecta para car2")
        return False

    if len(car3) != 1:
        print("Longitud incorrecta para car3")
        return False

    temp2 = num2

    while num1 <= temp2:
        print(car1)
        temp2 -= 1

    while num3 >= temp2:
        print(car2)
        temp2 += 1

    if ord(car1) + ord(car2) + ord(car3) == 230:
        if ord(car1) + ord(car3) == 160:
            print(car3)
        else:
            print(car2)

    if ord(car1) < ord(car2):
        if ord(car1) < ord(car3):
            print("OK")
        else:
            print("MAL")

    if num1 % 2 == 0 and ord(car1) % 2 == 0:
        for i in range(num3):
            print(car2)


def func2(cadena):
    if type(cadena) != str:
        print("Tipo incorrecto esperado para cadena")
        return False
    if cadena == "":
        print("Cadena vacía")
        return False
    for i in range(0, int(len(cadena) / 2)):
        if cadena[i] != cadena[len(cadena) - i - 1]:
            return False
    return True
