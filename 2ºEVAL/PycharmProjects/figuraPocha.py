def creacionLinea(numero, posx, posy):
    cadenaLinea = str(numero)
    if posx == 1:
        return cadenaLinea
    if posx == 3:
        return cadenaLinea
    if numero % 2 == 0:
        if posy == 3:
            return cadenaLinea
        if posx == 2:
            if posy == 2 or posy == 1:
                return " "
    else:
        if posy == 1:
            return cadenaLinea
        if posx == 2:
            if posy == 2 or posy == 3:
                return " "

def creacionFigura(numero):
    longitudFigura = (numero*3)+1
    posiciony = 0
    cadenaImprimir = "0"

    for i in range(0,3,1):
        posiciony+=1
        posicionx = 0;
        for a in range(0,numero+1,1):
            posicionx += 1
            cadenaImprimir += f"{creacionLinea(a+1,posicionx,posiciony)}"
            posicionx += 1
            cadenaImprimir += f"{creacionLinea(a+1, posicionx, posiciony)}"
            posicionx += 1
            cadenaImprimir += f"{creacionLinea(a+1, posicionx, posiciony)}"
            posicionx = 0
        print(cadenaImprimir)
        cadenaImprimir = "0"



creacionFigura(6)