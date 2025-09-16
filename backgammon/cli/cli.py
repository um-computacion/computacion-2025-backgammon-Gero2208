from core.board import Board

def main():
    print("Iniciando Backgammon")

    # Crear tablero y jugadores
    board = Board()
    board.setup()

    # Crear dos jugadores (id, color, direction)
    # Convención: 'jugador1' mueve +1, 'jugador2' mueve -1 (ajusta según tu tablero)
    p1 = Player("jugador1", "blanco", +1)
    p2 = Player("jugador2", "negro", -1)


if __name__ == '__main__':
    main()
