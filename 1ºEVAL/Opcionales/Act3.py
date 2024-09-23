import random


def l_Moneda(lanzamiento):
    resultado = []
    for j in range(lanzamiento):
        moneda = random.randint(1, 2)
        resultado.append(moneda)
    return resultado


def contador(lista):
    contador_Cruz = 0
    cont_def = 0
    for j in range(len(lista)):
        if j == 0 and lista[j] == 1:
            contador_Cruz += 1
        if j != 0 and lista[j] == 1 and lista[j] != lista[j - 1]:
            contador_Cruz = 1
        elif j != 0 and lista[j] == 1 and lista[j] == lista[j - 1]:
            contador_Cruz += 1
        if cont_def < contador_Cruz:
            cont_def = contador_Cruz
    return cont_def


veces = 2
while veces <= 2:
    veces = int(input("Introduce las veces que quieres lanzar la moneda\n"))
    if veces < 2:
        print("Debes lanzar la moneda minimo 2 veces")
monedas = l_Moneda(veces)
for i in monedas:
    if i == 1:
        print("\u2716", end="")
    else:
        print("\u26AA", end="")
print()

print(f"Cruz ha salido {contador(monedas)} veces seguidas")
