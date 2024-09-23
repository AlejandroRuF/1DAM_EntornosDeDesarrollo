def segle21(dia, mes, anyo):
    print("*** Programa que indica si una fecha es del siglo XXI")

    # Creamos una variable booleana que indique si el año es bisiesto o no
    bisiesto = anyo % 4 == 0 and (anyo % 100 != 0 or anyo % 400 == 0)

    if anyo < 2001 or anyo > 2100:  # Comprobamos año
        print("El año esta mal")
        return False
    elif mes < 1 or mes > 12:  # Comprobamos mes
        print("El mes esta mal")
        return False
    elif dia < 1 or dia > 31:  # Comprobamos que día está dentro del rango permitido
        print("El día esta mal")
        return False
    elif dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        # Comprobamos que abril, junio, septiembre y noviembre no tienen 31 días
        print("Demasiados días para este mes")
        return False
    elif mes == 2 and bisiesto and dia > 29:  # Si es bisiesto el dia tiene 29 dias
        print("Febrero en un año bisiesto tiene como mucho 29 días")
        return False
    elif mes == 2 and not bisiesto and dia > 28:
        print("Febrero en un año no bisiesto tiene como mucho 28 días")
        return False
    else:
        print("La fecha introducida es correcta")
        return True


