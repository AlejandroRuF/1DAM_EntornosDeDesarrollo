def bisiesto(anyo):

    if not anyo % 4:
        if not anyo % 100:     # divisible entre 4 y 100
            if not anyo % 400:  # divisible entre 4, 100 y 400
                return True
            else:              # divisible entre 4 y 100 y no entre 400
                return False
        else:                 # divisible  entre 4 y no entre 100
            return True
    else:                    # no divisible entre 4
        return False

