# Prompts para la documentación del videojuego Backgammon
## Modelo utilizado: GPT-5 mini (Excepto que se aclare en el prompt)

## Prompt

### Documenta la clase Dice y los actuales métodos que tiene

## Response

class Dice:
    """
    Clase que representa los dados utilizados en el juego de Backgammon.

    Atributos:
        __valor__ (list[int]): Lista con los valores actuales de los dos dados. 
                               Inicialmente [0, 0]. Se actualiza con cada tirada.

    Métodos:
        roll(): Lanza los dos dados y actualiza el atributo __valor__ con valores aleatorios entre 1 y 6.
        dobles(): Devuelve True si ambos dados tienen el mismo valor, False en caso contrario.
    """
    def __init__(self):
        self.__valor__ = [0, 0]

    def roll(self):
        """
        Lanza los dos dados y actualiza el atributo __valor__ con valores aleatorios entre 1 y 6.

        Returns:
            list[int]: Lista con los dos valores obtenidos.
        """
        self.__valor__ = [random.randint(1, 6), random.randint(1, 6)]
        return self.__valor__
    
    def dobles(self):
        """
        Verifica si ambos dados tienen el mismo valor.

        Returns:
            bool: True si los dos valores son iguales, False en caso contrario.
        """
        return self.__valor__[0] == self.__valor__[1]

## Prompt

### Documenta la clase Game y los actuales métodos que tiene

## Response

class Game:
    """
    Clase que gestiona los turnos de una partida de Backgammon.

    Atributos:
        __p1__ (Player): Primer jugador.
        __p2__ (Player): Segundo jugador.
        __turno__ (int): 0 si es el turno de __p1__, 1 si es el turno de __p2__.

    Métodos:
        __init__(p1, p2): Inicializa la partida con dos jugadores y establece el turno inicial.
        jugador_actual(): Devuelve el jugador cuyo turno es actualmente.
        cambiar_turno(): Alterna el turno entre los dos jugadores.
    """

    def __init__(self, p1, p2):
        self.__p1__ = p1
        self.__p2__ = p2
        self.__turno__ = 0  # 0 para p1, 1 para p2

    def jugador_actual(self):
        """
        Devuelve el jugador cuyo turno es actualmente.

        Returns:
            Player: El jugador que debe jugar en este turno.
        """
        return self.__p1__ if self.__turno__ == 0 else self.__p2__

    def cambiar_turno(self):
        """
        Alterna el turno entre los dos jugadores.
        """
        self.__turno__ = 1 - self.__turno__

## Prompt (Se utilizó Jules)

### Haz docstring para la clase Board y todos sus métodos

