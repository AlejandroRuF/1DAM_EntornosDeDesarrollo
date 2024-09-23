import math


def area_circle(radi):
    area=math.pi*(radi**2)
    return area

radi=int(input("Introduce el radio del circulo para calcular su area\n"))

print(f"El area del circulo es {area_circle(radi):.2f}")