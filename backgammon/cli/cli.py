from ..core.player import Player
from ..core.board import Board
from ..core.game import Game

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

    board = Board()
    board.setup(color1, color2)

    game = Game(p1, p2)

    print("Tablero:")
    board.mostrar_tablero_cli()

    print(f"Turno de: {game.jugador_actual().nombre()} ({game.jugador_actual().color()})")


if __name__ == '__main__':
    main()
