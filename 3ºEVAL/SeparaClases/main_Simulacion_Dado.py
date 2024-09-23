from Dado import Dado
from Simulacion import Simulacion

if __name__ == "__main__":
    print("Bienvenidos a este juego de azar")

    nlanzamientos = int(input("Cuantas veces quieres lanzar el dado\n"))
    cara = int(input("Cuantas caras quieres que tenga tu dado\n"))
    dados = Dado(cara)
    lanzamientos = Simulacion(dados, nlanzamientos)
    lanzamientos.generar()
    lanzamientos.mostrar_resultados()
