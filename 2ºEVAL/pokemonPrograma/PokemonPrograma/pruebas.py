import time

print("Tu Pokemon esta evoluvionando")
for i in range(40):
    print(".", end="")
    time.sleep(8 / 60)
print(f"\nFelicidades tu aa se ha convertido en bb")

class MiClase:
    # Atributo de clase para contar instancias
    contador_instancias = 0

    def __init__(self):
        # Incrementar el contador y asignar un ID único a cada instancia
        MiClase.contador_instancias += 1
        self.id = MiClase.contador_instancias

    # Método de clase para obtener el número total de instancias
    @staticmethod
    def obtener_contador_instancias():
        return MiClase.contador_instancias

    # Método para obtener el ID de la instancia actual
    def obtener_id(self):
        return self.id

# Crear instancias de la clase
instancia1 = MiClase()
instancia2 = MiClase()
instancia3 = MiClase()

# Obtener el número total de instancias
print("Número total de instancias:", MiClase.obtener_contador_instancias())

# Obtener el ID de cada instancia
print("ID de instancia1:", instancia1.obtener_id())
print("ID de instancia2:", instancia2.obtener_id())
print("ID de instancia3:", instancia3.obtener_id())