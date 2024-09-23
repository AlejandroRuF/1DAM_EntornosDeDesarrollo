print(f"Indica una fecha del siglo 21")
dia = int(input("Pon el dia\n"))
mes = int(input("Pon el mes\n"))
anyo = int(input("Pon el año en formato aaaa\n"))
bisiesto = bool(0)

if anyo % 4 == 0 and anyo % 100 != 0:
    bisiesto = 1
elif anyo % 400 == 0 and anyo % 100 == 0 and anyo % 4 == 0:
    bisiesto = 1

if 31 >= dia > 0:
    if mes == 2 and bisiesto == 0 and dia <= 29:
        print(f"El mes {mes} no tiene tantos dias")

    elif dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11 or mes == 2):

        print(f"El mes {mes} no tiene tantos dias")
    else:
        print(f"Has introducido los dias correctamente")
else:
    print(f"El mes {mes} no tiene tantos dias")

if 12 >= mes >= 1:
    print(f"Has introducido el mes correctamente")
else:
    print(f"Los meses van del 1 al 12")

if 2001 <= anyo <= 2100:
    print(f"Has introducido el año correctamente")
else:
    print(f"El año {anyo} no es del siglo 21")
