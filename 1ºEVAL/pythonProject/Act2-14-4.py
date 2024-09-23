def final_igual(palabrax, palabray):
    comuninv = ""
    comun = ""
    pos = -1
    while True:

        if palabrax[pos] == palabray[pos]:
            comuninv += palabrax[pos]
        else:
            break
        pos -= 1

    comun = comuninv[::-1]
    return comun


palabra1 = input("Vamos a Escribir 2 palabras y ver las partes finales en comun\n"
                 "Introduce la primera palabra\n")
palabra2 = input("Introduce la segunda palabra\n")

print(f"El final comun es {final_igual(palabra1, palabra2)}")
