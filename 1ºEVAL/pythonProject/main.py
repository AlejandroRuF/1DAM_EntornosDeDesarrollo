palabra="0123456789"
rev=""
print(palabra)
for i in palabra[::-1]:#palabra al reves
    rev+=i

print(rev)

print(palabra[2:])#pos 2 hasta final
print(palabra[:2])#hasta pos 2
print(palabra[::-2])#imprime del reves de 2 en 2
print(palabra[::2])#imprime de 2 en 2

lista=["A","B","C","D","Z","H","a","f","x","b"]

lista.sort()
print(lista)
lista=lista[::-1]
print(lista)

lista2=[5,1,3,2,8,7,9,4,6,0]

lista2.sort()
print(lista2)
lista2=lista2[::-1]
print(lista2)

for i in range(len(lista)):
    print(lista[i])

for i in lista2:
    print(i)