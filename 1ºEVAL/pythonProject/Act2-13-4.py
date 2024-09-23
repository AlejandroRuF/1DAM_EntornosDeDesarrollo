def media(lista):
    largo=len(lista)
    sumalista=0
    for i in lista:
        sumalista += i
    return sumalista/largo

def mayor(lista):

    num_Mayor=lista[0]

    for i in lista:
        if i>num_Mayor:
            num_Mayor=i
    return num_Mayor

def menor(lista):

    num_Menor=lista[0]

    for i in lista:
        if i<num_Menor:
            num_Menor=i
    return num_Menor

lista=[]
while True:
    entrada=int(input("Introduce numeros para ponerlos en una funcion y calcular la media cuando pongas 0 el programa calculara la media (0 no incluido)\n"))
    if entrada!=0:
        lista.append(entrada)
    else:
        break
print(f"La media de {lista} es {media(lista)}")
print(f"El numero mayor de la lista es {mayor(lista)}")
print(f"El numero mayor de la lista es {menor(lista)}")