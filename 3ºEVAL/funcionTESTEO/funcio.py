def check_dni(dni):
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


if __name__ == "__main__":
    # try:
    assert (check_dni("46488008V") == True)
    assert (check_dni("53376118H") == True)
    assert (check_dni("38237444J") == True)
    assert (check_dni("84317227D") == True)
    assert (check_dni("07267666B") == True)
    assert (check_dni("58252795M") == True)

    assert (check_dni("46488008X") == False)
    assert (check_dni("46488008") == False)
    assert (check_dni("464880085855X") == False)
    assert (check_dni("X46488008") == False)
    assert (check_dni("46488X008X") == False)
    assert (check_dni("46488X") == False)
    assert (check_dni("46488008v") == False)
    assert (check_dni("ABCDEFGSQ") == False)

    # except Exception as e:
    #     print(e)
