def listascomun(lista1, lista2):
    listacomun = []

    for i in lista1:
        if i not in lista2:
            repetido = False
            for j in listacomun:
                if i in listacomun:
                    repetido = True
            if not repetido:
                listacomun.append(int(i))

    return listacomun


plista = []
slista = []
pos = 1
print(f"Vamos a introducir 2 listas cuando acabes se compararan que numeros tienen en comun y los diremos")
print(f"Introduce los valores de la lista 1 introduce 0 cuando acabes")
while True:

    temp = int(input(f"Lista 1 valor {pos}: "))
    if temp != 0:
        plista.append(temp)
    else:
        break
    pos += 1

print(f"Introduce los valores de la lista 2 introduce 0 cuando acabes")
pos = 1
while True:

    temp = int(input(f"Lista 2 valor {pos}: "))
    if temp != 0:
        slista.append(temp)
    else:
        break
    pos += 1

print(f"Valores:\n"
      f"Lista 1 ---> {plista}\n"
      f"Lista 2 ---> {slista}\n"
      f"Valores en comun:\n"
      f"{listascomun(plista, slista)}")
