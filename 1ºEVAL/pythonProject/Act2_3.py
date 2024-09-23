nom = input("Escribe tu nombre por favor :\n")
email = input("Escribe tu email :\n")
fechanacimiento = input("Escribe tu fecha de nacimiento siguiendo el formato dd/mm/aaaa :\n")

print("Hola "+nom + " naciste el "+fechanacimiento+" y tu email es " + email)

print(f"Hola {nom} naciste el {fechanacimiento} y tu email es {email}")

print("Hola {} naciste el {} y tu email es {}".format(nom, fechanacimiento, email))
