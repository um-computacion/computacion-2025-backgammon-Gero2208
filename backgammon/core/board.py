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

    def mostrar_tablero_cli(self, alto_col=5, ancho_col=3, simbolos=None):
        """
        Muestra el tablero de Backgammon en la consola de forma alineada.
        - alto_col: alto visible de cada columna de fichas (5 por defecto).
        - ancho_col: ancho fijo de cada celda/columna (3 por defecto).
        - simbolos: dict opcional {"blanco": "○", "negro": "●"}.
        """
        # --- Config ---
        if simbolos is None:
            simbolos = {"blanco": "○", "negro": "●"}
        VACIO = " "

        def celda(txt):
            return f"{txt:^{ancho_col}}"

        def columna_para_pila(pila, orientacion="top"):
            """
            Devuelve una lista de largo alto_col, con las fichas 'pegadas'
            hacia 'top' (para fila superior) o 'bottom' (para fila inferior).
            Si hay más de alto_col fichas, se muestran (alto_col-1) y un '×N'.
            """
            if not pila:
                return [celda(VACIO)] * alto_col

            color = pila[0]
            ficha = simbolos.get(color, VACIO)
            n = len(pila)

            if n <= alto_col:
                fichas = [celda(ficha)] * n
                vacios = [celda(VACIO)] * (alto_col - n)
                if orientacion == "top":
                    # Pegadas arriba
                    return fichas + vacios
                else:
                    # Pegadas abajo
                    return vacios + fichas
            else:
                # (alto_col-1) fichas + contador
                visibles = alto_col - 1
                contador = celda(f"×{n}")
                fichas = [celda(ficha)] * visibles
                if orientacion == "top":
                    return fichas + [contador]
                else:
                    return [contador] + fichas

        # --- Construcción de columnas visibles ---
        # Top visual: índices internos 12..23 (que el usuario ve como 13..24 izquierda->derecha)
        columnas_sup = [columna_para_pila(self.__points__[i], "top") for i in range(12, 24)]
        # Bottom visual: índices internos 11..0 (que el usuario ve como 12..1 izquierda->derecha)
        columnas_inf = [columna_para_pila(self.__points__[i], "bottom") for i in range(11, -1, -1)]

        # --- Helpers de impresión ---
        def separador():
            # Dos cuadrantes de 6 columnas cada uno
            return "  +" + "-" * (ancho_col * 6) + "+" + "-" * (ancho_col * 6) + "+"

        def linea_con_divisiones(celdas):
            # Inserta una barra vertical entre las columnas 6 y 7 (bar central)
            partes = ["  |"]
            for idx, c in enumerate(celdas, 1):
                partes.append(c)
                if idx == 6:
                    partes.append("|")
            partes.append("|")
            return "".join(partes)

        # --- Encabezados (números de puntos) ---
        cab_sup = []
        for p in range(13, 25):  # 13..24
            cab_sup.append(celda(str(p if p >= 10 else f" {p}")))
        cab_inf = []
        for p in range(12, 0, -1):  # 12..1
            cab_inf.append(celda(str(p if p >= 10 else f" {p}")))

        # --- Impresión ---
        print()
        print("   " + "".join(cab_sup[:6]) + " " + "".join(cab_sup[6:]))
        print(separador())

        # Fila superior: se imprime de arriba (índice alto) hacia abajo (índice 0)
        for fila in range(alto_col - 1, -1, -1):
            fila_sup = [col[fila] for col in columnas_sup]
            print(linea_con_divisiones(fila_sup))

        # Triángulos superiores
        triangles_up = [celda("▲")] * 12
        print(linea_con_divisiones(triangles_up))
        print(separador())

        # Triángulos inferiores
        triangles_down = [celda("▼")] * 12
        print(linea_con_divisiones(triangles_down))

        # Fila inferior: se imprime de abajo (índice 0) hacia arriba (índice alto)
        for fila in range(alto_col - 1, -1, -1):
            fila_inf = [col[fila] for col in columnas_inf]
            print(linea_con_divisiones(fila_inf))

        print(separador())
        print("   " + "".join(cab_inf[:6]) + " " + "".join(cab_inf[6:]))

        # --- Barra y fuera ---
        bar_blanco = len(self.__bar__.get("blanco", []))
        bar_negro = len(self.__bar__.get("negro", []))
        off_blanco = len(self.__final__.get("blanco", []))
        off_negro = len(self.__final__.get("negro", []))
        print(f"\nBarra: Blanco={bar_blanco}  Negro={bar_negro}   |   Final: Blanco={off_blanco}  Negro={off_negro}")

