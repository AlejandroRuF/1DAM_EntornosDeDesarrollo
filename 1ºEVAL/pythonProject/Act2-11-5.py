def mail(correo):
    arroba=0
    posarroba=0
    punto=False
    pos=0
    pospunto=0

    for i in correo:
        if i==".":
            pospunto=pos
        if i == "." and pos==(len(correo)-1):
            punto=False
            break
        if i == "." and (posarroba + 1 == pos):
            punto=False
            break
        if i == "@" and pospunto == (posarroba-1):
            punto = False
            break
        if pos==0 and i=="@":
            break
        if i=="@":
            arroba+=1
            posarroba +=1
        if arroba==0 and i!="@" :
            posarroba +=1

        if i=="." and posarroba<pos :
            punto =True

        pos += 1


    if arroba==1 and punto:
        return True
    else:
        return False

correo=""

while True:
    correo = input("Introduce un correo y te dire si es correcto\n")
    if correo != "0":
        print(f"{correo} ----->   {mail(correo)}")
    else:
        print("Adios")
        break