num1 = int(input("Indica un numero\n"))
num2 = int(input("Indica otro numero\n"))
num3 = int(input("Indica el ultimo numero\n"))

if num1 > num2 and num1 > num3:
    print(f"El numero {num1} es el mayor")
    if num2 > num3:
        print(f"El numero {num3} es el menor")
    else:
        print(f"El numero {num2} es el menor")


elif num1 < num2 > num3:
    print(f"El numero {num2} es mayor")
    if num1 > num3:
        print(f"El numero {num3} es el menor")
    else:
        print(f"El numero {num1} es el menor")


elif num1 < num3 and num2 < num3:
    print(f"El numero {num3} es mayor")
    if num1 > num2:
        print(f"El numero {num2} es el menor")
    else:
        print(f"El numero {num1} es el menor")
