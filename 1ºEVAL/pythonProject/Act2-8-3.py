numero=int(input("Escribe un numero cuando escribas '0' el bucle terminara\n"))
numeroant=-999999999
while numero!=0:

    if numeroant>=numero:
        print(f"El numero debe ser mayor que {numeroant}")
    else:
        numeroant = numero

    numero = int(input())