from Pokemon import Pokemon


class Entrenador:
    __nombre: str
    __id: int
    __lista_pokemon = []
    __contador = 0

    def __init__(self, nombre):
        Entrenador.__contador += 1
        self.__id = Entrenador.__contador
        self.__nombre = None
        self.set_nombre(nombre)
        self.__lista_pokemon = []
        self.set_lista_pokemon()

    def get_id(self):
        return self.__id

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise Exception("El Nombre del entrenador debe ser una cadena de caracteres")

    def get_nombre(self):
        return self.__nombre

    def set_lista_pokemon(self):
        if len(self.__lista_pokemon) == 0:
            self.__lista_pokemon.append(Pokemon("Pichu", "Electrico", 1, 5, "Picachu", 10, "Raichu", self.get_nombre()))
        else:
            raise Exception("Este entrenador ya existe")

    def get_lista_pokemon(self):
        return self.__lista_pokemon

    def anyadir_pokemon(self, pokemon: Pokemon):
        if isinstance(pokemon, Pokemon):
            if len(self.__lista_pokemon) < 6:
                self.__lista_pokemon.append(pokemon)
            else:
                raise Exception("Tu equipo ya esta lleno")
        else:
            raise Exception("El pokemon añadido de ser un objeto tipo Pokemon")

    def quitar_Pokemon(self, numPokemon):

        if isinstance(numPokemon, int) and 0 <= numPokemon <= 6 and len(self.__lista_pokemon) > 1:
            if len(self.__lista_pokemon) >= numPokemon:
                self.__lista_pokemon.pop(numPokemon)
            else:
                raise Exception("No tienes ningun pokemon en esa posicion")
        else:
            raise Exception("Debes Elegir un numero entero entre el 1 y el 6 no puedes tener menos de 1 pokemon en tu"
                            " equipo")

    def mostrar_lista(self):
        contador = 1;
        for i in self.__lista_pokemon:
            print(f"{contador}: \n"
                  f"{i}\n")
            contador += 1

    def __str__(self):
        return (f"El entrenador {self.get_nombre()} con id {self.get_id()} tiene {len(self.__lista_pokemon)}"
                f" pokemons en su poder:\n")

    @staticmethod
    def set_contador():
        return Entrenador.__contador


if __name__ == "__main__":

    En = Entrenador("Alex")
    en1 = Entrenador("Emi")
    en2 = Entrenador("Arch")

    print(Entrenador.set_contador())

    print(en1.get_id())
    print(En.get_id())
    print(en2.get_id())

    print(En)

    print(en1)

    print(en2)

    en1.mostrar_lista()
    en1.anyadir_pokemon(Pokemon("Charmander", "Fuego", 15, 16, "Charmeleon", 45, "Charizard", en1.get_nombre()))
    en1.mostrar_lista()
    en1.get_lista_pokemon()[1].subirNivel(15)
    en1.mostrar_lista()
    en1.get_lista_pokemon()[1].subirNivel(15)
    en1.mostrar_lista()
    en1.quitar_Pokemon(0)
    en1.mostrar_lista()
