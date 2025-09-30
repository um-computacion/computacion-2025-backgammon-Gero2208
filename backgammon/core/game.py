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