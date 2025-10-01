import unittest
from backgammon.core.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board.setup("blanco", "negro")

    def test_setup_fichas_blanco(self):
        self.assertEqual(self.board.__points__[0], ["blanco"] * 2)
        self.assertEqual(self.board.__points__[11], ["blanco"] * 5)
        self.assertEqual(self.board.__points__[16], ["blanco"] * 3)
        self.assertEqual(self.board.__points__[18], ["blanco"] * 5)

    def test_setup_fichas_negro(self):
        self.assertEqual(self.board.__points__[23], ["negro"] * 2)
        self.assertEqual(self.board.__points__[12], ["negro"] * 5)
        self.assertEqual(self.board.__points__[7], ["negro"] * 3)
        self.assertEqual(self.board.__points__[5], ["negro"] * 5)

    def test_barra_vacia(self):
        self.assertEqual(self.board.__bar__["blanco"], [])
        self.assertEqual(self.board.__bar__["negro"], [])

    def test_final_vacio(self):
        self.assertEqual(self.board.__final__["blanco"], [])
        self.assertEqual(self.board.__final__["negro"], [])

if __name__ == "__main__":
    unittest.main()