def cuentapalabras(frase):
    """Funció que conta el número de vegades que apareix cada paraula en un text.
    Parámetres:
        - t: És una cadena de caràcters.
    Torna:
        Un diccionari amb paraula:freqüència amb les paraules del text i la seua freqüència.
    """
    frase = frase.split()
    contadorPalabras = {}
    for palabra in frase:
        if palabra in contadorPalabras:
            contadorPalabras[palabra] += 1
        else:
            contadorPalabras[palabra] = 1
    return contadorPalabras


def masRepetida(fraseContada):
    """Funció que conta la paraula amb més repeticions d'un diccionari en formato paraula:freqüència.
        Parámetres:
            - w: Diccionari
        Torna:
            la paraula del text que més es repeteix amb la seua freqüència.
        """
    PalabraMasRepetida = ''
    reepeticionesMaximas = 0
    for palabrasContadas, numRepetidas in fraseContada.items():
        if numRepetidas > reepeticionesMaximas:
            PalabraMasRepetida = palabrasContadas
            reepeticionesMaximas = numRepetidas
    return PalabraMasRepetida, reepeticionesMaximas


fraseAContar = 'No es veia cap ànima vivent ni es sentia una mosca en aquell immens edifici'
print(cuentapalabras(fraseAContar))
print(masRepetida(cuentapalabras(fraseAContar)))