## Response

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
        Muestra una representación del tablero en la consola.

        Args:
            alto_col (int): La altura máxima de las columnas de fichas.
            ancho_col (int): El ancho de cada columna.
            simbolos (dict, optional): Un diccionario para personalizar los
                                       símbolos de las fichas.
        """
        # --- Config ---
        if simbolos is None:
            simbolos = {"blanco": "●", "negro": "○"}
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

## Prompt (Se utilizó Jules)

### Haz docstring para la clase Checkers y todos sus métodos

## Response

from .exceptions import MovimientoInvalido

class Checkers:
    """
    Clase que contiene la lógica estática para validar y ejecutar movimientos de fichas.
    """
    @staticmethod
    def es_movimiento_valido(board, jugador, origen, destino, dado):
        """
        Valida si un movimiento de una ficha de un punto a otro es válido.

        Args:
            board (Board): El tablero de juego.
            jugador (Player): El jugador que realiza el movimiento.
            origen (int): El punto de origen del movimiento.
            destino (int): El punto de destino del movimiento.
            dado (int): El valor del dado utilizado para el movimiento.

        Raises:
            MovimientoInvalido: Si el movimiento no es válido por alguna razón.
        """
        color = jugador.color()
        direccion = jugador.direccion()
        puntos = board.get_points()
        if origen < 0 or origen > 23 or destino < 0 or destino > 23:
            raise MovimientoInvalido("Origen o destino fuera del tablero.")
        if not puntos[origen] or puntos[origen][0] != color:
            raise MovimientoInvalido("No hay ficha propia en el origen.")
        if destino != origen + direccion * dado:
            raise MovimientoInvalido("El destino no corresponde al dado y dirección.")
        if puntos[destino]:
            color_destino = puntos[destino][0]
            cantidad = len(puntos[destino])
            if color_destino != color and cantidad > 1:
                raise MovimientoInvalido("No puedes mover a una casilla ocupada por 2 o más fichas rivales.")
            
    @staticmethod
    def mover(board, jugador, origen, destino, dado):
        """
        Mueve una ficha de un punto de origen a uno de destino.

        Args:
            board (Board): El tablero de juego.
            jugador (Player): El jugador que realiza el movimiento.
            origen (int): El punto de origen del movimiento.
            destino (int): El punto de destino del movimiento.
            dado (int): El valor del dado utilizado para el movimiento.
        """
        Checkers.es_movimiento_valido(board, jugador, origen, destino, dado)
        color = jugador.color()
        puntos = board.get_points()
        bar = board.get_bar()

        # captura: si en destino hay 1 ficha y es rival -> enviarla a la barra
        if puntos[destino] and puntos[destino][0] != color and len(puntos[destino]) == 1:
            enemigo_color = puntos[destino].pop()
            bar[enemigo_color].append(enemigo_color)

        # mover la ficha desde origen a destino
        puntos[origen].pop()
        puntos[destino].append(color)

    @staticmethod
    def destinos_posibles(board, jugador, origen, dados):
        """
        Calcula los destinos posibles para una ficha desde un punto de origen con los dados disponibles.

        Args:
            board (Board): El tablero de juego.
            jugador (Player): El jugador que realiza el movimiento.
            origen (int): El punto de origen.
            dados (list[int]): La lista de dados disponibles.

        Returns:
            list[int]: Una lista de los puntos de destino posibles.
        """
        color = jugador.color()
        direccion = jugador.direccion()
        puntos = board.get_points()
        destinos = []
        for dado in dados:
            destino = origen + direccion * dado
            if 0 <= destino <= 23:
                try:
                    Checkers.es_movimiento_valido(board, jugador, origen, destino, dado)
                    if destino not in destinos:
                        destinos.append(destino)
                except MovimientoInvalido:
                    continue
        return destinos
    
    @staticmethod
    def dado_para_movimiento(jugador, origen, destino, dados):
        """
        Determina qué dado se corresponde con un movimiento de un origen a un destino.

        Args:
            jugador (Player): El jugador que realiza el movimiento.
            origen (int): El punto de origen.
            destino (int): El punto de destino.
            dados (list[int]): La lista de dados disponibles.

        Returns:
            int or None: El valor del dado si el movimiento es posible, o None en caso contrario.
        """
        direccion = jugador.direccion()
        delta = destino - origen
        dado = delta * direccion  # +1/-1 normaliza el signo
        if dado <= 0:
            return None
        return dado if dado in dados else None
    
    @staticmethod
    def mover_y_consumir(board, jugador, origen, destino, dados):
        """
        Realiza un movimiento y consume el dado correspondiente.

        Args:
            board (Board): El tablero de juego.
            jugador (Player): El jugador que realiza el movimiento.
            origen (int): El punto de origen.
            destino (int): El punto de destino.
            dados (list[int]): La lista de dados disponibles.

        Returns:
            list[int]: La lista de dados restantes.
        """
        dado_usado = Checkers.dado_para_movimiento(jugador, origen, destino, dados)
        if dado_usado is None:
            raise MovimientoInvalido("Movimiento incompatible con los dados disponibles.")
        Checkers.mover(board, jugador, origen, destino, dado_usado)
        restantes = dados.copy()
        restantes.remove(dado_usado)  # consume una ocurrencia
        return restantes

    @staticmethod
    def hay_movimientos_posibles(board, jugador, dados):
        """
        Verifica si el jugador tiene algún movimiento posible con los dados disponibles.

        Args:
            board (Board): El tablero de juego.
            jugador (Player): El jugador actual.
            dados (list[int]): La lista de dados disponibles.

        Returns:
            bool: True si hay al menos un movimiento posible, False en caso contrario.
        """
        puntos = board.get_points()
        color = jugador.color()

        # 1. Comprobar movimientos normales en el tablero
        for i in range(24):
            if puntos[i] and puntos[i][0] == color:
                if Checkers.destinos_posibles(board, jugador, i, dados):
                    return True
        
        # 2. Si no hay movimientos normales, comprobar si se puede hacer "bear off"
        if Checkers.todas_en_inicio(board, jugador):
            # Iterar sobre las fichas en la casa del jugador
            casa_range = range(18, 24) if jugador.direccion() == 1 else range(6)
            for origen in casa_range:
                if puntos[origen] and puntos[origen][0] == color:
                    # Iterar sobre los dados disponibles
                    for dado in dados:
                        if Checkers.puede_bear_off(board, jugador, origen, dado):
                            return True
        return False

    @staticmethod
    def destino_entrada_por_dado(jugador, dado):
        """
        Devuelve el índice de punto donde se intenta entrar desde la barra
        para un dado dado, según la dirección del jugador.

        Args:
            jugador (Player): El jugador que intenta reingresar.
            dado (int): El valor del dado a utilizar.

        Returns:
            int: El punto de destino para el reingreso.
        """
        direccion = jugador.direccion()
        if direccion == 1:
            return dado - 1        # dados 1..6 -> índices 0..5
        else:
            return 24 - dado       # dados 1..6 -> índices 23..18

    @staticmethod
    def puede_reingresar(board, jugador, dado):
        """
        Comprueba si con el valor 'dado' se puede reingresar una ficha desde la barra.

        Args:
            board (Board): El tablero de juego.
            jugador (Player): El jugador que intenta reingresar.
            dado (int): El valor del dado a utilizar.

        Returns:
            int or None: El índice de destino si es posible, o None si no.
        """
        destino = Checkers.destino_entrada_por_dado(jugador, dado)
        if destino < 0 or destino > 23:
            return None
        puntos = board.get_points()
        color = jugador.color()
        if not puntos[destino]: return destino
        if puntos[destino][0] == color: return destino
        if len(puntos[destino]) == 1: return destino
        return None

    @staticmethod
    def reingresar_desde_bar(board, jugador, dado):
        """
        Ejecuta la entrada desde la barra usando 'dado'.

        Args:
            board (Board): El tablero de juego.
            jugador (Player): El jugador que reingresa.
            dado (int): El valor del dado a utilizar.

        Raises:
            MovimientoInvalido: Si no se puede reingresar con ese dado.
        """
        destino = Checkers.puede_reingresar(board, jugador, dado)
        if destino is None:
            raise MovimientoInvalido("No puedes reingresar con ese dado.")
        color = jugador.color()
        bar = board.get_bar()
        puntos = board.get_points()
        bar[color].pop()
        if puntos[destino] and puntos[destino][0] != color:
            enemigo_color = puntos[destino].pop()
            bar[enemigo_color].append(enemigo_color)
        puntos[destino].append(color)

    @staticmethod
    def todas_en_inicio(board, jugador) -> bool:
        """
        Verifica si todas las fichas del jugador están en su tablero de casa.

        Args:
            board (Board): El tablero de juego.
            jugador (Player): El jugador a verificar.

        Returns:
            bool: True si todas las fichas están en casa, False en caso contrario.
        """
        color = jugador.color()
        direccion = jugador.direccion()
        if board.get_bar().get(color): return False
        puntos = board.get_points()
        if direccion == 1:
            for i in range(0, 18):
                if puntos[i] and puntos[i][0] == color: return False
        else:
            for i in range(6, 24):
                if puntos[i] and puntos[i][0] == color: return False
        return True

    @staticmethod
    def distancia_desde_origen(board, jugador, origen: int) -> bool:
        """
        Verifica si hay fichas del jugador en puntos más alejados del final que el origen.

        Args:
            board (Board): El tablero de juego.
            jugador (Player): El jugador a verificar.
            origen (int): El punto de origen a comparar.

        Returns:
            bool: True si hay fichas más alejadas, False en caso contrario.
        """
        color = jugador.color()
        puntos = board.get_points()
        if jugador.direccion() == 1:
            for i in range(18, origen):
                if puntos[i] and puntos[i][0] == color: return True
        else:
            for i in range(origen + 1, 6):
                if puntos[i] and puntos[i][0] == color: return True
        return False

    @staticmethod
    def puede_bear_off(board, jugador, origen: int, dado: int):
        """
        Verifica si un movimiento de bear_off es válido sin ejecutarlo.

        Args:
            board (Board): El tablero de juego.
            jugador (Player): El jugador que realiza el movimiento.
            origen (int): El punto desde el que se saca la ficha.
            dado (int): El valor del dado a utilizar.

        Returns:
            bool: True si el bear_off es posible, False en caso contrario.
        """
        try:
            # Replicar la lógica de validación de bear_off sin modificar el tablero
            if not Checkers.todas_en_inicio(board, jugador): return False
            color = jugador.color()
            puntos = board.get_points()
            direccion = jugador.direccion()
            punto_exacto = (24 - dado) if direccion == 1 else (dado - 1)

            if 0 <= punto_exacto < 24 and puntos[punto_exacto] and puntos[punto_exacto][0] == color:
                if origen != punto_exacto: return False
            else:
                hay_fichas_superiores = False
                if direccion == 1:
                    for i in range(18, punto_exacto):
                        if puntos[i] and puntos[i][0] == color: hay_fichas_superiores = True; break
                else:
                    for i in range(punto_exacto + 1, 6):
                        if puntos[i] and puntos[i][0] == color: hay_fichas_superiores = True; break
                if hay_fichas_superiores: return False

                punto_mas_alto = -1
                if direccion == 1:
                    for i in range(23, 17, -1):
                        if puntos[i] and puntos[i][0] == color: punto_mas_alto = i; break
                else:
                    for i in range(5, -1, -1):
                        if puntos[i] and puntos[i][0] == color: punto_mas_alto = i; break
                
                if punto_mas_alto == -1: return False
                distancia_mas_alta = (24 - punto_mas_alto) if direccion == 1 else (punto_mas_alto + 1)
                if dado < distancia_mas_alta or origen != punto_mas_alto: return False
            return True
        except:
            return False
        
    @staticmethod
    def bear_off(board, jugador, origen: int, dado: int):
        """
        Realiza el movimiento de sacar una ficha del tablero (bear off).

        Args:
            board (Board): El tablero de juego.
            jugador (Player): El jugador que saca la ficha.
            origen (int): El punto desde el que se saca la ficha.
            dado (int): El valor del dado a utilizar.

        Raises:
            MovimientoInvalido: Si no se puede sacar la ficha.
        """
        if not Checkers.todas_en_inicio(board, jugador):
            raise MovimientoInvalido("Aún no puedes sacar fichas.")

        color = jugador.color()
        puntos = board.get_points()
        direccion = jugador.direccion()

        # Calcular el punto exacto que corresponde al dado
        punto_exacto = -1
        if direccion == 1:
            punto_exacto = 24 - dado
        else:
            punto_exacto = dado - 1

        # Caso 1: El punto exacto está ocupado
        if 0 <= punto_exacto < 24 and puntos[punto_exacto] and puntos[punto_exacto][0] == color:
            if origen != punto_exacto:
                raise MovimientoInvalido(f"Debes sacar la ficha desde el punto {punto_exacto + 1}.")
            puntos[origen].pop()
            board.increment_final(color)
            return

        # Si el punto exacto está libre, comprobar si hay fichas en puntos superiores
        hay_fichas_superiores = False
        if direccion == 1: # Casa en 18-23
            for i in range(18, punto_exacto):
                if puntos[i] and puntos[i][0] == color:
                    hay_fichas_superiores = True
                    break
        else: # Casa en 0-5
            for i in range(punto_exacto + 1, 6):
                if puntos[i] and puntos[i][0] == color:
                    hay_fichas_superiores = True
                    break
        
        if hay_fichas_superiores:
             raise MovimientoInvalido("No puedes sacar fichas si tienes otras en puntos más altos.")

        # Caso 2: El punto exacto está vacío y no hay fichas en puntos superiores
        else:
            # Buscar el punto más alto ocupado
            punto_mas_alto = -1
            if direccion == 1: # Casa en 18-23, el más alto es el de mayor índice
                for i in range(23, 17, -1):
                    if puntos[i] and puntos[i][0] == color:
                        punto_mas_alto = i
                        break
            else: # Casa en 0-5, el más alto es el de mayor índice
                for i in range(5, -1, -1):
                    if puntos[i] and puntos[i][0] == color:
                        punto_mas_alto = i
                        break
            
            if punto_mas_alto == -1:
                raise MovimientoInvalido("No tienes fichas para sacar.")

            # El dado debe ser mayor o igual a la distancia del punto más alto
            distancia_mas_alta = (24 - punto_mas_alto) if direccion == 1 else (punto_mas_alto + 1)
            
            if dado >= distancia_mas_alta:
                if origen != punto_mas_alto:
                     raise MovimientoInvalido(f"Debes sacar la ficha desde tu punto más alto: {punto_mas_alto + 1}.")
                puntos[origen].pop()
                board.increment_final(color)
            else:
                raise MovimientoInvalido("No puedes usar ese dado para sacar una ficha.")

## Prompt (Se utilizó Jules)

### Haz docstring para la clase Dice y todos sus métodos

## Response

import random

class Dice:
    """
    Representa un par de dados para el juego de Backgammon.

    Esta clase gestiona el estado y el comportamiento de los dados,
    incluyendo su lanzamiento y la gestión de dobles.

    Atributos:
        __valor__ (list[int]): Una lista de dos enteros que representan
                               el valor de cada dado.
    """
    def __init__(self):
        """
        Inicializa los dados con un valor de [0, 0].
        """
        self.__valor__ = [0, 0]

    def roll(self):
        """
        Lanza los dados para obtener nuevos valores aleatorios.

        Asigna dos nuevos valores aleatorios entre 1 y 6 a los dados.

        Returns:
            list[int]: La lista con los dos nuevos valores de los dados.
        """
        self.__valor__ = [random.randint(1, 6), random.randint(1, 6)]
        return self.__valor__
    
    def dobles(self):
        """
        Comprueba si los dos dados tienen el mismo valor.

        Returns:
            bool: True si los valores de los dados son iguales, False en caso contrario.
        """
        return self.__valor__[0] == self.__valor__[1]
    
    def duplicar(self):
        """
        Devuelve los valores de los dados, duplicados si son dobles.

        Si los dados son dobles, devuelve una lista con cuatro veces el valor del dado.
        Si no, devuelve una lista con los dos valores de los dados.

        Returns:
            list[int]: Una lista de 4 elementos si son dobles, o 2 en caso contrario.
        """
        if self.dobles():
            return [self.__valor__[0]] * 4 
        else:
            return self.__valor__
    
    def set_valor(self, valor):
        """
        Establece el valor de los dados con fines de prueba.

        Args:
            valor (list[int]): La lista de valores a establecer.
        """
        self.__valor__ = valor

## Prompt (Se utilizó Jules)

### Haz docstring para la clase Game y todos sus métodos

## Response

from .player import Player
from .board import Board
from .dice import Dice
from .checkers import Checkers
from .exceptions import MovimientoInvalido, DadoInvalido, OrigenInvalido
import random

class Game:
    """
    Clase principal que orquesta una partida de Backgammon.

    Esta clase actúa como el controlador central del juego, gestionando el
    estado de la partida, los turnos de los jugadores, el lanzamiento de

    dados y la validación de movimientos. Es la interfaz principal para
    las interfaces de usuario (CLI, Pygame).

    Atributos:
        __p1__ (Player): El primer jugador.
        __p2__ (Player): El segundo jugador.
        __turno__ (int): El índice del jugador actual (0 para p1, 1 para p2).
        __board__ (Board): La instancia del tablero de juego.
        __dice__ (Dice): La instancia de los dados.
        movimientos_restantes (list[int]): Una lista de los valores de los
                                           dados que aún se pueden usar en
                                           el turno actual.
    """

    def __init__(self, p1, p2):
        """
        Inicializa una nueva partida de Backgammon.

        Args:
            p1 (Player): El primer jugador.
            p2 (Player): El segundo jugador.
        """
        self.__p1__ = p1
        self.__p2__ = p2
        self.__turno__ = 0
        self.__board__ = Board()
        self.__board__.setup(p1.color(), p2.color())
        self.__dice__ = Dice()
        self.movimientos_restantes = []

    def decidir_iniciador(self):
        """
        Determina qué jugador comienza la partida.

        Cada jugador lanza un dado, y el que obtenga el número más alto
        comienza. En caso de empate, se repite el lanzamiento.

        Returns:
            tuple[Player, int, int]: Una tupla con el jugador que inicia,
                                     el tiro del jugador 1 y el tiro del
                                     jugador 2.
        """
        while True:
            tiro_p1 = random.randint(1, 6)
            tiro_p2 = random.randint(1, 6)
            if tiro_p1 > tiro_p2:
                self.__turno__ = 0
                return self.__p1__, tiro_p1, tiro_p2
            elif tiro_p2 > tiro_p1:
                self.__turno__ = 1
                return self.__p2__, tiro_p1, tiro_p2

    def jugador_actual(self):
        """
        Devuelve el jugador cuyo turno está en curso.

        Returns:
            Player: La instancia del jugador actual.
        """
        return self.__p1__ if self.__turno__ == 0 else self.__p2__

    def cambiar_turno(self):
        """
        Pasa el turno al siguiente jugador.
        """
        self.__turno__ = 1 - self.__turno__
        self.movimientos_restantes = []

    def lanzar_dados(self):
        """
        Lanza los dados al comienzo de un turno.

        Actualiza los movimientos restantes para el turno actual.

        Returns:
            list[int]: La lista de movimientos de dados disponibles.
        """
        self.__dice__.roll()
        self.movimientos_restantes = self.__dice__.duplicar()
        return self.movimientos_restantes

    def mover_ficha(self, origen, destino):
        """
        Ejecuta el movimiento de una ficha de un origen a un destino.

        Valida el movimiento y, si es válido, lo aplica al tablero,
        consumiendo el dado correspondiente.

        Args:
            origen (int): El punto de origen del movimiento.
            destino (int): El punto de destino del movimiento.

        Raises:
            MovimientoInvalido: Si el movimiento no es válido.
        """
        self.movimientos_restantes = Checkers.mover_y_consumir(
            self.__board__, self.jugador_actual(), origen, destino, self.movimientos_restantes
        )

    def get_board_status(self):
        """
        Devuelve el estado actual del tablero.

        Returns:
            Board: La instancia del tablero del juego.
        """
        return self.__board__

    def hay_movimientos_posibles(self):
        """
        Verifica si el jugador actual tiene algún movimiento legal.

        Returns:
            bool: True si hay al menos un movimiento posible, False en caso contrario.
        """
        if self.jugador_tiene_fichas_en_barra():
             for dado in self.movimientos_restantes:
                 if Checkers.puede_reingresar(self.__board__, self.jugador_actual(), dado) is not None:
                     return True
             return False
        return Checkers.hay_movimientos_posibles(self.__board__, self.jugador_actual(), self.movimientos_restantes)

    def jugador_tiene_fichas_en_barra(self):
        """
        Comprueba si el jugador actual tiene fichas en la barra.

        Returns:
            list[str]: La lista de fichas en la barra, o una lista vacía.
        """
        color_actual = self.jugador_actual().color()
        return self.__board__.get_bar().get(color_actual, [])

    def posibles_entradas_desde_barra(self):
        """
        Calcula los posibles movimientos de reingreso desde la barra.

        Returns:
            list[tuple[int, int]]: Una lista de tuplas, donde cada una
                                   contiene un dado y el destino
                                   correspondiente.
        """
        entradas = []
        for dado in self.movimientos_restantes:
            destino = Checkers.puede_reingresar(self.__board__, self.jugador_actual(), dado)
            if destino is not None:
                entradas.append((dado, destino))
        return entradas

    def reingresar_desde_barra(self, dado):
        """
        Reingresa una ficha desde la barra al tablero.

        Args:
            dado (int): El valor del dado a utilizar para el reingreso.

        Raises:
            DadoInvalido: Si el dado no está disponible.
            MovimientoInvalido: Si el reingreso con ese dado no es válido.
        """
        if dado not in self.movimientos_restantes:
            raise DadoInvalido("No tienes ese dado disponible.")
        
        Checkers.reingresar_desde_bar(self.__board__, self.jugador_actual(), dado)
        self.movimientos_restantes.remove(dado)

    def todas_fichas_en_casa(self):
        """
        Comprueba si todas las fichas del jugador actual están en su casa.

        Returns:
            bool: True si todas las fichas están en casa, False en caso contrario.
        """
        return Checkers.todas_en_inicio(self.__board__, self.jugador_actual())

    def sacar_ficha(self, origen, dado):
        """
        Saca una ficha del tablero (bear off).

        Args:
            origen (int): El punto desde el que se saca la ficha.
            dado (int): El valor del dado a utilizar.

        Raises:
            DadoInvalido: Si el dado no está disponible.
            MovimientoInvalido: Si no es posible sacar la ficha.
        """
        if dado not in self.movimientos_restantes:
            raise DadoInvalido("No tienes ese dado disponible.")
        
        Checkers.bear_off(self.__board__, self.jugador_actual(), origen, dado)
        self.movimientos_restantes.remove(dado)

    def validar_origen_y_obtener_destinos(self, origen):
        """
        Valida un punto de origen y devuelve los destinos posibles.

        Args:
            origen (int): El punto de origen a validar.

        Returns:
            list[int]: Una lista de destinos posibles desde el origen.

        Raises:
            OrigenInvalido: Si no hay movimientos posibles desde el origen.
        """
        destinos = Checkers.destinos_posibles(self.__board__, self.jugador_actual(), origen, self.movimientos_restantes)
        if not destinos:
            raise OrigenInvalido(f"No hay movimientos posibles desde la casilla {origen + 1} con los dados actuales.")
        return destinos

    def ganador(self):
        """
        Comprueba si algún jugador ha ganado la partida.

        Un jugador gana si ha sacado sus 15 fichas del tablero.

        Returns:
            Player or None: El jugador ganador, o None si la partida no ha
                            terminado.
        """
        final = self.__board__.get_final()
        p1_color = self.__p1__.color()
        p2_color = self.__p2__.color()

        if len(final.get(p1_color, [])) >= 15:
            return self.__p1__
        if len(final.get(p2_color, [])) >= 15:
            return self.__p2__
        return None

## Prompt (Se utilizó Jules)

### Haz docstring para la clase Player y todos sus métodos

## Response

class Player:
    """
    Representa a un jugador en el juego de Backgammon.

    Esta clase almacena la información esencial de un jugador, incluyendo su
    nombre, color y la dirección en la que se mueven sus fichas en el tablero.

    Atributos:
        __nombre__ (str): El nombre del jugador.
        __color__ (str): El color de las fichas del jugador ('blanco' o 'negro').
        __direccion__ (int): La dirección de movimiento del jugador en el
                             tablero (+1 para los blancos, -1 para los negros).
    """
    def __init__(self, color: str, nombre: str, direccion: int):
        """
        Inicializa una nueva instancia de Jugador.

        Args:
            color (str): El color de las fichas del jugador.
            nombre (str): El nombre del jugador.
            direccion (int): La dirección de movimiento en el tablero.
        """
        self.__nombre__ = str(nombre)
        self.__color__ = str(color)
        self.__direccion__ = direccion

    def nombre(self):
        """
        Devuelve el nombre del jugador.

        Returns:
            str: El nombre del jugador.
        """
        return self.__nombre__
    
    def color(self):
        """
        Devuelve el color de las fichas del jugador.

        Returns:
            str: El color del jugador ('blanco' o 'negro').
        """
        return self.__color__
    
    def direccion(self):
        """
        Devuelve la dirección de movimiento del jugador en el tablero.

        Returns:
            int: La dirección de movimiento (+1 o -1).
        """
        return self.__direccion__

## Prompt (Se utilizó Jules)

### Haz docstring para el CLI

## Response

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
        board.mostrar_tablero_cli()
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
                board.mostrar_tablero_cli()
                print(f"Dados restantes: {game.movimientos_restantes}")

        ganador_actual = game.ganador()
        if ganador_actual:
            print(f"¡Felicidades, {ganador_actual.nombre()}! Has ganado la partida.")
            board.mostrar_tablero_cli()
            break
        
        game.cambiar_turno()

if __name__ == '__main__':
    main()


## Prompt (Se utilizó Jules)

### Haz docstring para el ui de pygame

## Response

import pygame
from core.game import Game
from core.player import Player

# --- Constantes ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

# --- Colores ---
COLOR_FONDO = (210, 180, 140)  # Un color madera claro
COLOR_PICO_1 = (139, 69, 19)   # Marrón oscuro
COLOR_PICO_2 = (245, 245, 220)  # Beige
COLOR_BARRA = (100, 100, 100)  # Gris para la barra
COLOR_FICHA_BLANCA = (255, 255, 255)
COLOR_FICHA_NEGRA = (0, 0, 0)
COLOR_TEXTO = (20, 20, 20)

# --- Dimensiones del tablero ---
MARGEN = 20
ANCHO_PICO = (ANCHO_VENTANA - 2 * MARGEN) // 13  # 12 picos + 1 para la barra
ALTO_PICO = ALTO_VENTANA // 2 - MARGEN
ANCHO_BARRA = ANCHO_PICO


# --- Funciones de Dibujado ---

def dibujar_tablero(pantalla):
    """
    Dibuja el tablero de Backgammon en la pantalla.

    Esto incluye el fondo, los picos triangulares y la barra central.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
    """
    pantalla.fill(COLOR_FONDO)

    # Dibujar los picos
    for i in range(12):
        color = COLOR_PICO_1 if i % 2 == 0 else COLOR_PICO_2
        
        # Picos superiores
        x_base = MARGEN + i * ANCHO_PICO
        if i >= 6:  # Añadir espacio para la barra
            x_base += ANCHO_BARRA
        
        puntos = [(x_base, MARGEN), 
                  (x_base + ANCHO_PICO, MARGEN), 
                  (x_base + ANCHO_PICO / 2, MARGEN + ALTO_PICO)]
        pygame.draw.polygon(pantalla, color, puntos)

        # Picos inferiores
        puntos = [(x_base, ALTO_VENTANA - MARGEN), 
                  (x_base + ANCHO_PICO, ALTO_VENTANA - MARGEN), 
                  (x_base + ANCHO_PICO / 2, ALTO_VENTANA - MARGEN - ALTO_PICO)]
        pygame.draw.polygon(pantalla, color, puntos)

    # Dibujar la barra central
    pygame.draw.rect(pantalla, COLOR_BARRA, 
                     (MARGEN + 6 * ANCHO_PICO, MARGEN, 
                      ANCHO_BARRA, ALTO_VENTANA - 2 * MARGEN))

def dibujar_fichas(pantalla, board):
    """
    Dibuja las fichas en sus posiciones actuales en el tablero.

    Esto incluye las fichas en los picos y en la barra.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
        board (Board): El objeto del tablero que contiene el estado de las fichas.
    """
    puntos = board.get_points()
    bar = board.get_bar()
    radio_ficha = ANCHO_PICO // 2 - 5

    # Dibujar fichas en la barra
    y_base_blanco = ALTO_VENTANA / 2 - radio_ficha
    y_base_negro = ALTO_VENTANA / 2 + radio_ficha
    x_bar = MARGEN + 6 * ANCHO_PICO + ANCHO_BARRA / 2

    for i, color in enumerate(["blanco", "negro"]):
        y_base = y_base_blanco if color == "blanco" else y_base_negro
        for j, ficha in enumerate(bar.get(color, [])):
            color_ficha = COLOR_FICHA_BLANCA if color == "blanco" else COLOR_FICHA_NEGRA
            pygame.draw.circle(pantalla, color_ficha, (int(x_bar), int(y_base - j * 2 * radio_ficha)), radio_ficha)
            pygame.draw.circle(pantalla, (0,0,0), (int(x_bar), int(y_base - j * 2 * radio_ficha)), radio_ficha, 2)

    # Dibujar fichas en los picos
    for i, punto in enumerate(puntos):
        if not punto:
            continue

        color_str = punto[0]
        color_ficha = COLOR_FICHA_BLANCA if color_str == "blanco" else COLOR_FICHA_NEGRA
        
        for j, _ in enumerate(punto):
            # Calcular la posición de la ficha
            if i < 12:  # Picos inferiores
                x = ANCHO_VENTANA - MARGEN - (i * ANCHO_PICO) - ANCHO_PICO / 2
                if i >= 6:
                    x -= ANCHO_BARRA
                y = ALTO_VENTANA - MARGEN - radio_ficha - (j * 2 * radio_ficha)
            else:  # Picos superiores
                x = MARGEN + ((i - 12) * ANCHO_PICO) + ANCHO_PICO / 2
                if (i - 12) >= 6:
                    x += ANCHO_BARRA
                y = MARGEN + radio_ficha + (j * 2 * radio_ficha)

            pygame.draw.circle(pantalla, color_ficha, (int(x), int(y)), radio_ficha)
            # Dibujar un borde para que se distingan
            pygame.draw.circle(pantalla, (0,0,0), (int(x), int(y)), radio_ficha, 2)

def get_pico_desde_pos(pos):
    """
    Convierte las coordenadas de la pantalla (x, y) al índice del pico correspondiente.

    Args:
        pos (tuple[int, int]): Una tupla con las coordenadas x e y del clic.

    Returns:
        int or None: El índice del pico (0-23) si el clic está en un pico,
                     o None en caso contrario.
    """
    x, y = pos
    
    # Fuera de los márgenes verticales
    if not (MARGEN < y < ALTO_VENTANA - MARGEN):
        return None

    # Ajustar x por la barra central
    x_ajustado = x - MARGEN
    if x_ajustado > 6 * ANCHO_PICO:
        x_ajustado -= ANCHO_BARRA

    # Calcular el índice de la columna (0-11)
    col = x_ajustado // ANCHO_PICO
    if not (0 <= col < 12):
        return None

    # Determinar si es un pico superior o inferior
    if y < ALTO_VENTANA / 2:
        # Picos superiores (12-23)
        return int(12 + col)
    else:
        # Picos inferiores (11-0)
        return int(11 - col)

def dibujar_seleccion(pantalla, pico):
    """
    Resalta un pico seleccionado en el tablero.

    Dibuja un borde alrededor del pico para indicar que está seleccionado.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
        pico (int or None): El índice del pico a resaltar.
    """
    if pico is None:
        return

    # Calcular la geometría del pico
    if pico < 12:  # Picos inferiores
        x_base = ANCHO_VENTANA - MARGEN - ((pico + 1) * ANCHO_PICO)
        if pico >= 6:
            x_base -= ANCHO_BARRA
        
        puntos = [(x_base, ALTO_VENTANA - MARGEN), 
                  (x_base + ANCHO_PICO, ALTO_VENTANA - MARGEN), 
                  (x_base + ANCHO_PICO / 2, ALTO_VENTANA - MARGEN - ALTO_PICO)]
    else:  # Picos superiores
        x_base = MARGEN + ((pico - 12) * ANCHO_PICO)
        if (pico - 12) >= 6:
            x_base += ANCHO_BARRA
            
        puntos = [(x_base, MARGEN), 
                  (x_base + ANCHO_PICO, MARGEN), 
                  (x_base + ANCHO_PICO / 2, MARGEN + ALTO_PICO)]

    pygame.draw.polygon(pantalla, (255, 255, 0, 100), puntos, 5)  # Resaltado amarillo semitransparente

def dibujar_pantalla_inicio(pantalla):
    """
    Muestra una pantalla de inicio simple.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
    """
    fuente = pygame.font.Font(None, 50)
    pantalla.fill(COLOR_FONDO)
    texto = fuente.render("Clic para empezar", True, COLOR_TEXTO)
    rect = texto.get_rect(center=(ANCHO_VENTANA / 2, ALTO_VENTANA / 2))
    pantalla.blit(texto, rect)

def dibujar_pantalla_fin(pantalla, ganador):
    """
    Muestra la pantalla de fin de juego con el nombre del ganador.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
        ganador (Player): El jugador que ha ganado la partida.
    """
    fuente_grande = pygame.font.Font(None, 72)
    fuente_pequeña = pygame.font.Font(None, 36)

    pantalla.fill(COLOR_FONDO)

    texto_ganador = f"¡Ganador: {ganador.nombre()}!"
    sup_ganador = fuente_grande.render(texto_ganador, True, COLOR_TEXTO)
    rect_ganador = sup_ganador.get_rect(center=(ANCHO_VENTANA / 2, ALTO_VENTANA / 2 - 50))
    pantalla.blit(sup_ganador, rect_ganador)

    texto_continuar = "Clic para salir"
    sup_continuar = fuente_pequeña.render(texto_continuar, True, COLOR_TEXTO)
    rect_continuar = sup_continuar.get_rect(center=(ANCHO_VENTANA / 2, ALTO_VENTANA / 2 + 100))
    pantalla.blit(sup_continuar, rect_continuar)


# --- Funciones de Manejo de Eventos ---

def manejar_eventos_jugando(evento, game, board, pico_seleccionado):
    """
    Gestiona los eventos de entrada del usuario durante el estado de juego.

    Procesa los clics del ratón para seleccionar y mover fichas, reingresar
    desde la barra y sacar fichas del tablero.

    Args:
        evento (pygame.event.Event): El evento actual de Pygame.
        game (Game): La instancia actual del juego.
        board (Board): El objeto del tablero.
        pico_seleccionado (int or None): El índice del pico actualmente
                                         seleccionado.

    Returns:
        int or None: El nuevo pico seleccionado, o None si no hay selección.
    """
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if game.jugador_tiene_fichas_en_barra():
            pos_clic = pygame.mouse.get_pos()
            pico = get_pico_desde_pos(pos_clic)
            if pico is not None:
                dado = abs(pico - 24) if game.jugador_actual().color() == "negro" else pico + 1
                try: game.reingresar_desde_barra(dado)
                except Exception as e: print(f"Error: {e}")
        
        elif game.todas_fichas_en_casa():
            pos_clic = pygame.mouse.get_pos()
            pico = get_pico_desde_pos(pos_clic)
            if pico_seleccionado is None and pico is not None:
                if board.get_points()[pico] and board.get_points()[pico][0] == game.jugador_actual().color():
                    return pico # Devuelve el nuevo pico seleccionado
            elif pico_seleccionado is not None:
                origen = pico_seleccionado
                destino = pico
                try: game.mover_ficha(origen, destino)
                except Exception:
                    for dado in game.movimientos_restantes:
                        try:
                            game.sacar_ficha(origen, dado)
                            break
                        except Exception: continue
                return None # Deselecciona el pico
        else:
            pos_clic = pygame.mouse.get_pos()
            pico = get_pico_desde_pos(pos_clic)
            if pico is not None:
                if pico_seleccionado is None:
                    if board.get_points()[pico] and board.get_points()[pico][0] == game.jugador_actual().color():
                        return pico # Devuelve el nuevo pico seleccionado
                else:
                    origen = pico_seleccionado
                    destino = pico
                    try: game.mover_ficha(origen, destino)
                    except Exception as e: print(f"Error: {e}")
                    return None # Deselecciona el pico
    return pico_seleccionado

def dibujar_info_turno(pantalla, game, mensaje_info):
    """
    Muestra información sobre el turno actual, como el jugador y los dados.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
        game (Game): La instancia actual del juego.
        mensaje_info (str): Un mensaje de información adicional para mostrar.
    """
    fuente = pygame.font.Font(None, 36)
    
    # Turno del jugador
    jugador_actual = game.jugador_actual()
    texto_turno = f"Turno de: {jugador_actual.color()}"
    superficie_turno = fuente.render(texto_turno, True, COLOR_TEXTO)
    pantalla.blit(superficie_turno, (MARGEN, ALTO_VENTANA + MARGEN))

    # Dados restantes
    dados = game.movimientos_restantes
    texto_dados = f"Dados: {dados}"
    superficie_dados = fuente.render(texto_dados, True, COLOR_TEXTO)
    pantalla.blit(superficie_dados, (MARGEN, ALTO_VENTANA + MARGEN + 40))

    # Mensaje de información
    if mensaje_info:
        fuente_info = pygame.font.Font(None, 28)
        superficie_info = fuente_info.render(mensaje_info, True, (200, 0, 0)) # Rojo
        pantalla.blit(superficie_info, (ANCHO_VENTANA / 2, ALTO_VENTANA + MARGEN + 60))

def main():
    """
    Función principal que inicia y gestiona el bucle del juego.
    
    Utiliza una máquina de estados simple para controlar el flujo del juego:
    - INICIO: Pantalla inicial, un clic para empezar.
    - JUGANDO: Bucle principal del juego donde se interactúa con el tablero.
    - FIN: Pantalla que muestra al ganador.
    """
    pygame.init()

    # --- Configuración de la ventana ---
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA + 100))
    pygame.display.set_caption("Backgammon")

    # --- Inicialización del juego ---
    p1 = Player("blanco", "Jugador 1", 1)
    p2 = Player("negro", "Jugador 2", -1)
    game = Game(p1, p2)
    board = game.get_board_status()

    # --- Estado del juego ---
    ESTADO = "INICIO"  # INICIO, JUGANDO, FIN
    mensaje_info = ""

    pico_seleccionado = None

    # --- Bucle principal del juego ---
    ejecutando = True
    while ejecutando:
        # --- Gestión de eventos ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            if ESTADO == "INICIO":
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    game.decidir_iniciador()
                    game.lanzar_dados()
                    ESTADO = "JUGANDO"
            
            elif ESTADO == "JUGANDO":
                pico_seleccionado = manejar_eventos_jugando(evento, game, board, pico_seleccionado)

            elif ESTADO == "FIN":
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    ejecutando = False

        # --- Lógica y Dibujo por estado ---
        if ESTADO == "INICIO":
            dibujar_pantalla_inicio(pantalla)
        
        elif ESTADO == "JUGANDO":
            if game and not game.ganador():
                # Lógica de cambio de turno
                if not game.movimientos_restantes:
                    game.cambiar_turno()
                    game.lanzar_dados()
                    mensaje_info = "" # Limpiar mensaje anterior
                    if not game.hay_movimientos_posibles():
                        mensaje_info = "No tienes movimientos. Turno cedido."
                        game.movimientos_restantes = [] # Forzar el cambio en el próximo fotograma
                
                # Dibujo
                dibujar_tablero(pantalla)
                dibujar_fichas(pantalla, board)
                dibujar_seleccion(pantalla, pico_seleccionado)
                dibujar_info_turno(pantalla, game, mensaje_info)
            else:
                ESTADO = "FIN"
        
        elif ESTADO == "FIN":
            if game:
                dibujar_pantalla_fin(pantalla, game.ganador())

        # --- Actualización de la pantalla ---
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()

