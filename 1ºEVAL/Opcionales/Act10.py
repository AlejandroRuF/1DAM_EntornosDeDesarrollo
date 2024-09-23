def barrejar(cadena1, cadena2):
    result = ''
    i = 0
    j = 0
    while i < len(cadena1) and j < len(cadena2):
        result += cadena1[i:i+2]
        result += cadena2[j:j+2]
        i += 2
        j += 2
    # Agregar el resto de la cadena si alguna de ellas es más corta
    result += cadena1[i:]
    result += cadena2[j:]

    return result

palabra1 = input('Escribe la cadena 1')
palabra2 = input('Escribe la cadena 2')
print(barrejar(palabra1, palabra2))