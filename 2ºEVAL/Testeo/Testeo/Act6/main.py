def ip_ok(ip):
    lista = ip.split(".")
    check = 0
    if len(lista) == 4:
        check += 1
    else:
        print(f"La IP és incorrecta -> No té 4 blocs")

    for x in range(len(lista)):
        if int(lista[x]) > 256:
            print(f"La IP és incorrecta -> El bloc {x+1} és major que 256")
        elif int(lista[x]) < 0:
            print(f"La IP és incorrecta -> El bloc {x + 1} és menor que 0")
        else:
            check += 1
    if check == 5:
        print(f"La IP és correcta")


if __name__ == "__main__":
    ip_ok("1.2.3.4")
    ip_ok("500.1.1.1")
    ip_ok("1.1")
    ip_ok("1.-1.1.1")

