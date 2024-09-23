palabra="palabra9"
reves=""

for i in range(0,len(palabra),1):
    reves+=palabra[i]
    print(f"{i} {palabra[i]}")


pos=0
for i in palabra:
    reves+=i
    print(f"{i} {pos}")
    pos+=1


for i in range(0, len(palabra),1):
    if palabra[i] =="p":
        print("p")
    if palabra[i]== "9":
        print("numero")
    if palabra[i]=="a" and i>3:
        break

for i in range(len(palabra)):
    reves += palabra[i]
    print(reves)