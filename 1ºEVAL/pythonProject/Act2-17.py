import random


def lanzamiento():
    return int(random.randint(1, 6))


veces = int(input(f"Cuantas veces quieres tirar el dado\n"))

dados = []


for i in range(veces):
    dados.append(lanzamiento())

uno = int(0)
dos = int(0)
tres = int(0)
cuatro = int(0)
cinco = int(0)
seis = int(0)

for i in dados:
    if i == 1:
        uno += 1
    elif i == 2:
        dos += 1
    elif i == 3:
        tres += 1
    elif i == 4:
        cuatro += 1
    elif i == 5:
        cinco += 1
    elif i == 6:
        seis += 1

porc1=uno/veces*100
porc2=dos/veces*100
porc3=tres/veces*100
porc4=cuatro/veces*100
porc5=cinco/veces*100
porc6=seis/veces*100

print(f"1 --> {uno}({porc1}) \n2 --> {dos}({porc2}) \n3 --> {tres}({porc3}) \n4 --> {cuatro}({porc4}) "
      f"\n5 --> {cinco}({porc5}) \n6 --> {seis}({porc6})")
