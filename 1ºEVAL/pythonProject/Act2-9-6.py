num1=int(input("Escribe un numero\n"))

for i in range (1,num1+1,1):
    print("   *  ",end="")
print("")
for i in range (1,((num1*2)+1),1):
    print(" * ",end="")
print("")
for i in range (1,num1+2,1):
    print("*     ",end="")

print("\n\nSolución 2:")

cadena=""
for i in range (num1):
    cadena=cadena +"  * "
print(cadena)

cadena=""
for i in range (num1):
    cadena=cadena +" * *"
print(cadena)

cadena=""
for i in range (num1+1):
    cadena=cadena +"*   "
print(cadena)
