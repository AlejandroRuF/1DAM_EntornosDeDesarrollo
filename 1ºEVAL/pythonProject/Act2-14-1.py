def contrario(palabra):
    cpalabra=""
    for i in range(len(palabra)-1,-1,-1):
        cpalabra +=palabra[i]


    return cpalabra

palabra = input("Dime una palabra y te la devolvere inversa\n")
print(contrario(palabra))