print(f"Vamos a averiguar que tipo de triangulo tienes")
lado1 = int(input("Introduce el primer lado del triangulo\n"))
lado2 = int(input("Introduce el lado 2 del triangulo\n"))
lado3 = int(input("Introduce el tercer lado del triangulo\n"))

if lado1 == lado2 == lado3:
    print(f"Como los tres lados son iguales tienes un triangulo equilatero")

elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado3 == lado2 != lado1:
    print(f"Como solo tiene dos costados iguales es un triangulo isosceles")

else:
    print(f"Como ningun lado es igual es un triangulo escaleno")
