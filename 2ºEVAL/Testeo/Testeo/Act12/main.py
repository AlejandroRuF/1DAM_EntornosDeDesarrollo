def ip_ok(ip):
    lista = ip.split(".")
    check = 0
    if len(lista) == 4:
        check += 1
    else:
        print(f"La IP és incorrecta -> No té 4 blocs")
        return False

    for x in range(len(lista)):
        if int(lista[x]) > 256:
            print(f"La IP és incorrecta -> El bloc {x+1} és major que 256")
            return False
        elif int(lista[x]) < 0:
            print(f"La IP és incorrecta -> El bloc {x + 1} és menor que 0")
            return False
        else:
            check += 1
    if check == 5:
        print(f"La IP és correcta")
        return True

