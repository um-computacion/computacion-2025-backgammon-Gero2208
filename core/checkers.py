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

    @staticmethod
    def todas_en_inicio(board, jugador) -> bool:
        """True si todas las fichas del jugador están en su tablero de casa y no hay fichas en la barra."""
        color = jugador.color()
        direccion = jugador.direccion()
        # ahora usamos atributos no mangled: bar y points
        if board.bar.get(color):
            return False
        puntos = board.points
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
        """
        Devuelve True si en el tablero de casa hay fichas 'más lejos de salir' que el origen.
        Implementado a propósito con muchos if por claridad didáctica.
        """
        color = jugador.color()
        direccion = jugador.direccion()
        puntos = board.points

        if direccion == 1:
            # casa 18..23, 'más lejos' = índices menores dentro de 18..23
            if origen == 23:
                if (puntos[22] and puntos[22][0] == color): return True
                if (puntos[21] and puntos[21][0] == color): return True
                if (puntos[20] and puntos[20][0] == color): return True
                if (puntos[19] and puntos[19][0] == color): return True
                if (puntos[18] and puntos[18][0] == color): return True
                return False
            if origen == 22:
                if (puntos[21] and puntos[21][0] == color): return True
                if (puntos[20] and puntos[20][0] == color): return True
                if (puntos[19] and puntos[19][0] == color): return True
                if (puntos[18] and puntos[18][0] == color): return True
                return False
            if origen == 21:
                if (puntos[20] and puntos[20][0] == color): return True
                if (puntos[19] and puntos[19][0] == color): return True
                if (puntos[18] and puntos[18][0] == color): return True
                return False
            if origen == 20:
                if (puntos[19] and puntos[19][0] == color): return True
                if (puntos[18] and puntos[18][0] == color): return True
                return False
            if origen == 19:
                if (puntos[18] and puntos[18][0] == color): return True
                return False
            # origen == 18
            return False
        else:
            # direccion == -1, casa 0..5, 'más lejos' = índices mayores dentro de 0..5
            if origen == 0:
                if (puntos[1] and puntos[1][0] == color): return True
                if (puntos[2] and puntos[2][0] == color): return True
                if (puntos[3] and puntos[3][0] == color): return True
                if (puntos[4] and puntos[4][0] == color): return True
                if (puntos[5] and puntos[5][0] == color): return True
                return False
            if origen == 1:
                if (puntos[2] and puntos[2][0] == color): return True
                if (puntos[3] and puntos[3][0] == color): return True
                if (puntos[4] and puntos[4][0] == color): return True
                if (puntos[5] and puntos[5][0] == color): return True
                return False
            if origen == 2:
                if (puntos[3] and puntos[3][0] == color): return True
                if (puntos[4] and puntos[4][0] == color): return True
                if (puntos[5] and puntos[5][0] == color): return True
                return False
            if origen == 3:
                if (puntos[4] and puntos[4][0] == color): return True
                if (puntos[5] and puntos[5][0] == color): return True
                return False
            if origen == 4:
                if (puntos[5] and puntos[5][0] == color): return True
                return False
            # origen == 5
            return False
        
    @staticmethod
    def puede_bear_off(board, jugador, origen: int, dado: int) -> bool:
        """
        Devuelve True si puede 'salir' (bear-off) una ficha desde 'origen' usando ese dado.
        Implementación intencionalmente con muchos if por posición y dado.
        Reglas:
        - Debes tener todas las fichas en la casa y nada en la barra.
        - Si el dado coincide exactamente con la distancia a salir, puedes salir.
        - Si el dado es mayor, solo puedes usarlo si no hay fichas más lejos en la casa.
        """
        color = jugador.color()
        direccion = jugador.direccion()
        puntos = board.points

        # validaciones básicas
        if not (0 <= origen <= 23):
            return False
        if not puntos[origen] or puntos[origen][0] != color:
            return False
        if not (1 <= dado <= 6):
            return False
        if not Checkers._all_in_home(board, jugador):
            return False

        # Lógica por dirección con muchos ifs
        if direccion == 1:
            # Casa 18..23, distancia = 24 - origen
            if origen < 18 or origen > 23:
                return False

            # origen 23 -> distancia 1
            if origen == 23:
                if dado == 1:
                    return True
                if dado in (2, 3, 4, 5, 6):
                    # permitido si no hay más lejos (22..18)
                    return not Checkers._hay_mas_lejos_en_home_if(board, jugador, 23)
                return False

            # origen 22 -> distancia 2
            if origen == 22:
                if dado == 2:
                    return True
                if dado in (3, 4, 5, 6):
                    return not Checkers._hay_mas_lejos_en_home_if(board, jugador, 22)
                return False

            # origen 21 -> distancia 3
            if origen == 21:
                if dado == 3:
                    return True
                if dado in (4, 5, 6):
                    return not Checkers._hay_mas_lejos_en_home_if(board, jugador, 21)
                return False

            # origen 20 -> distancia 4
            if origen == 20:
                if dado == 4:
                    return True
                if dado in (5, 6):
                    return not Checkers._hay_mas_lejos_en_home_if(board, jugador, 20)
                return False

            # origen 19 -> distancia 5
            if origen == 19:
                if dado == 5:
                    return True
                if dado == 6:
                    return not Checkers._hay_mas_lejos_en_home_if(board, jugador, 19)
                return False

            # origen 18 -> distancia 6
            if origen == 18:
                if dado == 6:
                    return True
                return False

            return False
        else:
            # direccion == -1, Casa 0..5, distancia = origen + 1
            if origen < 0 or origen > 5:
                return False

            # origen 0 -> distancia 1
            if origen == 0:
                if dado == 1:
                    return True
                if dado in (2, 3, 4, 5, 6):
                    return not Checkers._hay_mas_lejos_en_home_if(board, jugador, 0)
                return False

            # origen 1 -> distancia 2
            if origen == 1:
                if dado == 2:
                    return True
                if dado in (3, 4, 5, 6):
                    return not Checkers._hay_mas_lejos_en_home_if(board, jugador, 1)
                return False

            # origen 2 -> distancia 3
            if origen == 2:
                if dado == 3:
                    return True
                if dado in (4, 5, 6):
                    return not Checkers._hay_mas_lejos_en_home_if(board, jugador, 2)
                return False

            # origen 3 -> distancia 4
            if origen == 3:
                if dado == 4:
                    return True
                if dado in (5, 6):
                    return not Checkers._hay_mas_lejos_en_home_if(board, jugador, 3)
                return False

            # origen 4 -> distancia 5
            if origen == 4:
                if dado == 5:
                    return True
                if dado == 6:
                    return not Checkers._hay_mas_lejos_en_home_if(board, jugador, 4)
                return False

            # origen 5 -> distancia 6
            if origen == 5:
                if dado == 6:
                    return True
                return False

            return False
    
    @staticmethod
    def bear_off(board, jugador, origen: int, dado: int):
        """
        Ejecuta la salida desde 'origen' usando 'dado'.
        Lanza MovimientoInvalido si no es legal según puede_bear_off_con_dado.
        Actualiza board.points y board.off.
        """
        if not Checkers.puede_bear_off_con_dado(board, jugador, origen, dado):
            raise MovimientoInvalido("No puedes sacar esa ficha con ese dado.")
        color = jugador.color()
        puntos = board.points

        # quitar una ficha del origen
        if not puntos[origen] or puntos[origen][0] != color:
            raise MovimientoInvalido("No hay ficha propia en el origen para salir.")
        puntos[origen].pop()

        # se asume que board.off ya existe y es un dict con claves 'blanco' y 'negro'
        board.off[color] = board.off.get(color, 0) + 1
        # no devuelve nada; si quieres consumir el dado fuera, hazlo en la capa que coordina los dados