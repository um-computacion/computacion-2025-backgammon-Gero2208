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

    ganador, tiro_p1, tiro_p2 = game.decidir_iniciador()
    print(f"{ganador.nombre()} comienza (tiradas: {tiro_p1} vs {tiro_p2})")

    dado = Dice()
    
    while True:
        print(f"Turno de: {game.jugador_actual().nombre()} ({game.jugador_actual().color()})")
        resultado = dado.roll()
        dados_disponibles = dado.duplicar()
        movimientos_restantes = dados_disponibles.copy()

        board.mostrar_tablero_cli()
        print(f"Dados restantes: {movimientos_restantes}")

        while movimientos_restantes:
            try:
                origen = int(input("Desde qué punto quieres mover? ")) - 1
                destinos = Checkers.destinos_posibles(board, game.jugador_actual(), origen, movimientos_restantes)
                if not destinos:
                    print(f"No hay movimientos posibles desde la casilla {origen+1} con los dados actuales.")
                    if not Checkers.hay_movimientos_posibles(board, game.jugador_actual(), movimientos_restantes):
                        print("No quedan movimientos posibles con los dados restantes.")
                        break
                    continue

                print(f"Puedes mover desde {origen+1} a las casillas: {[d+1 for d in destinos]}")
                destino = int(input("A qué punto quieres mover? ")) - 1

                movimientos_restantes = Checkers.mover_y_consumir(
                    board, game.jugador_actual(), origen, destino, movimientos_restantes
                )

                # Mostrar tablero solo si quedan movimientos por hacer en este turno
                if movimientos_restantes:
                    board.mostrar_tablero_cli()
                    print(f"Dados restantes: {movimientos_restantes}")

            except MovimientoInvalido as e:
                print(f"Error: {e}")
            except ValueError:
                print("Entrada inválida.")
            except Exception as e:
                print(f"Error inesperado: {e}")

            if movimientos_restantes and not Checkers.hay_movimientos_posibles(board, game.jugador_actual(), movimientos_restantes):
                print("No quedan movimientos posibles con los dados restantes.")
                break

        game.cambiar_turno()

if __name__ == '__main__':
    main()
