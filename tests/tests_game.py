"""
Este módulo contiene las pruebas unitarias para la clase Game.
"""
import unittest
from core.game import Game
from core.player import Player
from core.exceptions import DadoInvalido, OrigenInvalido


class TestGame(unittest.TestCase):
    """
    Pruebas para la clase Game.
    """

    def setUp(self):
        """
        Configura un nuevo juego para cada prueba.
        """
        self.p1 = Player("blanco", "p1", +1)
        self.p2 = Player("negro", "p2", -1)
        self.game = Game(self.p1, self.p2)

    def test_decidir_iniciador(self):
        """
        Prueba que se decide un iniciador válido.
        """
        # --- Caso normal ---
        iniciador, _, _ = self.game.decidir_iniciador()
        self.assertIn(iniciador, (self.p1, self.p2))

        # --- Caso con empate ---
        # Sobrescribir roll_one para simular un empate y luego un desempate
        # La función se llamará 4 veces: 3, 3 (empate), 5, 2 (desempate)
        valores = [3, 3, 5, 2]
        def mock_roll_one():
            return valores.pop(0)

        self.game.__dice__.roll_one = mock_roll_one

        iniciador, tiro_p1, tiro_p2 = self.game.decidir_iniciador()

        # El ganador del desempate (5 vs 2) debe ser p1
        self.assertEqual(iniciador, self.p1)
        self.assertEqual(tiro_p1, 5)
        self.assertEqual(tiro_p2, 2)

    def test_jugador_actual(self):
        """
        Prueba que el jugador actual es uno de los dos jugadores.
        """
        # El iniciador se decide aleatoriamente, por lo que el jugador actual puede ser cualquiera
        self.assertIn(self.game.jugador_actual(), (self.p1, self.p2))

    def test_cambiar_turno(self):
        """
        Prueba que el turno se cambia correctamente entre los jugadores.
        """
        jugador_inicial = self.game.jugador_actual()
        self.game.cambiar_turno()
        self.assertNotEqual(self.game.jugador_actual(), jugador_inicial)
        self.game.cambiar_turno()
        self.assertEqual(self.game.jugador_actual(), jugador_inicial)

    def test_lanzar_dados(self):
        """
        Prueba que el lanzamiento de dados devuelve un resultado válido.
        """
        movimientos = self.game.lanzar_dados()
        self.assertIn(len(movimientos), (2, 4))
        self.assertTrue(all(1 <= m <= 6 for m in movimientos))

    def test_hay_movimientos_posibles(self):
        """
        Prueba la detección de movimientos posibles con fichas en la barra.
        """
        # --- Fichas en la barra con reingreso posible ---
        self.game.get_board_status().get_bar()[self.p1.color()].append(self.p1.color())
        self.game.movimientos_restantes = [1, 2]
        self.assertTrue(self.game.hay_movimientos_posibles())

        # --- Fichas en la barra sin reingreso posible ---
        # Bloquear los puntos de entrada 1 y 2
        self.game.get_board_status().get_points()[0] = [self.p2.color()] * 2
        self.game.get_board_status().get_points()[1] = [self.p2.color()] * 2
        self.assertFalse(self.game.hay_movimientos_posibles())

    def test_posibles_entradas_desde_barra(self):
        """
        Prueba que se calculan correctamente las entradas posibles.
        """
        self.game.get_board_status().get_bar()[self.p1.color()].append(self.p1.color())
        self.game.movimientos_restantes = [1, 3]
        # Bloquear la entrada con el dado 3
        self.game.get_board_status().get_points()[2] = [self.p2.color()] * 2

        entradas = self.game.posibles_entradas_desde_barra()

        self.assertEqual(len(entradas), 1)
        self.assertEqual(entradas[0], (1, 0)) # dado 1 -> destino 0

    def test_reingresar_desde_barra_dado_invalido(self):
        """
        Prueba que reingresar con un dado inválido lanza una excepción.
        """
        self.game.get_board_status().get_bar()[self.p1.color()].append(self.p1.color())
        self.game.movimientos_restantes = [1, 2]
        with self.assertRaises(DadoInvalido):
            self.game.reingresar_desde_barra(3)

    def test_sacar_ficha_dado_invalido(self):
        """
        Prueba que sacar ficha con un dado inválido lanza una excepción.
        """
        # Preparar el tablero para que el bear off sea legal
        for i in range(18, 24):
            self.game.get_board_status().get_points()[i] = [self.p1.color()]
        self.game.movimientos_restantes = [1, 2]
        with self.assertRaises(DadoInvalido):
            self.game.sacar_ficha(23, 3)

    def test_validar_origen_sin_movimientos(self):
        """
        Prueba que validar un origen sin movimientos lanza una excepción.
        """
        # Configurar un escenario sin movimientos posibles desde el origen 0
        self.game.movimientos_restantes = [1]
        self.game.get_board_status().get_points()[1] = [self.p2.color()] * 2
        with self.assertRaises(OrigenInvalido):
            self.game.validar_origen_y_obtener_destinos(0)

    def test_ganador(self):
        """
        Prueba que se detecta correctamente al ganador.
        """
        # --- Gana el Jugador 1 ---
        for _ in range(15):
            self.game.get_board_status().increment_final(self.p1.color())
        self.assertEqual(self.game.ganador(), self.p1)

        # --- Resetear y probar que gana el Jugador 2 ---
        self.setUp() # Reinicia el juego
        for _ in range(15):
            self.game.get_board_status().increment_final(self.p2.color())
        self.assertEqual(self.game.ganador(), self.p2)

        # --- No hay ganador ---
        self.setUp() # Reinicia el juego
        self.assertIsNone(self.game.ganador())


if __name__ == '__main__':
    unittest.main()
