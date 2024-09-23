def taula_multiplicar(numero):
    print(f"\nTabla del {numero}")
    for i in range (0,11,1):
        print(f"{numero} X {i:02d} = {numero*i:02d}")


for i in range (1,6,1):
    taula_multiplicar(i)
