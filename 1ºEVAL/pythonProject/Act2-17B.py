import random

def lanzamiento(caras):

    return int(random.randint(1, caras))


veces = int(input(f"Cuantas veces quieres tirar el dado\n"))

lados=int(input("Cuantas Caras tiene el dado\n"))

dados = []

for i in range(veces):
    dados.append(lanzamiento(lados))


cara=0
for i in range(1, lados+1,1):
    for x in dados:
        if i == x:
            cara += 1
    print(f"{i} --> {cara} veces({round((cara/veces*100),5)}) \n")
    cara=0

