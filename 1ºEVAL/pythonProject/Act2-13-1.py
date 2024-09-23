def media(lista):
    largo=len(lista)
    sumalista=0
    for i in lista:
        sumalista += i
    return sumalista/largo

lista1=[2,4,8]
lista2=[9,10,2,6,8,8]
lista3=[100,102,200,500,600,700,900,1000]

print(f"La media de {lista1} es : {round(media(lista1),2)}")
print(f"La media de {lista2} es : {round(media(lista2),2)}")
print(f"La media de {lista3} es : {round(media(lista3),2)}")
