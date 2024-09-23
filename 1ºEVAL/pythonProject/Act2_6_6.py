print("Vamos a adivinar el superheroe")
vof= input("Puede volar (Si o no)\n")
if vof=="Si" or vof=="si":
    vof=input("Es Humano? (Si o No)\n")
    if vof=="Si" or vof== "si":
        vof=input("Lleva mascara? (Si o No)\n")
        if vof=="Si" or vof=="si":
            print("Estas Pensando en Ironman")
        else:
            print("Estas pensando en Captain Marvel")
    else:
        vof = input("Lleva mascara? (Si o No)\n")
        if vof == "Si" or vof == "si":
            print("Estas Pensando en Ronan Accuser")
        else:
            print("Estas pensando en Vision")
else:
    vof = input("Es Humano? (Si o No)\n")
    if vof == "Si" or vof == "si":
        vof = input("Lleva mascara? (Si o No)\n")
        if vof == "Si" or vof == "si":
            print("Estas Pensando en Spiderman")
        else:
            print("Estas pensando en Hulk")
    else:
        vof = input("Lleva mascara? (Si o No)\n")
        if vof == "Si" or vof == "si":
            print("Estas Pensando en Black Bolt")
        else:
            print("Estas pensando en Thanos")