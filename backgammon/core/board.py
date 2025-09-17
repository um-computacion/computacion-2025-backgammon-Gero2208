class Board:
    """
    Representación simple del tablero de Backgammon.

    El tablero se modela como una lista de 24 puntos (índices 0 a 23), donde cada punto es una lista de fichas.
    Cada ficha se representa por el identificador del jugador (por ejemplo: 'jugador1' o 'jugador2').
    Además, existen dos zonas especiales:
    - __bar__: fichas capturadas que deben volver a entrar al tablero.
    - __final__ (borne-off): fichas que ya han salido del tablero.

    Esta clase proporciona los métodos mínimos para inicializar el tablero y gestionar el estado básico
    necesario para la lógica y los tests del juego.
    """
    def __init__(self):
        self.__points__ = [[] for _ in range(24)]
        self.__bar__ = {"jugador1": [], "jugador2": []}
        self.__final__ = {"jugador1": [], "jugador2": []}

    def setup(self):
        """
        Coloca las fichas en la disposición inicial estándar de Backgammon.

        Limpia el tablero y posiciona las fichas de ambos jugadores según la convención:
        - 'jugador1': 2 fichas en el punto 0, 5 en el 11, 3 en el 16 y 5 en el 18.
        - 'jugador2': posiciones simétricas (2 en el 23, 5 en el 12, 3 en el 7 y 5 en el 5).

        Esta disposición corresponde a la posición inicial clásica del juego.
        """
        # Limpiar
        self.__points__ = [[] for _ in range(24)]
        self.__bar__ = {"jugador1": [], "jugador2": []}
        self.__final__ = {"jugador1": [], "jugador2": []}

        # Disposición (convención elegida):
        # jugador1
        self.__points__[0] = ["jugador1"] * 2
        self.__points__[11] = ["jugador1"] * 5
        self.__points__[16] = ["jugador1"] * 3
        self.__points__[18] = ["jugador1"] * 5

        # jugador2 - posiciones simétricas (24 - idx)
        self.__points__[23] = ["jugador2"] * 2
        self.__points__[12] = ["jugador2"] * 5
        self.__points__[7] = ["jugador2"] * 3
        self.__points__[5] = ["jugador2"] * 5