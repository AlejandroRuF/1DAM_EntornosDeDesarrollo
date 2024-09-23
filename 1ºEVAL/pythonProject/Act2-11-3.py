def media(num1,num2,num3,num4):
    return (num1+num2+num3+num4)/4

num1= int(input("Escribe el primer numero para calcular la media\n"))

num2= int(input("Escribe el segundo numero para calcular la media\n"))

num3= int(input("Escribe el tercer numero para calcular la media\n"))

num4= int(input("Escribe el cuarto numero para calcular la media\n"))

print(f"La media de {num1}, {num2}, {num3} y {num4} es {media(num1,num2,num3,num4)}")