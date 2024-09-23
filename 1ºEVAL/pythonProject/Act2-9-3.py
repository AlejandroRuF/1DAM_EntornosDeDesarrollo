numero=int(input("Dame un numero por favor\n"))

for i in range(1,(numero+1),1):
    print(" "*(numero-i)+"*" * (i-1)+"*"*i)
for i in range(numero, 1, -1):
    print(" "*(numero-i+1)+"*" * (i-2)+"*"*(i-1))
