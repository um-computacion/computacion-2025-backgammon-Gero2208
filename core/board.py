"""
Este módulo contiene la clase Board, que representa el tablero de Backgammon.
"""


class Board:
    """
    Representa el tablero de juego de Backgammon.

    Esta clase gestiona el estado de los 24 puntos del tablero, la barra
    para fichas capturadas y la zona final para las fichas que han salido.
    No contiene lógica de movimiento, solo representa el estado del tablero.

    Atributos:
        __points__ (list[list[str]]): Una lista de 24 listas, donde cada
                                     lista interna representa un punto y
                                     contiene las fichas (por color) en él.
        __bar__ (dict[str, list[str]]): Un diccionario que almacena las
                                        fichas capturadas para cada color.
        __final__ (dict[str, list[str]]): Un diccionario que almacena las
                                          fichas que han sido sacadas del
                                          tablero para cada color.
    """

    def __init__(self):
        """
        Inicializa un tablero de Backgammon vacío.
        """
        self.__points__ = [[] for _ in range(24)]
        self.__bar__ = {"blanco": [], "negro": []}
        self.__final__ = {"blanco": [], "negro": []}

    def get_bar(self):
        """
        Devuelve el estado de la barra.

        Returns:
            dict[str, list[str]]: El diccionario de la barra.
        """
        return self.__bar__

    def get_points(self):
        """
        Devuelve el estado de los puntos del tablero.

        Returns:
            list[list[str]]: La lista de puntos del tablero.
        """
        return self.__points__

    def increment_final(self, color):
        """
        Añade una ficha a la zona final del color especificado.

        Args:
            color (str): El color de la ficha a añadir.
        """
        self.__final__[color].append(color)

    def get_final(self):
        """
        Devuelve el estado de la zona final.

        Returns:
            dict[str, list[str]]: El diccionario de la zona final.
        """
        return self.__final__

    def setup(self, color1, color2):
        """
        Configura el tablero a la disposición inicial estándar de Backgammon.

        Args:
            color1 (str): El color del primer jugador.
            color2 (str): El color del segundo jugador.
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
        Devuelve una cadena de texto con la representación del tablero.

        Args:
            alto_col (int): La altura máxima de las columnas de fichas.
            ancho_col (int): El ancho de cada columna.
            simbolos (dict, optional): Un diccionario para personalizar los
                                       símbolos de las fichas.
        Returns:
            str: Una cadena de texto con la representación del tablero.
        """
        # --- Config ---
        if simbolos is None:
            simbolos = {"blanco": "●", "negro": "○"}
        vacio = " "

        def celda(txt):
            return f"{txt:^{ancho_col}}"

        def columna_para_pila(pila, orientacion="top"):
            """
            Devuelve una lista de largo alto_col, con las fichas 'pegadas'
            hacia 'top' (para fila superior) o 'bottom' (para fila inferior).
            Si hay más de alto_col fichas, se muestran (alto_col-1) y un '×N'.
            """
            if not pila:
                return [celda(vacio)] * alto_col

            color = pila[0]
            ficha = simbolos.get(color, vacio)
            n = len(pila)

            if n <= alto_col:
                fichas = [celda(ficha)] * n
                vacios = [celda(vacio)] * (alto_col - n)
                return fichas + vacios if orientacion == "top" else vacios + fichas
            # (alto_col-1) fichas + contador
            visibles = alto_col - 1
            contador = celda(f"×{n}")
            fichas = [celda(ficha)] * visibles
            return fichas + [contador] if orientacion == "top" else [contador] + fichas

        # --- Construcción de columnas visibles ---
        columnas_sup = [columna_para_pila(self.__points__[i], "top") for i in range(12, 24)]
        columnas_inf = [columna_para_pila(self.__points__[i], "bottom")
                        for i in range(11, -1, -1)]

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
        cab_sup = [celda(str(p if p >= 10 else f" {p}")) for p in range(13, 25)]
        cab_inf = [celda(str(p if p >= 10 else f" {p}")) for p in range(12, 0, -1)]

        # --- Construcción de la salida ---
        lines = []
        lines.append("")
        lines.append("   " + "".join(cab_sup[:6]) + " " + "".join(cab_sup[6:]))
        lines.append(separador())

        # Fila superior: se imprime de arriba (índice alto) hacia abajo (índice 0)
        for fila in range(alto_col - 1, -1, -1):
            fila_sup = [col[fila] for col in columnas_sup]
            lines.append(linea_con_divisiones(fila_sup))

        # Triángulos
        triangles_up = [celda("▲")] * 12
        lines.append(linea_con_divisiones(triangles_up))
        lines.append(separador())
        triangles_down = [celda("▼")] * 12
        lines.append(linea_con_divisiones(triangles_down))

        # Fila inferior
        for fila in range(alto_col - 1, -1, -1):
            fila_inf = [col[fila] for col in columnas_inf]
            lines.append(linea_con_divisiones(fila_inf))

        lines.append(separador())
        lines.append("   " + "".join(cab_inf[:6]) + " " + "".join(cab_inf[6:]))

        # --- Barra y fuera ---
        bar_blanco = len(self.__bar__.get("blanco", []))
        bar_negro = len(self.__bar__.get("negro", []))
        off_blanco = len(self.__final__.get("blanco", []))
        off_negro = len(self.__final__.get("negro", []))
        lines.append(f"\nBarra: Blanco={bar_blanco} Negro={bar_negro} | "
                     f"Final: Blanco={off_blanco} Negro={off_negro}")

        return "\n".join(lines)
