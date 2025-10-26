class MovimientoInvalido(Exception):
    """Excepción para movimientos inválidos en Backgammon."""
    pass

class Checkers:
    @staticmethod
    def es_movimiento_valido(board, jugador, origen, destino, dado):
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
        direccion = jugador.direccion()
        delta = destino - origen
        dado = delta * direccion  # +1/-1 normaliza el signo
        if dado <= 0:
            return None
        return dado if dado in dados else None
    
    @staticmethod
    def mover_y_consumir(board, jugador, origen, destino, dados):
        dado_usado = Checkers.dado_para_movimiento(jugador, origen, destino, dados)
        if dado_usado is None:
            raise MovimientoInvalido("Movimiento incompatible con los dados disponibles.")
        Checkers.mover(board, jugador, origen, destino, dado_usado)
        restantes = dados.copy()
        restantes.remove(dado_usado)  # consume una ocurrencia
        return restantes

    @staticmethod
    def hay_movimientos_posibles(board, jugador, dados):
        puntos = board.get_points()
        color = jugador.color()
        for i in range(24):
            if puntos[i] and puntos[i][0] == color:
                if Checkers.destinos_posibles(board, jugador, i, dados):
                    return True
        return False

    @staticmethod
    def destino_entrada_por_dado(jugador, dado):
        """
        Devuelve el índice de punto donde se intenta entrar desde la barra
        para un dado dado, según la dirección del jugador.
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
        Devuelve el índice destino (int) si es posible, o None si no.
        """
        destino = Checkers.destino_entrada_por_dado(jugador, dado)
        if destino < 0 or destino > 23:
            return None
        puntos = board.get_points()
        color = jugador.color()
        # vacío -> posible
        if not puntos[destino]:
            return destino
        # propio -> posible
        if puntos[destino][0] == color:
            return destino
        # una ficha rival -> posible (captura)
        if len(puntos[destino]) == 1:
            return destino
        # dos o más rivales -> no posible
        return None

    @staticmethod
    def reingresar_desde_bar(board, jugador, dado):
        """
        Ejecuta la entrada desde la barra usando 'dado'. Lanza MovimientoInvalido si no se puede.
        Actualiza board.__bar__ y board.__points__, y realiza captura si corresponde.
        """
        destino = Checkers.puede_reingresar(board, jugador, dado)
        if destino is None:
            raise MovimientoInvalido("No puedes reingresar con ese dado.")
        color = jugador.color()
        bar = board.get_bar()
        puntos = board.get_points()
        # quitar ficha de la barra
        bar[color].pop()
        # captura si hay una ficha rival
        if puntos[destino] and puntos[destino][0] != color and len(puntos[destino]) == 1:
            enemigo_color = puntos[destino].pop()
            bar[enemigo_color].append(enemigo_color)
        # colocar la ficha reingresada
        puntos[destino].append(color)

    @staticmethod
    def todas_en_inicio(board, jugador) -> bool:
        """True si todas las fichas del jugador están en su tablero de casa y no hay fichas en la barra."""
        color = jugador.color()
        direccion = jugador.direccion()
        if board.get_bar().get(color):
            return False
        puntos = board.get_points()
        if direccion == 1:
            # casa = 18..23, fuera de casa = 0..17
            for i in range(0, 18):
                if puntos[i] and puntos[i][0] == color:
                    return False
        else:
            # casa = 0..5, fuera de casa = 6..23
            for i in range(6, 24):
                if puntos[i] and puntos[i][0] == color:
                    return False
        return True

    @staticmethod
    def distancia_desde_origen(board, jugador, origen: int) -> bool:
        color = jugador.color()
        puntos = board.get_points()
        # si el jugador va en direccion 1, la casa es 18-23. "mas lejos" = indice menor
        if jugador.direccion() == 1:
            for i in range(18, origen):
                if puntos[i] and puntos[i][0] == color:
                    return True
        # si el jugador va en direccion -1, la casa es 0-5. "mas lejos" = indice mayor
        else:
            for i in range(origen + 1, 6):
                if puntos[i] and puntos[i][0] == color:
                    return True
        return False
        
    @staticmethod
    def puede_bear_off(board, jugador, origen: int, dado: int) -> bool:
        color = jugador.color()
        puntos = board.get_points()
        # si no estan todas en casa, no se puede
        if not Checkers.todas_en_inicio(board, jugador):
            return False
        # si el origen no es del jugador, no se puede
        if not puntos[origen] or puntos[origen][0] != color:
            return False
        # distancia para salir desde el origen
        distancia = -1
        if jugador.direccion() == 1:
            distancia = 24 - origen
        else:
            distancia = origen + 1
        # si el dado es exacto, se puede
        if dado == distancia:
            return True
        # si el dado es mayor, solo si no hay nadie mas lejos
        if dado > distancia:
            return not Checkers.distancia_desde_origen(board, jugador, origen)
        return False
    
    @staticmethod
    def bear_off(board, jugador, origen: int, dado: int):
        if not Checkers.puede_bear_off(board, jugador, origen, dado):
            raise MovimientoInvalido("No puedes sacar esa ficha con ese dado.")
        color = jugador.color()
        puntos = board.get_points()
        puntos[origen].pop()
        board.increment_final(color)