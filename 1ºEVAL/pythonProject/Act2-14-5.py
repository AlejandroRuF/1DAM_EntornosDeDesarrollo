def vocal(caracter):
    if caracter.lower() == "a" or caracter.lower() == "e" or caracter.lower() == "i" or caracter.lower() == "o" or caracter.lower() == "u":
        return True
    else:
        return False

def vocals(palabra):
    vocales=0
    for i in palabra:
        if vocal(i):
            vocales += 1
    return vocales

palabra= input("Dime una letra y te dire si es una vocal, dime una palabra y te dire cuantas vocales tiene\n")

if len(palabra)==1:
    print(f"{palabra} ---> {vocal(palabra)}")
else:
    print(f"{palabra} ---> tiene {vocals(palabra)} vocales")