import juego

# Creo el objeto juego

juego1 = juego.Juego("Pepe", # Nombre jugador 1
                     "Paco", # Nombre jugador 2
                     6, # Caras dado 1
                     8, # Caras dado 2
                     12, # Caras dado 3
                     10, # Lanzamientos
                     "S")  # Muestro resultados intermedios

# Hago los lanzamientos


# Muestro el resultado del juego
juego1.mostrar()
while True:
    juego1 = juego.Juego("Pepe", # Nombre jugador 1
                         "Paco", # Nombre jugador 2
                         4, # Caras dado 1
                         4, # Caras dado 2
                         4, # Caras dado 3
                         10, # Lanzamientos
                         "s")  # Muestro resultados intermedios
    juego1.lanzamiento()
    if juego1.resultados1 == juego1.resultados2:
        juego1.mostrar()
        break

while True:
    juego1 = juego.Juego("Pepe", # Nombre jugador 1
                         "Paco", # Nombre jugador 2
                         4, # Caras dado 1
                         4, # Caras dado 2
                         4, # Caras dado 3
                         10, # Lanzamientos
                         "s")  # Muestro resultados intermedios
    juego1.lanzamiento()
    if juego1.resultados1 > juego1.resultados2:
        juego1.mostrar()
        break

while True:
    juego1 = juego.Juego("Pepe", # Nombre jugador 1
                         "Paco", # Nombre jugador 2
                         4, # Caras dado 1
                         4, # Caras dado 2
                         4, # Caras dado 3
                         10, # Lanzamientos
                         "s")  # Muestro resultados intermedios
    juego1.lanzamiento()
    if juego1.resultados1 < juego1.resultados2:
        juego1.mostrar()
        break
try:
    # Creo el objeto juego
    juego1 = juego.Juego("Pepe", # Nombre jugador 1
                         "Paco", # Nombre jugador 2
                         4, # Caras dado 1
                         8, # Caras dado 2
                         1, # Caras dado 3
                         5, # Lanzamientos
                         "s")  # Muestro resultados intermedios

except Exception as e:
    print(e)

try:
    # Creo el objeto juego
    juego1 = juego.Juego("123456789012345678dfyhrsdtgsdtfgsdfggsdfgsdfgsdfg90", # Nombre jugador 1
                         "Paco", # Nombre jugador 2
                         1, # Caras dado 1
                         8, # Caras dado 2
                         12, # Caras dado 3
                         2, # Lanzamientos
                         "s")  # Muestro resultados intermedios

except Exception:
    print("ok")

try:
    # Creo el objeto juego
    juego1 = juego.Juego("Pepe", # Nombre jugador 1
                         "12345678901dfgsdfgsdfgsdfgsdfgsdfg234567890", # Nombre jugador 2
                         1, # Caras dado 1
                         8, # Caras dado 2
                         12, # Caras dado 3
                         2, # Lanzamientos
                         "s")  # Muestro resultados intermedios

except Exception:
    print("ok")

try:
    # Creo el objeto juego
    juego1 = juego.Juego("Pepe", # Nombre jugador 1
                         "Paco", # Nombre jugador 2
                         1, # Caras dado 1
                         8, # Caras dado 2
                         12, # Caras dado 3
                         0, # Lanzamientos
                         "s")  # Muestro resultados intermedios

except Exception:
    print("ok")