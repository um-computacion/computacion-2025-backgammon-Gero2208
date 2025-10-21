class MovimientoInvalido(Exception):
    """Excepción para movimientos inválidos en Backgammon."""
    pass

class Checkers:
    @staticmethod
    def es_movimiento_valido(board, jugador, origen, destino, dado):
        color = jugador.color()
        direccion = jugador.direccion()
        puntos = board.__points__
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
        puntos = board.__points__

        # captura: si en destino hay 1 ficha y es rival -> enviarla a la barra
        if puntos[destino] and puntos[destino][0] != color and len(puntos[destino]) == 1:
            enemigo_color = puntos[destino].pop()
            board.__bar__[enemigo_color].append(enemigo_color)

        # mover la ficha desde origen a destino
        puntos[origen].pop()
        puntos[destino].append(color)

    @staticmethod
    def destinos_posibles(board, jugador, origen, dados):
        color = jugador.color()
        direccion = jugador.direccion()
        puntos = board.__points__
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
        puntos = board.__points__
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
        puntos = board.__points__
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
        # quitar ficha de la barra
        board.__bar__[color].pop()
        # captura si hay una ficha rival
        if board.__points__[destino] and board.__points__[destino][0] != color and len(board.__points__[destino]) == 1:
            enemigo_color = board.__points__[destino].pop()
            board.__bar__[enemigo_color].append(enemigo_color)
        # colocar la ficha reingresada
        board.__points__[destino].append(color)