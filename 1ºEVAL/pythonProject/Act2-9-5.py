num1 = int(input("Escribe el numero de filas\n"))
num2 = int(input("Escribe el numero de columnas\n"))

for i in range(1, (num1+1), 1):

    for j in range(1, num2+1, 1):
        for x in range(1, num1 + 1, 1):
            print("*",end="")
        print(" ",end="")
    print("")
