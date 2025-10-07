from ..core.player import Player
from ..core.board import Board
from ..core.game import Game
from ..core.dice import Dice
from ..core.checkers import Checkers, MovimientoInvalido

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

    dado = Dice()
    resultado = dado.roll()
    print(f"Dados: {resultado}")
    if dado.dobles():
        print("Dobles!")
        print(f"Dados: {dado.duplicar()}")

    try:
        origen = int(input("Desde qué punto quieres mover? ")) - 1
        dados_disponibles = dado.duplicar()
        posibles_destinos = Checkers.destinos_posibles(board, game.jugador_actual(), origen, dados_disponibles)
        if posibles_destinos:
            # Suma 1 para mostrar al usuario los puntos como 1-24
            print(f"Puedes mover desde {origen+1} a las casillas: {[d+1 for d in posibles_destinos]}")
        else:
            print(f"No hay movimientos posibles desde la casilla {origen+1} con los dados actuales.")
            return

        destino = int(input("A qué punto quieres mover? ")) - 1
        dado_usado = int(input("¿Con qué dado? "))  # O selecciona de los disponibles
        Checkers.mover(board, game.jugador_actual(), origen, destino, dado_usado)
        board.mostrar_tablero_cli()
    except MovimientoInvalido as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
