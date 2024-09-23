def comprobar(cadena, letraf, numerof):
    contador = 0

    for i in range(0, len(cadena), 1):
        if cadena[i] == letraf:
            contador += 1
    if contador >= numerof:
        return True
    else:
        return False


palabra = ""

while True:
    print("Vamos a comprobar si sabes contar")
    palabra = input("Introduce una palabra cualquiera  si quieres salir del programa introduce 'Ruiz'\n")
    if palabra.lower() != "ruiz":
        letra = input("Introduce una letra\n")
        numero = int(input("Introduce el numero de veces minimo que crees que esta esa letra\n"))

        print(f"En {palabra} esta {numero} veces la letra {letra}? ----> {comprobar(palabra, letra, numero)}")
    else:
        break
