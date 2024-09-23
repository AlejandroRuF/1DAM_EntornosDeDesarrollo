num=int(input("Introduce un numero\n"))

print("Solución 1:")

print("*   "*(num+1))
print("* * "*(num)+"*")
print("*   "*(num+1))
print("\n")


print("Solución 2:")

#Línea 1
cadena=""
for i in range(num+1):
    cadena = cadena +"*   "
print(cadena)

cadena=""
for i in range(num+1):
    if i==(num):
        cadena = cadena + "* "
    else:
        cadena = cadena + "* * "
print(cadena)

cadena=""
for i in range(num+1):
    cadena = cadena +"*   "
print(cadena)




