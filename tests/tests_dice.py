import unittest
from core.dice import Dice

class TestDice(unittest.TestCase):

    def test_dice_roll(self):
        dice = Dice()
        values = dice.roll()
        self.assertEqual(len(values), 2)
        self.assertTrue(all(1 <= v <= 6 for v in values))

    def test_dice_doubles(self):
        dice = Dice()
        dice.set_valor([1, 1])
        self.assertTrue(dice.dobles())
        dice.set_valor([1, 2])
        self.assertFalse(dice.dobles())

    def test_dice_duplicar(self):
        dice = Dice()
        dice.set_valor([1, 1])
        self.assertEqual(dice.duplicar(), [1, 1, 1, 1])
        dice.set_valor([1, 2])
        self.assertEqual(dice.duplicar(), [1, 2])

if __name__ == '__main__':
    unittest.main()