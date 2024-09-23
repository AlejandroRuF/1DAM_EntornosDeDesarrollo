def opera(lista1, lista2, caracter):
    resultadof = []

    if len(lista1) == len(lista2) and caracter in ["+", "-", "*"]:
        for i in range(len(lista1)):
            if caracter == "-" or caracter == "-":
                operacion = lista1[i] - lista2[i]
                resultadof.append(operacion)
            if caracter == "+":
                operacion = lista1[i] + lista2[i]
                resultadof.append(operacion)
            if caracter == "*":
                operacion = lista1[i] * lista2[i]
                resultadof.append(operacion)

    return resultadof


operador = ""
entrada = ""
while True:
    listan1 = []
    listan2 = []
    resultado = []
    print("Introduce 2 listas de numeros para realizar una operacion con ellos las listas deben ser del mismo tamaño"+
          " dejalas vacias para salir")

    pos = 1

    while True:

        entrada = int(input("Introduce numeros para la primera lista cuando acabes introduce 0\n"))
        if entrada != 0:
            listan1.append(entrada)
            print(f"Numeros introducidos ---> {pos}")
            pos += 1
        else:
            break
    pos = 1
    while True:
        entrada = int(input("Introduce numeros para la segunda lista cuando acabes introduce 0\n"))
        if entrada != 0:
            listan2.append(entrada)
            print(f"Numeros introducidos ---> {pos}")
            pos += 1
        else:
            break

    if len(listan1) == 0 and len(listan2) == 0:
        break
    else:
        operador = input("Introduce la operacion que quieras realizar '+', '-', '*'\n")
        resultado = opera(listan1, listan2, operador)
        print(listan1)
        print(operador)
        print(listan2)
        print(f"-----> {resultado}")
