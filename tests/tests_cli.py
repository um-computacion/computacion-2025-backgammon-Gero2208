import unittest
from cli.cli import procesar_turno
from core.game import Game
from core.player import Player

class TestCli(unittest.TestCase):

    def setUp(self):
        self.p1 = Player("blanco", "p1", +1)
        self.p2 = Player("negro", "p2", -1)
        self.game = Game(self.p1, self.p2)
        self.game.movimientos_restantes = [1, 2, 3, 4]

    def test_procesar_turno_movimiento_normal(self):
        # Configurar el tablero para un movimiento simple
        self.game.get_board_status().get_points()[0] = [self.p1.color()]
        self.assertTrue(procesar_turno(self.game, "mover 1 2"))
        self.assertEqual(len(self.game.get_board_status().get_points()[0]), 0)
        self.assertIn(self.p1.color(), self.game.get_board_status().get_points()[1])

    def test_procesar_turno_reingresar(self):
        # Poner una ficha en la barra
        self.game.get_board_status().get_bar()[self.p1.color()].append(self.p1.color())
        self.assertTrue(procesar_turno(self.game, "reingresar 1"))
        self.assertFalse(self.game.get_board_status().get_bar()[self.p1.color()])
        self.assertIn(self.p1.color(), self.game.get_board_status().get_points()[0])

    def test_procesar_turno_sacar_ficha(self):
        # Limpiar el tablero y poner todas las fichas del p1 en casa
        self.game.get_board_status().get_points().clear()
        self.game.get_board_status().get_points().extend([[] for _ in range(24)])
        for i in range(18, 24):
            self.game.get_board_status().get_points()[i] = [self.p1.color()]
        
        self.game.movimientos_restantes = [1]
        self.assertTrue(procesar_turno(self.game, "sacar 24 1"))
        
        # Verificar que la ficha fue sacada
        self.assertEqual(len(self.game.get_board_status().get_points()[23]), 0)
        self.assertEqual(len(self.game.get_board_status().get_final()[self.p1.color()]), 1)

    def test_procesar_turno_comando_invalido(self):
        self.assertFalse(procesar_turno(self.game, "comando_invalido"))
        self.assertFalse(procesar_turno(self.game, "mover 1"))
        self.assertFalse(procesar_turno(self.game, "mover 1 2 3"))

if __name__ == '__main__':
    unittest.main()
