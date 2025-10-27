from core.player import Player
from core.game import Game
from core.exceptions import BackgammonException

def main():
    print("Iniciando Backgammon")

    nombre1 = input("Nombre del Jugador 1: ")
    color1 = input("Color del Jugador 1 (Blanco/Negro): ").lower()
    while color1 not in ("blanco", "negro"):
        print("Color inválido. Debe ser 'Blanco' o 'Negro'")
        color1 = input("Color del Jugador 1 (Blanco/Negro): ").lower()
    
    nombre2 = input("Nombre del Jugador 2: ")
    color2 = "blanco" if color1 == "negro" else "negro"

    p1 = Player(color1, nombre1, +1)
    p2 = Player(color2, nombre2, -1)

    game = Game(p1, p2)

    ganador, tiro_p1, tiro_p2 = game.decidir_iniciador()
    print(f"{ganador.nombre()} comienza (tiradas: {tiro_p1} vs {tiro_p2})")

    while not game.ganador():
        jugador_actual = game.jugador_actual()
        print(f"Turno de: {jugador_actual.nombre()} ({jugador_actual.color()})")

        game.lanzar_dados()
        
        board = game.get_board_status()
        board.mostrar_tablero_cli()
        print(f"Dados restantes: {game.movimientos_restantes}")

        while game.movimientos_restantes:
            if not game.hay_movimientos_posibles():
                print("No tienes movimientos posibles con los dados restantes.")
                break

            try:
                if game.jugador_tiene_fichas_en_barra():
                    entradas = game.posibles_entradas_desde_barra()
                    print("Debes reingresar una ficha desde la barra.")
                    print(f"Entradas posibles: {[(d, dest + 1) for d, dest in entradas]}")
                    dado_elegido = int(input("¿Qué dado quieres usar para reingresar? "))
                    game.reingresar_desde_barra(dado_elegido)

                elif game.todas_fichas_en_casa():
                    accion = input("¿Quieres mover (m) o sacar (s) una ficha? ").lower()
                    if accion == 's':
                        origen = int(input("¿Desde qué punto quieres sacar la ficha? ")) - 1
                        dado_a_usar = int(input(f"¿Qué dado quieres usar para sacar desde {origen + 1}? Tienes {game.movimientos_restantes}: "))
                        game.sacar_ficha(origen, dado_a_usar)
                    elif accion == 'm':
                        origen = int(input("¿Desde qué punto quieres mover? ")) - 1
                        destinos = game.validar_origen_y_obtener_destinos(origen)
                        print(f"Puedes mover desde {origen + 1} a las casillas: {[d + 1 for d in destinos]}")
                        destino = int(input("¿A qué punto quieres mover? ")) - 1
                        game.mover_ficha(origen, destino)
                    else:
                        print("Acción no válida. Por favor, elige 'm' para mover o 's' para sacar.")
                        continue
                
                else:
                    origen = int(input("¿Desde qué punto quieres mover? ")) - 1
                    destinos = game.validar_origen_y_obtener_destinos(origen)
                    print(f"Puedes mover desde {origen + 1} a las casillas: {[d + 1 for d in destinos]}")
                    destino = int(input("¿A qué punto quieres mover? ")) - 1
                    game.mover_ficha(origen, destino)

                if game.movimientos_restantes:
                    board.mostrar_tablero_cli()
                    print(f"Dados restantes: {game.movimientos_restantes}")

            except BackgammonException as e:
                print(f"Error: {e}")
            except ValueError:
                print("Entrada inválida.")
            except Exception as e:
                print(f"Error inesperado: {e}")

        ganador_actual = game.ganador()
        if ganador_actual:
            print(f"¡Felicidades, {ganador_actual.nombre()}! Has ganado la partida.")
            board.mostrar_tablero_cli()
            break
        
        game.cambiar_turno()

if __name__ == '__main__':
    main()
