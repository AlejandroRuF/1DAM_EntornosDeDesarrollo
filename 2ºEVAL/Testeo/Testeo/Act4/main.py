def bisiesto(anyo):

    if not anyo % 4:
        if not anyo % 100:     # divisible entre 4 y 100
            if not anyo % 400:  # divisible entre 4, 100 y 400
                print("Es bisiesto")
            else:              # divisible entre 4 y 100 y no entre 400
                print("No es bisiesto")
        else:                 # divisible  entre 4 y no entre 100
            print("Es bisiesto")
    else:                    # no divisible entre 4
        print("No es bisiesto")


if __name__ == "__main__":
    bisiesto(2022)
    bisiesto(2020)
    bisiesto(2000)
    bisiesto(2004)
    bisiesto(1900)
