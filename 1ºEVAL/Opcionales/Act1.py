def ip(numeros):
    numip = []
    #numip=numeros.split(".")
    temp = ""
    pos = 1
    for i in numeros:
        if i != ".":
            temp += i
        else:
            numip.append(temp)
            temp = ""
        if pos == len(numeros):
            numip.append(temp)
        pos += 1

    return numip


def compruebanum(num):
    iplist = []
    iplist = ip(num)
    tempint = 0
    ok = True
    largo = False
    if len(iplist) == 4:
        largo = True

    for i in iplist:
        tempint = int(i)
        if tempint < 0 or tempint > 255:
            ok = False
            break
    if largo and ok:
        return True
    else:
        return False


num = input("Introduce una direccion ip y te dire si es correcta o no\n")
print(f"Tu ip es {compruebanum(num)}")
