from ..core.player import Player
from ..core.board import Board

def main():
    print("Iniciando Backgammon")

    nombre1 = input("Nombre del Jugador 1: ")
    color1 = input("Color del Jugador 1 (Blanco/Negro): ").lower()
    while color1 not in ("blanco", "negro"):
        print("Color inválido. Debe ser 'Blanco' o 'Negro'")
        color1 = input("Color del Jugador 1 (Blanco/Negro): ").lower()
    nombre2 = input("Nombre del Jugador 2: ")
    color2 = ""
    if color1 == "negro":
        color2 = "blanco"
    else:
        color2 = "negro"

    p1 = Player(color1, nombre1, +1)
    p2 = Player(color2, nombre2, -1)

    print("Tablero:")
    board = Board(color1, color2)
    board.mostrar_tablero_cli()


if __name__ == '__main__':
    main()
