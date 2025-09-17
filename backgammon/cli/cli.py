from ..core.player import Player
from ..core.board import Board

def main():
    print("Iniciando Backgammon")

    nombre1 = input("Nombre del Jugador 1: ")
    color = input("Color del Jugador 1 (Blanco/Negro): ").lower()
    while color not in ("blanco", "negro"):
        print("Color inválido. Debe ser 'Blanco' o 'Negro'")
        color = input("Color del Jugador 1 (Blanco/Negro): ").lower()
    nombre2 = input("Nombre del Jugador 2: ")

    p1 = Player(color, nombre1, +1)
    p2 = Player("", nombre2, -1)
    p2.asignar_color_opuesto(color)

    print("Tablero:")
    board = Board()
    board.setup()


if __name__ == '__main__':
    main()
