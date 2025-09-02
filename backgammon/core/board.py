class Board:
    def __init__(self):
        self.__triangulos__ = 24 # Estructura de 24 triangulos
        self.__bar__ = {"jugador1": [], "jugador2": []} # Zona especial del tablero donde van las fichas capturadas (una por cada jugador).
        self.__final__ = {"jugador1": [], "jugador2": []} # Zona especial del tablero donde se colocan las fichas que ya salieron (borne off).