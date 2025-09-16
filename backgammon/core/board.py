class Board:
    """Representación simple del tablero de Backgammon.

    Internamente se representa como una lista de 24 puntos (índices 0..23).
    Cada punto es una lista de fichas, donde cada ficha es el identificador del jugador
    (por ejemplo: 'jugador1' o 'jugador2'). Además existen dos zonas especiales:
    - bar: fichas capturadas que deben volver a entrar.
    - final (borne-off): fichas que ya han salido del tablero.

    Esta implementación ofrece métodos mínimos necesarios para tests y lógica de juego:
    - setup(): coloca las fichas en la posición inicial estándar de Backgammon
    - get_point(idx): devuelve la lista de fichas en un punto
    - is_move_legal(player, from_idx, to_idx): comprobación básica de legalidad
    - apply_move(player, from_idx, to_idx): aplica un movimiento (no gestiona dados)
    - possible_moves(player, die): devuelve movimientos posibles para un dado

    Nota: Esta clase es una implementación inicial enfocada a claridad y testeo; reglas
    completas (entrada desde bar, bearing off con condiciones, golpes múltiples, etc.)
    se pueden agregar posteriormente.
    """

    def __init__(self):
        self.points = [[] for _ in range(24)]
        self.bar = {"jugador1": [], "jugador2": []}
        self.final = {"jugador1": [], "jugador2": []}

    def setup(self):
        """Coloca las fichas en la disposición inicial estándar.

        Usamos la convención:
        - 'jugador1' empieza en el punto 0 con 2 fichas, etc. (convención de índice)
        La colocación estándar de Backgammon (índices 0..23) suele ser:
        jugador1: 2 en 0, 5 en 11, 3 en 16, 5 en 18  (o una rotación equivalente)
        jugador2: posiciones simétricas en el otro lado.
        """
        # Limpiar
        self.points = [[] for _ in range(24)]
        self.bar = {"jugador1": [], "jugador2": []}
        self.final = {"jugador1": [], "jugador2": []}

        # Disposición (convención elegida):
        # jugador1
        self.points[0] = ["jugador1"] * 2
        self.points[11] = ["jugador1"] * 5
        self.points[16] = ["jugador1"] * 3
        self.points[18] = ["jugador1"] * 5

        # jugador2 - posiciones simétricas (24 - idx)
        self.points[23] = ["jugador2"] * 2
        self.points[12] = ["jugador2"] * 5
        self.points[7] = ["jugador2"] * 3
        self.points[5] = ["jugador2"] * 5