numero=int(input("Dame un numero por favor\n"))

for i in range(1,(numero+1),1):
    print("*"*i)
for i in range(1,(numero+1),1):
    print("*"*(numero-i))