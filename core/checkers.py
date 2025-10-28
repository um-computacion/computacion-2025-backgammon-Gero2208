from .exceptions import MovimientoInvalido

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
        if not puntos[destino]: return destino
        if puntos[destino][0] == color: return destino
        if len(puntos[destino]) == 1: return destino
        return None

    @staticmethod
    def reingresar_desde_bar(board, jugador, dado):
        """
        Ejecuta la entrada desde la barra usando 'dado'. Lanza MovimientoInvalido si no se puede.
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
        """True si todas las fichas del jugador están en su tablero de casa y no hay fichas en la barra."""
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
        """Función pura que verifica si un movimiento de bear_off es válido sin ejecutarlo."""
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