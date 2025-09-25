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

    def setup(self, color1, color2):
        """
        Coloca las fichas en la disposición inicial estándar de Backgammon.

        color1: color del primer jugador ('blanco' o 'negro')
        color2: color del segundo jugador ('blanco' o 'negro')
        """
        self.__points__ = [[] for _ in range(24)]
        self.__bar__ = {color1: [], color2: []}
        self.__final__ = {color1: [], color2: []}

        # color1
        self.__points__[0] = [color1] * 2
        self.__points__[11] = [color1] * 5
        self.__points__[16] = [color1] * 3
        self.__points__[18] = [color1] * 5

        # color2 - posiciones simétricas
        self.__points__[23] = [color2] * 2
        self.__points__[12] = [color2] * 5
        self.__points__[7] = [color2] * 3
        self.__points__[5] = [color2] * 5

    def mostrar_tablero_cli(self):
        """
        Muestra el tablero de Backgammon en la consola de forma gráfica,
        sin numeración, solo triángulos y fichas por color.
        """
        simbolos = {"blanco": "⚪", "negro": "⚫", "jugador1": "A", "jugador2": "B"}

        print("  +---------------------+---------------------+")
        # Fila superior (puntos 12 a 23)
        fila_sup = "  |"
        for i in range(12, 24):
            punto = self.__points__[i]
            if punto:
                color = punto[0]
                ficha = simbolos.get(color, "?")
                cantidad = len(punto)
                if cantidad <= 5:
                    fila_sup += f"▲{ficha * cantidad: <2}"
                else:
                    fila_sup += f"▲{ficha}x{cantidad}"
            else:
                fila_sup += "▲  "
            if i == 17:
                fila_sup += "   |"
        fila_sup += "   |"
        print(fila_sup)
        print("  +---------------------+---------------------+")

        # Fila inferior (puntos 11 a 0)
        fila_inf = "  |"
        for i in range(11, -1, -1):
            punto = self.__points__[i]
            if punto:
                color = punto[0]
                ficha = simbolos.get(color, "?")
                cantidad = len(punto)
                if cantidad <= 5:
                    fila_inf += f"▼{ficha * cantidad: <2}"
                else:
                    fila_inf += f"▼{ficha}x{cantidad}"
            else:
                fila_inf += "▼  "
            if i == 6:
                fila_inf += "   |"
        fila_inf += "   |"
        print(fila_inf)
        print("  +---------------------+---------------------+")

        bar_blanco = len(self.__bar__.get("blanco", []))
        bar_negro = len(self.__bar__.get("negro", []))
        off_blanco = len(self.__final__.get("blanco", []))
        off_negro = len(self.__final__.get("negro", []))
        print(f"Barra: Blanco={bar_blanco}  Negro={bar_negro}   |   Final: Blanco={off_blanco}  Negro={off_negro}")