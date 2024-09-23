def vocal(caracter):
    vocales = "aeiouAEIOU"
    if caracter in vocales:
        return True
    else:
        return False


def digito(caracter):
    digitosok = "12345"
    if caracter in digitosok:
        return True
    else:
        return False


def simbolo(caracter):
    simbolos = "$%&"
    if caracter in simbolos:
        return True
    else:
        return False


def comprobar(cadena):
    vocalok = True
    digitok = True
    simbolook = True
    for i in range(0, len(cadena), 3):
        if not vocal(cadena[i]):
            vocalok = False
    for i in range(1, len(cadena), 3):
        if not digito(cadena[i]):
            digitok = False
    for i in range(2, len(cadena), 3):
        if not simbolo(cadena[i]):
            simbolook = False

    if vocalok and digitok and simbolook:
        return True
    else:
        return False


entrada = ""
while entrada != "salvadorgadea":
    entrada = input("Introduce una cadena y te dire si esta con el formato indicado en la hoja\n")

    print(f"La cadena {entrada} es -----> {comprobar(entrada)}")
