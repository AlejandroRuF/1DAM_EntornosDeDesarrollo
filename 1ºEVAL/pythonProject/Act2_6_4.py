ram = int(input("Cuanta RAM tiene tu ordenador\n"))

if ram < 4:
    print(f"Poca RAM")
if 4 <= ram < 8:
    print(f"Vas justet de RAM")
if 8 <= ram < 16:
    print(f"No esta mal")
if ram >= 16:
    print(f"Equipazoo!!")
