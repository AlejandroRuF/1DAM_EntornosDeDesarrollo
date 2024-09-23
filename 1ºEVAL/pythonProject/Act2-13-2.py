def media(lista):
    largo=len(lista)
    sumalista=0
    for i in lista:
        sumalista += i
    return sumalista/largo

lista=[]
while True:
    entrada=int(input("Introduce numeros para ponerlos en una funcion y calcular la media cuando pongas 0 el programa calculara la media (0 no incluido)\n"))
    if entrada!=0:
        lista.append(entrada)
    else:
        break
print(f"La media de {lista} es {media(lista)}")