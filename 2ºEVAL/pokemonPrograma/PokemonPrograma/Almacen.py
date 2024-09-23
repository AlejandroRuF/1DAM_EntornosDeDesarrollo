from Entrenador import Entrenador
from Pokemon import Pokemon


class Almacen:
    __lista_pokemon_guardadods = []
    __entrenador: str

    def set_entrenador(self, entrenador: Entrenador):
        if isinstance(entrenador, Entrenador):
            self.__entrenador = entrenador
        else:
            raise Exception("El entrenador debe ser un objeto de tipo Entrenador")

    def get_Entrenador(self):
        return self.__entrenador

    def set_lista_pokemon_guardados(self, pokemon: Pokemon):
        if isinstance(pokemon, Pokemon):
            self.__lista_pokemon_guardadods.append(pokemon)
        else:
            raise Exception("En la caja solo puedes guardar Pokemons")

    def get_lista_pokemon_guardados(self):
        return self.__lista_pokemon_guardadods

    def mostrar_Alacen(self):
        print(f"\nPokemon guardados en la caja:\n")
        for i in range(len(self.__lista_pokemon_guardadods)):
            print(f"{i + 1}:\n"
                  f"{self.__lista_pokemon_guardadods[i]}")

    def mostrar_pokemonEntrenador(self):
        print(f"\nPokemon que lleva el entrenador:\n")
        for i in range(len(self.__entrenador.get_lista_pokemon())):
            print(f"{i + 1}:\n"
                  f"{self.__entrenador.get_lista_pokemon()[i]}")

    def sacar_pokemon(self, num):
        num = (num - 1)
        if isinstance(num, int) and 0 <= num < len(self.__lista_pokemon_guardadods):
            if len(self.__entrenador.get_lista_pokemon()) < 6:
                self.__entrenador.anyadir_pokemon(self.__lista_pokemon_guardadods[num])
                self.__lista_pokemon_guardadods.pop(num)
                self.mostrar_Alacen()
                self.mostrar_pokemonEntrenador()
            else:
                raise Exception("No tienes hueco en tu equipo para mas pokemons")
        else:
            raise Exception(f"Debes introducir un numero entero entre 1 y {len(self.__lista_pokemon_guardadods)}")


    def dejar_pokemon(self, num):
        num = (num - 1)
        if isinstance(num, int) and 0 <= num < len(self.__entrenador.get_lista_pokemon()):
            if len(self.__entrenador.get_lista_pokemon()) > 1:
                self.__lista_pokemon_guardadods.append(self.__entrenador.get_lista_pokemon()[num])
                self.__entrenador.quitar_Pokemon(num)
                self.mostrar_Alacen()
                self.mostrar_pokemonEntrenador()
            else:
                raise Exception("No puedes quedarte sin pokemon")

    def capturar_pokemon(self, pokemon:Pokemon):
        if isinstance(pokemon, Pokemon):
            self.__lista_pokemon_guardadods.append(pokemon)
        else:
            raise Exception("Solo puedes capturar Pokemons")


    def __init__(self, entrenador: Entrenador, lista_pokemon: list):
        self.__entrenador = None
        self.set_entrenador(entrenador)
        self.__lista_pokemon_guardadods = []
        for i in lista_pokemon:
            self.set_lista_pokemon_guardados(i)


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

    list_pokemon = [Pokemon("Charmander", "Fuego", 15, 16, "Charmeleon", 45, "Charizard", en1.get_nombre()),
                    Pokemon("Bulbasaur", "PLANTA", 18, 32, "Ivysaur", 50, "Venusaur", en1.get_nombre()),
                    Pokemon("Squirtle", "AGUA", 15, 35, "Wartortle", 45, "Blastoise", en1.get_nombre()),
                    Pokemon("Jigglypuff", "AGUA", 20, 30, "Wigglytuff", 40, "Wigglytuff Gigantamax", en1.get_nombre()),
                    Pokemon("Eevee", "FUEGO", 22, 35, "Vaporeon", 50, "Jolteon", en1.get_nombre()),
                    Pokemon("Gastly", "DRAGON", 25, 36, "Haunter", 45, "Gengar", en1.get_nombre())]

    al1 = Almacen(en1, list_pokemon)
    al1.mostrar_Alacen()
    al1.mostrar_pokemonEntrenador()
    al1.sacar_pokemon(1)
    al1.dejar_pokemon(2)
    p1 = Pokemon("Jigglypuff", "AGUA", 20, 30, "Wigglytuff", 40, "Wigglytuff Gigantamax", en1.get_nombre())
    al1.capturar_pokemon(p1)
    al1.mostrar_Alacen()
    al1.mostrar_pokemonEntrenador()
    al1.capturar_pokemon(Pokemon("Squirtle", "AGUA", 15, 35, "Wartortle", 45, "Blastoise", en1.get_nombre()))
    al1.mostrar_Alacen()
    al1.mostrar_pokemonEntrenador()
    h1 = "hola"
    