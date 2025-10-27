import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):

    def test_player_creation(self):
        player = Player("blanco", "p1", +1)
        self.assertEqual(player.nombre(), "p1")
        self.assertEqual(player.color(), "blanco")
        self.assertEqual(player.direccion(), +1)

if __name__ == '__main__':
    unittest.main()