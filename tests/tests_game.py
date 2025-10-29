"""
Este módulo contiene las pruebas unitarias para la clase Game.
"""
import unittest
from core.game import Game
from core.player import Player


class TestGame(unittest.TestCase):
    """
    Pruebas para la clase Game.
    """

    def setUp(self):
        """
        Configura un nuevo juego para cada prueba.
        """
        self.p1 = Player("blanco", "p1", +1)
        self.p2 = Player("negro", "p2", -1)
        self.game = Game(self.p1, self.p2)

    def test_decidir_iniciador(self):
        """
        Prueba que se decide un iniciador válido.
        """
        iniciador, _, _ = self.game.decidir_iniciador()
        self.assertIn(iniciador, (self.p1, self.p2))

    def test_jugador_actual(self):
        """
        Prueba que el jugador actual es uno de los dos jugadores.
        """
        # El iniciador se decide aleatoriamente, por lo que el jugador actual puede ser cualquiera
        self.assertIn(self.game.jugador_actual(), (self.p1, self.p2))

    def test_cambiar_turno(self):
        """
        Prueba que el turno se cambia correctamente entre los jugadores.
        """
        jugador_inicial = self.game.jugador_actual()
        self.game.cambiar_turno()
        self.assertNotEqual(self.game.jugador_actual(), jugador_inicial)
        self.game.cambiar_turno()
        self.assertEqual(self.game.jugador_actual(), jugador_inicial)

    def test_lanzar_dados(self):
        """
        Prueba que el lanzamiento de dados devuelve un resultado válido.
        """
        movimientos = self.game.lanzar_dados()
        self.assertIn(len(movimientos), (2, 4))
        self.assertTrue(all(1 <= m <= 6 for m in movimientos))

    def test_ganador(self):
        """
        Prueba que se detecta correctamente al ganador.
        """
        for _ in range(15):
            self.game.get_board_status().increment_final(self.p1.color())
        self.assertEqual(self.game.ganador(), self.p1)


if __name__ == '__main__':
    unittest.main()
