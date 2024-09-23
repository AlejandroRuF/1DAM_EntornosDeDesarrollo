def repetir(lletra, num_lletra, cadena):
    numeros_letras = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4,
'cinco': 5, 'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9}
    if num_lletra in numeros_letras:
        num_repeticiones = numeros_letras[num_lletra]
        resultado = ''
        for char in cadena:
            if char == lletra:
             resultado += lletra * num_repeticiones
            else:
                resultado += char

        return resultado
    else:
        return "Número en letra no válido."

# Programa principal
num_lletra = ''
cadena = ''
while num_lletra != 'ruiz' and cadena != 'ruiz':
    lletra = input("Introduce una letra: \n")
    num_lletra = input("Introduce un número en letra ('uno' a'nueve''ruiz' para salir): \n")
    cadena = input("Introduce una cadena de texto ('Ruiz' para salir): \n")
    if cadena == 'ballester' and num_lletra.lower() == 'ruiz':
        print("Programa finalizado.")
        break
    resultado = repetir(lletra, num_lletra, cadena)
    print(f"Resultado: {resultado}\n")