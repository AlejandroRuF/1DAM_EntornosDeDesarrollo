def letras(car):
    if 'A' <= car <= 'Z':
        return True
    else:
        return False


def numero(car):
    if '0' <= car <= '9':
        return True
    else:
        return False


def dni_ok(dnifunc):
    pos = 1
    largo = False
    letraPos = False
    numeros = True
    #letra = False

    if len(dnifunc) == 9:
        largo = True

    for i in dnifunc:

        if letras(i) and pos != (len(dnifunc)):
            letraPos = False
            break
        if letras(i) and pos == (len(dnifunc)):
            letraPos = True
            if letraPos:
                letradni = i
        if numero(i)== False  and pos < (len(dnifunc)):
            numeros = False
            break

        pos += 1

    if numeros and letraPos and largo:
        pos = 0
        temp = ""
        for i in dnifunc:
            if pos != 8:
                temp = temp + i
            pos += 1
        numerodni = int(temp)
        if letradni == lletra_dni(numerodni):
            print(f"El DNI {dnifunc} es True")
            return True
        else:
            print(f"La letra correcta para ese numero de dni seria {lletra_dni(numerodni)}")
            return False

    else:
        print("Los datos introducidos no son correctos")
        return False


def letra_dni(numerofunc):
    tabla_letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    letra = tabla_letras[numerofunc % 23]
    return letra


dni = int(1)
while dni != 0:
    dni = input("Introduce un numero de DNI para saber si es correcto (con la letra en mayuscula) para acabar introduce 0\n")
    dni_ok(dni)

