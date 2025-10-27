from .player import Player
from .board import Board
from .dice import Dice
from .checkers import Checkers
from .exceptions import MovimientoInvalido, DadoInvalido, OrigenInvalido
import random

class Game:
    """
    Clase que gestiona la lógica y el estado de una partida de Backgammon.
    """

    def __init__(self, p1, p2):
        self.__p1__ = p1
        self.__p2__ = p2
        self.__turno__ = 0
        self.__board__ = Board()
        self.__board__.setup(p1.color(), p2.color())
        self.__dice__ = Dice()
        self.movimientos_restantes = []

    def decidir_iniciador(self):
        """
        Decide quién inicia la partida lanzando un dado por cada jugador.
        Si hay empate, se repite.
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
        """Devuelve el jugador cuyo turno es actualmente."""
        return self.__p1__ if self.__turno__ == 0 else self.__p2__

    def cambiar_turno(self):
        """Alterna el turno entre los dos jugadores."""
        self.__turno__ = 1 - self.__turno__
        self.movimientos_restantes = []

    def lanzar_dados(self):
        """Lanza los dados y devuelve los movimientos disponibles."""
        self.__dice__.roll()
        self.movimientos_restantes = self.__dice__.duplicar()
        return self.movimientos_restantes

    def mover_ficha(self, origen, destino):
        """
        Mueve una ficha y consume el dado utilizado.
        Lanza MovimientoInvalido si el movimiento no es válido.
        """
        self.movimientos_restantes = Checkers.mover_y_consumir(
            self.__board__, self.jugador_actual(), origen, destino, self.movimientos_restantes
        )

    def get_board_status(self):
        """Devuelve una representación del estado actual del tablero."""
        return self.__board__

    def hay_movimientos_posibles(self):
        """Comprueba si el jugador actual tiene algún movimiento posible con los dados restantes."""
        if self.jugador_tiene_fichas_en_barra():
             for dado in self.movimientos_restantes:
                 if Checkers.puede_reingresar(self.__board__, self.jugador_actual(), dado) is not None:
                     return True
             return False
        return Checkers.hay_movimientos_posibles(self.__board__, self.jugador_actual(), self.movimientos_restantes)

    def jugador_tiene_fichas_en_barra(self):
        """Comprueba si el jugador actual tiene fichas en la barra."""
        color_actual = self.jugador_actual().color()
        return self.__board__.get_bar().get(color_actual, [])

    def posibles_entradas_desde_barra(self):
        """Devuelve una lista de tuplas (dado, destino) para reingresar desde la barra."""
        entradas = []
        for dado in self.movimientos_restantes:
            destino = Checkers.puede_reingresar(self.__board__, self.jugador_actual(), dado)
            if destino is not None:
                entradas.append((dado, destino))
        return entradas

    def reingresar_desde_barra(self, dado):
        """
        Reingresa una ficha desde la barra utilizando el dado especificado.
        Lanza DadoInvalido si el dado no es válido, o MovimientoInvalido si no es posible.
        """
        if dado not in self.movimientos_restantes:
            raise DadoInvalido("No tienes ese dado disponible.")
        
        Checkers.reingresar_desde_bar(self.__board__, self.jugador_actual(), dado)
        self.movimientos_restantes.remove(dado)

    def todas_fichas_en_casa(self):
        """Comprueba si todas las fichas del jugador actual están en su tablero de casa."""
        return Checkers.todas_en_inicio(self.__board__, self.jugador_actual())

    def sacar_ficha(self, origen, dado):
        """
        Saca una ficha del tablero (bear off).
        Lanza DadoInvalido si el dado no es válido, o MovimientoInvalido si no es posible.
        """
        if dado not in self.movimientos_restantes:
            raise DadoInvalido("No tienes ese dado disponible.")
        
        Checkers.bear_off(self.__board__, self.jugador_actual(), origen, dado)
        self.movimientos_restantes.remove(dado)

    def validar_origen_y_obtener_destinos(self, origen):
        """
        Valida un punto de origen y devuelve los destinos posibles.
        Lanza OrigenInvalido si no hay movimientos posibles desde el origen.
        """
        destinos = Checkers.destinos_posibles(self.__board__, self.jugador_actual(), origen, self.movimientos_restantes)
        if not destinos:
            raise OrigenInvalido(f"No hay movimientos posibles desde la casilla {origen + 1} con los dados actuales.")
        return destinos

    def ganador(self):
        """Comprueba si hay un ganador en la partida."""
        final = self.__board__.get_final()
        p1_color = self.__p1__.color()
        p2_color = self.__p2__.color()

        if len(final.get(p1_color, [])) >= 15:
            return self.__p1__
        if len(final.get(p2_color, [])) >= 15:
            return self.__p2__
        return None