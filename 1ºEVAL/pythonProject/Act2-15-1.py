def vocal(caracter):
    if caracter.lower() == "a" or caracter.lower() == "e" or caracter.lower() == "i" or caracter.lower() == "o" or caracter.lower() == "u":
        return True
    else:
        return False


def vocals(palabra):
    vocales = 0
    for i in palabra:
        if vocal(i):
            vocales += 1
    return vocales


def consonant(caracter):
    if caracter.lower() in ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w",
                            "x", "y", "z"]:
        return True
    else:
        return False


def consonantes(palabra):
    consonats = 0
    for i in palabra:
        if consonant(i):
            consonats += 1
    return consonats


def espai(caracter):
    if caracter == " ":
        return True
    else:
        return False


def espais(palabra):
    espais = 0
    for i in palabra:
        if espai(i):
            espais += 1
    return espais


palabra = input(
    "Dime una letra y te dire que es, dime una palabra y te dire cuantas vocales, consonantes y espacios tiene\n")

if len(palabra) == 1:
    print(f"{palabra} es vocal ---> {vocal(palabra)}")
    print(f"{palabra} es consonante ---> {consonant(palabra)}")
    print(f"{palabra} es un espacio ---> {espai(palabra)}")
else:
    print(f"{palabra} ---> tiene {vocals(palabra)} vocales")
    print(f"{palabra} ---> tiene {consonantes(palabra)} consonantes")
    print(f"{palabra} ---> tiene {espais(palabra)} espacios")
