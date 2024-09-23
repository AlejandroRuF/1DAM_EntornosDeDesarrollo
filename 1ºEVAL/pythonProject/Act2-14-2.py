def contrario(palabra):
    cpalabra=""
    for i in range(len(palabra)-1,-1,-1):
        if palabra[i] != " ":
            cpalabra +=palabra[i]

    return cpalabra

def palindromo(palabra):
    esPalindromo = False
    npalabra=""
    for i in range (0,len(palabra),1):
        if palabra[i] != " ":
         npalabra += palabra[i]
    if contrario(npalabra).lower() == npalabra.lower():
        esPalindromo = True

    return esPalindromo

palabra = input("Dime una palabra y te dire si es un palindromo\n")
print(f"La inversa de {palabra.lower()} es {contrario(palabra).lower()}? ---> {palindromo(palabra)}")

