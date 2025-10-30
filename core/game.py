"""
Este módulo contiene la clase Game, que orquesta una partida de Backgammon.
"""
from .board import Board
from .checkers import Checkers
from .dice import Dice
from .exceptions import MovimientoInvalido, DadoInvalido, OrigenInvalido


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
            tiro_p1 = self.__dice__.roll_one()
            tiro_p2 = self.__dice__.roll_one()
            if tiro_p1 > tiro_p2:
                self.__turno__ = 0
                return self.__p1__, tiro_p1, tiro_p2
            if tiro_p2 > tiro_p1:
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
            self.__board__,
            self.jugador_actual(),
            origen,
            destino,
            self.movimientos_restantes
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
                if Checkers.puede_reingresar(
                    self.__board__, self.jugador_actual(), dado
                ) is not None:
                    return True
            return False
        return Checkers.hay_movimientos_posibles(
            self.__board__, self.jugador_actual(), self.movimientos_restantes
        )

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
