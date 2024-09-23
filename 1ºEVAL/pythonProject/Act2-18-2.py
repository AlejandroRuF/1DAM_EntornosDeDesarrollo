def listasimpares(lista1):
    listaimp = []

    for i in lista1:
        repetido = False
        if i % 2 != 0:
            if i in listaimp:
                repetido = True
            if not repetido:
                listaimp.append(int(i))

    return listaimp


lista = []
pos = 1
print(f"Vamos a introducir 1 listas cuando acabes diremos que numeros son imprares")
print(f"Introduce los valores de la lista introduce 0 cuando acabes")
while True:

    temp = int(input(f"Lista valor {pos}: "))
    if temp != 0:
        lista.append(temp)
    else:
        break
    pos += 1

print(f"Los valores impres en la lista son:\n"
      f"{listasimpares(lista)}")
