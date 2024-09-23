caracter=input("Dime un caracter alfanumerico\n")
cadena = input(f"Escribe una frase y te dire el numero de '{caracter}' que tiene\n")
contador = 0

for i in cadena:
    if i == caracter:
        contador = (contador + 1)

print(f"La frase {cadena} tiene {contador} '{caracter}'")
