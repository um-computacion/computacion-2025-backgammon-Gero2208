from core.player import Player
from core.board import Board
from core.game import Game
from core.dice import Dice
from core.checkers import Checkers, MovimientoInvalido

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
            # Si el jugador tiene fichas en la barra, obligar a reingresar primero
            color_actual = game.jugador_actual().color()
            if board.get_bar().get(color_actual):
                # calcula entradas posibles con los dados restantes
                entradas = []
                for d in movimientos_restantes:
                    dest = Checkers.puede_reingresar(board, game.jugador_actual(), d)
                    if dest is not None:
                        entradas.append((d, dest))
                if not entradas:
                    print("Tienes fichas en la barra pero no puedes reingresar con los dados restantes.")
                    break  # termina el turno
                # mostrar opciones simples: dado -> punto destino (usuario ve puntos 1..24)
                print("Debes reingresar una ficha desde la barra.")
                print(f"Entradas posibles: {[ (d, dest+1) for d, dest in entradas ]}")
                try:
                    dado_elegido = int(input("Qué dado quieres usar para reingresar? "))
                except ValueError:
                    print("Entrada inválida.")
                    continue
                if dado_elegido not in movimientos_restantes:
                    print("No tienes ese dado disponible.")
                    continue
                try:
                    Checkers.reingresar_desde_bar(board, game.jugador_actual(), dado_elegido)
                    movimientos_restantes.remove(dado_elegido)
                    # mostrar tablero solo si quedan movimientos por hacer
                    if movimientos_restantes:
                        board.mostrar_tablero_cli()
                        print(f"Dados restantes: {movimientos_restantes}")
                    continue
                except MovimientoInvalido as e:
                    print(f"Error: {e}")
                    continue
            # Bear off
            if Checkers.todas_en_inicio(board, game.jugador_actual()):
                print("Tus fichas estan en casa, puedes sacarlas del tablero")
                accion = input("Quieres mover (m) o sacar (s) una ficha? ").lower()
                if accion == 's':
                    try:
                        origen = int(input("Desde qué punto quieres sacar la ficha? ")) - 1
                        dado_str = input(f"Qué dado quieres usar para sacar desde {origen+1}? Tienes {movimientos_restantes}: ")
                        dado = int(dado_str)
                        if dado not in movimientos_restantes:
                            print("No tienes ese dado.")
                            continue
                        Checkers.bear_off(board, game.jugador_actual(), origen, dado)
                        movimientos_restantes.remove(dado)
                        if movimientos_restantes:
                            board.mostrar_tablero_cli()
                            print(f"Dados restantes: {movimientos_restantes}")
                        continue
                    except MovimientoInvalido as e:
                        print(f"Error: {e}")
                        continue
                    except ValueError:
                        print("Entrada inválida.")
                        continue
                elif accion != 'm':
                    print("Acción no válida. Por favor, elige 'm' para mover o 's' para sacar.")
                    continue
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

        ganador_actual = game.ganador(board)
        if ganador_actual:
            print(f"Felicidades, {ganador_actual.nombre()}! Has ganado la partida.")
            board.mostrar_tablero_cli()
            break
        game.cambiar_turno()
if __name__ == '__main__':
    main()
