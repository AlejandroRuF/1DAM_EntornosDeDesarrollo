num1 = int(input("Pon el primer numero a dividir\n"))
num2 = int(input("Pon el segundo numero a dividir\n"))

if num2 == 0:
    print("El divisor no puede ser 0")
else:
    resultado = num1/num2
    print(f"El resultado de la division sera {resultado}")
