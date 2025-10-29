"""
Este módulo contiene las pruebas unitarias para la clase Player.
"""
import unittest
from core.player import Player


class TestPlayer(unittest.TestCase):
    """
    Pruebas para la clase Player.
    """

    def test_player_creation(self):
        """
        Prueba que un jugador se crea con los atributos correctos.
        """
        player = Player("blanco", "p1", +1)
        self.assertEqual(player.nombre(), "p1")
        self.assertEqual(player.color(), "blanco")
        self.assertEqual(player.direccion(), +1)


if __name__ == '__main__':
    unittest.main()
