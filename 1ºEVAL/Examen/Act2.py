num = int(input("Dime un numero y te enseñare un patron\n"))
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
pos = 0
for i in range(0, num + 1, 1):
    print(f"{numeros[pos]} ", end="")
    if pos == len(numeros) - 1:
        pos = -1
    pos += 1
print()
print("0", end="")
pos = 1
for i in range(1, num + 1, 1):
    print(f"{numeros[pos]} ", end="")
    if pos == len(numeros) - 1:
        pos = -1
    pos += 1
print()

dibujo = "***¿¿??"
pos = 0

for i in range(0, (num*2) + 1, 1):
    print(dibujo[pos], end="")
    if pos == len(dibujo) - 1:
        pos = 0
    pos += 1
