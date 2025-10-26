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
    
    def decidir_iniciador(self):
        """
        Decide quién inicia la partida lanzando un dado (1-6) por cada jugador.
        Si hay empate se repite hasta que haya un ganador.
        Establece self.__turno__ al ganador (0 para p1, 1 para p2) y devuelve
        una tupla (jugador_ganador, tiro_p1, tiro_p2).
        """
        import random
        while True:
            tiro_p1 = random.randint(1, 6)
            tiro_p2 = random.randint(1, 6)
            if tiro_p1 > tiro_p2:
                self.__turno__ = 0
                return (self.__p1__, tiro_p1, tiro_p2)
            elif tiro_p2 > tiro_p1:
                self.__turno__ = 1
                return (self.__p2__, tiro_p1, tiro_p2)
            elif tiro_p1 == tiro_p2:
                continue
            
    def ganador(self, board):
        final = board.get_final()
        p1_color = self.__p1__.color()
        p2_color = self.__p2__.color()

        if len(final.get(p1_color, [])) >= 15:
            return self.__p1__
        if len(final.get(p2_color, [])) >= 15:
            return self.__p2__
        return None