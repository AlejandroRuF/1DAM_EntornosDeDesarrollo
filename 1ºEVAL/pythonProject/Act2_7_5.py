acaba = 1
while acaba != 0:

    cara = input("Introduce un caracter y te dire si es una vocal o no\n")

    if cara == "a" or cara == "e" or cara == "i" or cara == "o" or cara == "u" or cara == "A" or cara == "E" or cara == "I" or cara == "O" or cara == "U":
        print(f"{cara} --> VOCAL\n")
    else:
        print(f"{cara} --> NO VOCAL\n")

    if cara == "0":
        acaba = 0
