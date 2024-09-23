num1=int(input("Escribe un numero para saber si tabla de multiplicar\n"))

print(f"La tabla del {num1} es: ")
for i in range(0,11,1):
    print(f"{num1}x{i}={num1*i} ")