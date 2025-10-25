import unittest
from core.game import Game

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