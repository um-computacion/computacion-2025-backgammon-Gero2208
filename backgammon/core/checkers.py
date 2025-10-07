class MovimientoInvalido(Exception):
    """Excepción para movimientos inválidos en Backgammon."""
    pass

class Checkers:
    @staticmethod
    def es_movimiento_valido(board, jugador, origen, destino, dado):
        color = jugador.color() if callable(jugador.color) else jugador.color
        direccion = jugador.direccion() if callable(jugador.direccion) else jugador.direccion
        puntos = board.__points__
        if origen < 0 or origen > 23 or destino < 0 or destino > 23:
            raise MovimientoInvalido("Origen o destino fuera del tablero.")
        if not puntos[origen] or puntos[origen][0] != color:
            raise MovimientoInvalido("No hay ficha propia en el origen.")
        if destino != origen + direccion * dado:
            raise MovimientoInvalido("El destino no corresponde al dado y dirección.")
    # --- Validación de ocupación en el destino ---
        if puntos[destino]:
            color_destino = puntos[destino][0]
            cantidad = len(puntos[destino])
            if color_destino != color and cantidad > 1:
                raise MovimientoInvalido("No puedes mover a una casilla ocupada por 2 o más fichas rivales.")
    # Si está vacía, o hay fichas propias, o solo una rival, el movimiento es válido

    @staticmethod
    def mover(board, jugador, origen, destino, dado):
        """
        Intenta mover una ficha. Lanza MovimientoInvalido si no es posible.
        """
        Checkers.es_movimiento_valido(board, jugador, origen, destino, dado)
        color = jugador.color() if callable(jugador.color) else jugador.color
        puntos = board.__points__
        puntos[origen].pop()
        puntos[destino].append(color)
        # Aquí puedes agregar lógica para capturas, barra, borne-off, etc.

    @staticmethod
    def destinos_posibles(board, jugador, origen, dados):
        color = jugador.color() if callable(jugador.color) else jugador.color
        direccion = jugador.direccion() if callable(jugador.direccion) else jugador.direccion
        puntos = board.__points__
        destinos = []
        for dado in dados:
            destino = origen + direccion * dado
            if 0 <= destino <= 23:
                try:
                    Checkers.es_movimiento_valido(board, jugador, origen, destino, dado)
                    destinos.append(destino)
                except MovimientoInvalido:
                    continue
        return destinos