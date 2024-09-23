num = int(input("Introduce numeros para sumar cuando pongas 0 el programa acabara\n"))
contador = 0
resultado = 0
while num != 0:

    if contador == 0:
        resultado = num
    else:
        resultado = resultado + num
    if num != 0:
        num = int(input("Introduce otro numero para sumar cuando pongas 0 el programa acabara\n"))
    contador = contador + 1

print(f"El resultado es {resultado}")
