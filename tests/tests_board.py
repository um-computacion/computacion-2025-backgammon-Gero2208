"""
Este módulo contiene las pruebas unitarias para la clase Board.
"""
import unittest
from core.board import Board


class TestBoard(unittest.TestCase):
    """
    Pruebas para la clase Board.
    """

    def test_board_initialization(self):
        """
        Prueba que el tablero se inicializa correctamente.
        """
        board = Board()
        self.assertEqual(len(board.get_points()), 24)
        self.assertTrue(all(p == [] for p in board.get_points()))
        self.assertEqual(board.get_bar(), {"blanco": [], "negro": []})
        self.assertEqual(board.get_final(), {"blanco": [], "negro": []})

    def test_board_setup(self):
        """
        Prueba que el tablero se configura correctamente con la disposición inicial.
        """
        board = Board()
        board.setup("blanco", "negro")

        # Puntos con fichas blancas
        self.assertEqual(board.get_points()[0], ["blanco"] * 2)
        self.assertEqual(board.get_points()[11], ["blanco"] * 5)
        self.assertEqual(board.get_points()[16], ["blanco"] * 3)
        self.assertEqual(board.get_points()[18], ["blanco"] * 5)

        # Puntos con fichas negras
        self.assertEqual(board.get_points()[23], ["negro"] * 2)
        self.assertEqual(board.get_points()[12], ["negro"] * 5)
        self.assertEqual(board.get_points()[7], ["negro"] * 3)
        self.assertEqual(board.get_points()[5], ["negro"] * 5)

        # Puntos vacíos
        puntos_vacios = [1, 2, 3, 4, 6, 8, 9, 10, 13, 14, 15, 17, 19, 20, 21, 22]
        for p in puntos_vacios:
            self.assertFalse(board.get_points()[p])

    def test_increment_final(self):
        """
        Prueba que se pueden añadir fichas a la zona final correctamente.
        """
        board = Board()
        board.increment_final("blanco")
        self.assertEqual(board.get_final()["blanco"], ["blanco"])
        board.increment_final("blanco")
        self.assertEqual(board.get_final()["blanco"], ["blanco", "blanco"])
        board.increment_final("negro")
        self.assertEqual(board.get_final()["negro"], ["negro"])


if __name__ == '__main__':
    unittest.main()
