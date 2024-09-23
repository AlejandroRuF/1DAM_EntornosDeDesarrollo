class Persona:
    __contador = 0
    __nom = ""
    __edad = 0

    def __init__(self, nom, edad):
        Persona.__contador += 1
        self.__nom = nom
        self.set_edad(edad)
        self.__contador = Persona.__contador

    def get_nombre(self):
        return self.__nom

    def get_edad(self):
        return self.__edad

    def get_id(self):
        return self.__contador

    def __str__(self):
        nombre_objeto = [nombre for nombre, obj in globals().items() if obj is self][0]
        return f"{nombre_objeto}: Nombre: {self.get_nombre()} edad: {self.get_edad()} ID: {self.get_id()}"

    def set_edad(self, edad):
        if edad < 0:
            raise Exception("La edad debe ser positiva")
        else:
            self.__edad = edad

    def set_nom(self, nom):
        self.__nom = nom


persona1 = Persona("Alex",30)
print(persona1)
persona2 = Persona("Emi", 28)
print(persona2)
persona3 = Persona("Logan",18)
print(persona3)