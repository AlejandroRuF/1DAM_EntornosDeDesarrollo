num = int(input("Introduce numeros para sumar cuando pongas 0 el programa acabara, se mostrara la suma y se calculara la media\n"))
contador = 0
resultado = 0
negtivos = 0
positivos = 0
cero = 0

while num != 0:

    if contador == 0:
        resultado = num
    else:
        resultado = resultado + num
    if num != 0:
        num = int(input("Introduce otro numero para sumar cuando pongas 0 el programa acabara\n"))

    if num>0:
        positivos=positivos+1
    if num<0:
        negtivos=negtivos+1
    if num==0:
        cero=cero+1
    contador = contador + 1

media=resultado/(contador)
print(f"El resultado de la suma es {resultado} y la media de los numeros sumados es {media}")

if positivos>0:
    #if positivos!=1:
    print(f"Has introducido {positivos} veces numeros positivos")
    #else:
    #print(f"Has introducido {positivos} vez numeros positivos")

if negtivos>0:
    #if negtivos != 1:
    print(f"Has introducido {negtivos} veces numeros negativos")
    #else:
    #print(f"Has introducido {negtivos} vez numeros negativos")

if positivos>0:
    print(f"Has introducido {cero} vez el numero cero")