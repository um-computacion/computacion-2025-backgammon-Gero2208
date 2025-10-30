"""
Este módulo implementa una interfaz de línea de comandos (CLI) para jugar
al Backgammon.
"""
from core.player import Player
from core.game import Game
from core.exceptions import BackgammonException


def procesar_turno(game, entrada_usuario):
    """
    Procesa la entrada del usuario para un turno de juego.

    Parsea la entrada del usuario para determinar el comando y los argumentos,
    y luego llama al método de juego apropiado. Maneja los diferentes
    estados del juego, como tener fichas en la barra o estar en la fase de
    sacar fichas.

    Args:
        game (Game): La instancia actual del juego.
        entrada_usuario (str): La cadena de entrada del usuario.

    Returns:
        bool: True si la acción fue exitosa, False en caso contrario.
    """
    try:
        partes = entrada_usuario.split()
        comando = partes[0].lower()

        if game.jugador_tiene_fichas_en_barra():
            if comando == 'reingresar' and len(partes) == 2:
                dado = int(partes[1])
                game.reingresar_desde_barra(dado)
                return True
            else:
                print("Comando inválido. Debes usar: reingresar <dado>")
                return False

        elif game.todas_fichas_en_casa():
            if comando == 'sacar' and len(partes) == 3:
                origen = int(partes[1]) - 1
                dado = int(partes[2])
                game.sacar_ficha(origen, dado)
                return True
            elif comando == 'mover' and len(partes) == 3:
                origen = int(partes[1]) - 1
                destino = int(partes[2]) - 1
                game.mover_ficha(origen, destino)
                return True
            else:
                print("Comando inválido. Usa: sacar <origen> <dado> o mover <origen> <destino>")
                return False

        else:
            if comando == 'mover' and len(partes) == 3:
                origen = int(partes[1]) - 1
                destino = int(partes[2]) - 1
                game.mover_ficha(origen, destino)
                return True
            else:
                print("Comando inválido. Usa: mover <origen> <destino>")
                return False

    except (ValueError, IndexError):
        print("Entrada inválida. Asegúrate de que los números son correctos.")
        return False
    except BackgammonException as e:
        print(f"Error: {e}")
        return False


def main():
    """
    Función principal para ejecutar el juego de Backgammon en la línea de comandos.

    Inicializa el juego, gestiona la configuración de los jugadores, decide quién
    comienza, y luego entra en un bucle principal que procesa los turnos de los
    jugadores hasta que uno de ellos gana la partida.
    """
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
        print(board.mostrar_tablero_cli())
        print(f"Dados restantes: {game.movimientos_restantes}")

        while game.movimientos_restantes:
            if not game.hay_movimientos_posibles():
                print("No tienes movimientos posibles con los dados restantes.")
                break

            # Generar texto de ayuda dinámico
            prompt = "Jugada (ej: mover <origen> <destino>): "
            if game.jugador_tiene_fichas_en_barra():
                prompt = "Jugada (ej: reingresar <dado>): "
            elif game.todas_fichas_en_casa():
                prompt = "Jugada (ej: mover <origen> <destino> o sacar <origen> <dado>): "

            entrada = input(prompt)
            procesar_turno(game, entrada)

            if game.movimientos_restantes:
                print(board.mostrar_tablero_cli())
                print(f"Dados restantes: {game.movimientos_restantes}")

        ganador_actual = game.ganador()
        if ganador_actual:
            print(f"¡Felicidades, {ganador_actual.nombre()}! Has ganado la partida.")
            print(board.mostrar_tablero_cli())
            break

        game.cambiar_turno()


if __name__ == '__main__':
    main()
