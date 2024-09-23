def cuadrado(numero):
    lista=[]
    for i in range(0,numero,1):
        lista.append(numero)

    for i in lista:
        print(f"{i} "*numero)



numero= int(input("Escribe un numero\n"))

cuadrado(numero)
