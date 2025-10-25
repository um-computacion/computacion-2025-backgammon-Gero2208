## Prompt

### Haz tests de mis actuales métodos de la clase Dice

## Response

import unittest
from dice import Dice

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

## Prompt

### Haz tests para la clase Board

## Response

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

## Prompt

### Haz tests para la clase Game

## Response

import unittest
from backgammon.core.game import Game

class DummyPlayer:
    def __init__(self, nombre):
        self.nombre = nombre

class TestGame(unittest.TestCase):

    def setUp(self):
        self.p1 = DummyPlayer("Jugador1")
        self.p2 = DummyPlayer("Jugador2")
        self.game = Game(self.p1, self.p2)

    def test_turno_inicial(self):
        # El turno inicial debe ser del primer jugador
        self.assertIs(self.game.jugador_actual(), self.p1)

    def test_cambiar_turno(self):
        # Después de cambiar turno, debe ser el segundo jugador
        self.game.cambiar_turno()
        self.assertIs(self.game.jugador_actual(), self.p2)

    def test_alternar_turnos(self):
        # Alterna varias veces y verifica el jugador actual
        self.assertIs(self.game.jugador_actual(), self.p1)
        self.game.cambiar_turno()
        self.assertIs(self.game.jugador_actual(), self.p2)
        self.game.cambiar_turno()
        self.assertIs(self.game.jugador_actual(), self.p1)

    if __name__ == "__main__":
        unittest.main()
    
¿Qué hace cada test?

test_turno_inicial: Verifica que el turno inicial es del primer jugador.
test_cambiar_turno: Verifica que después de cambiar turno, es el segundo jugador.
test_alternar_turnos: Alterna varias veces y verifica que los turnos se alternan correctamente.