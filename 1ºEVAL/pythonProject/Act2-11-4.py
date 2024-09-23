def bisiesto(anyo):
    if anyo % 4 == 0 and anyo % 100 != 0:
        return True
    elif anyo % 400 == 0 and anyo % 100 == 0 and anyo % 4 == 0:
        return True
    else:
        return False

print(f"Introduce años y te diremos si es bisiestro (True) o no (False) cuando introduzcas 0 el programa acabara")

while True:
    anyo=int(input())
    if anyo==0:
        break
    else:
        print(f"{anyo} ----> {bisiesto(anyo)}")

