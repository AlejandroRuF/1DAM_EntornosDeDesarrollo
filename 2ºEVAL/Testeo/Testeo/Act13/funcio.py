def check_dni(dni):
    if type(dni) != str:
        raise Exception("Tipus de dada incorrecta")
    if len(dni) == 0:
        raise Exception("La Cadena esta vacia")
    lletres = "TRWAGMYFPDXBNJZSQVHLCKE"
    numeros = "1234567890"
    result = False
    if len(dni) == 9:
        lletra_control = dni[8].upper()
        dni = dni[:8]
        if len(dni) == len([n for n in dni if n in numeros]):
            if lletres[int(dni) % 23] == lletra_control:
                result = True
    return result
