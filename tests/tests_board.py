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

    def test_mostrar_tablero_cli_empty(self):
        """
        Prueba que la salida de un tablero vacío es correcta.
        """
        board = Board()
        output = board.mostrar_tablero_cli()
        self.assertIn("Barra: Blanco=0 Negro=0 | Final: Blanco=0 Negro=0", output)
        self.assertIn("   13 14 15 16 17 18  19 20 21 22 23 24", output)
        self.assertIn("   12 11 10  9  8  7   6  5  4  3  2  1", output)

    def test_mostrar_tablero_cli_setup(self):
        """
        Prueba que la salida de un tablero recién configurado es correcta.
        """
        board = Board()
        board.setup("blanco", "negro")
        output = board.mostrar_tablero_cli()
        self.assertIn("Barra: Blanco=0 Negro=0 | Final: Blanco=0 Negro=0", output)
        # Verificamos la presencia de algunos contadores de fichas
        self.assertIn("○", output)
        self.assertIn("●", output)

    def test_mostrar_tablero_cli_full_column(self):
        """
        Prueba que una columna con más de 5 fichas muestra el contador 'xN'.
        """
        board = Board()
        board.get_points()[0] = ["blanco"] * 6
        output = board.mostrar_tablero_cli()
        self.assertIn("×6", output)


if __name__ == '__main__':
    unittest.main()
