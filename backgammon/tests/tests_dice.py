import unittest
from backgammon.core.dice import Dice

class TestDice(unittest.TestCase):

    def test_valor_inicial(self):
        dado = Dice()
        self.assertEqual(dado.__valor__, [0, 0])

    def test_roll_rango(self):
        dado = Dice()
        valores = dado.roll()
        self.assertTrue(1 <= valores[0] <= 6)
        self.assertTrue(1 <= valores[1] <= 6)

    def test_dobles_true(self):
        dado = Dice()
        dado.__valor__ = [5, 5]
        self.assertTrue(dado.dobles())

    def test_dobles_false(self):
        dado = Dice()
        dado.__valor__ = [2, 6]
        self.assertFalse(dado.dobles())

if __name__ == "__main__":
    unittest.main()