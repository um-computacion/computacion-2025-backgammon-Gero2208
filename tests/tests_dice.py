"""
Este módulo contiene las pruebas unitarias para la clase Dice.
"""
import unittest
from core.dice import Dice


class TestDice(unittest.TestCase):
    """
    Pruebas para la clase Dice.
    """

    def test_dice_roll(self):
        """
        Prueba que el lanzamiento de los dados devuelve dos valores entre 1 y 6.
        """
        dice = Dice()
        values = dice.roll()
        self.assertEqual(len(values), 2)
        self.assertTrue(all(1 <= v <= 6 for v in values))

    def test_dice_doubles(self):
        """
        Prueba que la detección de dobles funciona correctamente.
        """
        dice = Dice()
        dice.set_valor([1, 1])
        self.assertTrue(dice.dobles())
        dice.set_valor([1, 2])
        self.assertFalse(dice.dobles())

    def test_dice_duplicar(self):
        """
        Prueba que los valores de los dados se duplican correctamente cuando son dobles.
        """
        dice = Dice()
        dice.set_valor([1, 1])
        self.assertEqual(dice.duplicar(), [1, 1, 1, 1])
        dice.set_valor([1, 2])
        self.assertEqual(dice.duplicar(), [1, 2])


if __name__ == '__main__':
    unittest.main()
