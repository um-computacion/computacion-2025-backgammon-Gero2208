"""
Este módulo contiene las pruebas unitarias para la clase Checkers.
"""
import unittest
from core.board import Board
from core.checkers import Checkers
from core.player import Player
from core.exceptions import MovimientoInvalido


class TestCheckers(unittest.TestCase):
    """
    Pruebas para la clase Checkers.
    """

    def setUp(self):
        """
        Configura un nuevo tablero y jugadores para cada prueba.
        """
        self.board = Board()
        self.p1 = Player("blanco", "p1", +1)
        self.p2 = Player("negro", "p2", -1)

    def test_es_movimiento_valido(self):
        """
        Prueba la validación de movimientos.
        """
        self.board.setup(self.p1.color(), self.p2.color())
        # Movimiento válido
        Checkers.es_movimiento_valido(self.board, self.p1, 0, 1, 1)
        # Origen sin ficha
        with self.assertRaises(MovimientoInvalido):
            Checkers.es_movimiento_valido(self.board, self.p1, 1, 2, 1)
        # Destino ocupado por más de una ficha rival
        with self.assertRaises(MovimientoInvalido):
            Checkers.es_movimiento_valido(self.board, self.p1, 0, 5, 5)
        # Origen o destino fuera del tablero
        with self.assertRaises(MovimientoInvalido):
            Checkers.es_movimiento_valido(self.board, self.p1, -1, 1, 2)
        with self.assertRaises(MovimientoInvalido):
            Checkers.es_movimiento_valido(self.board, self.p1, 0, 24, 24)
        # El destino no corresponde al dado
        with self.assertRaises(MovimientoInvalido):
            Checkers.es_movimiento_valido(self.board, self.p1, 0, 2, 1)

    def test_mover(self):
        """
        Prueba el movimiento de fichas, incluyendo capturas.
        """
        self.board.setup(self.p1.color(), self.p2.color())
        # Movimiento simple
        Checkers.mover(self.board, self.p1, 0, 1, 1)
        self.assertEqual(len(self.board.get_points()[0]), 1)
        self.assertEqual(self.board.get_points()[1], [self.p1.color()])
        # Captura
        self.board.get_points()[4] = [self.p2.color()]
        Checkers.mover(self.board, self.p1, 0, 4, 4)
        self.assertEqual(len(self.board.get_points()[0]), 0)
        self.assertEqual(self.board.get_points()[4], [self.p1.color()])
        self.assertEqual(self.board.get_bar()[self.p2.color()], [self.p2.color()])

    def test_destinos_posibles(self):
        """
        Prueba que se calculan correctamente los destinos posibles.
        """
        self.board.setup(self.p1.color(), self.p2.color())
        destinos = Checkers.destinos_posibles(self.board, self.p1, 0, [1, 2, 3])
        self.assertIn(1, destinos)
        self.assertIn(2, destinos)
        self.assertIn(3, destinos)

    def test_dado_para_movimiento(self):
        """
        Prueba la obtención del dado correspondiente a un movimiento.
        """
        self.assertEqual(Checkers.dado_para_movimiento(self.p1, 0, 1, [1, 2]), 1)
        self.assertEqual(Checkers.dado_para_movimiento(self.p1, 0, 2, [1, 2]), 2)
        self.assertIsNone(Checkers.dado_para_movimiento(self.p1, 0, 3, [1, 2]))
        # Movimiento en dirección contraria
        self.assertIsNone(Checkers.dado_para_movimiento(self.p1, 1, 0, [1]))

    def test_mover_y_consumir(self):
        """
        Prueba que el movimiento de una ficha consume el dado correcto.
        """
        self.board.setup(self.p1.color(), self.p2.color())
        dados = [1, 2]
        dados_restantes = Checkers.mover_y_consumir(self.board, self.p1, 0, 1, dados)
        self.assertEqual(dados_restantes, [2])
        # Dado no disponible
        with self.assertRaises(MovimientoInvalido):
            Checkers.mover_y_consumir(self.board, self.p1, 0, 3, dados)

    def test_hay_movimientos_posibles(self):
        """
        Prueba la detección de movimientos posibles.
        """
        self.board.setup(self.p1.color(), self.p2.color())
        self.assertTrue(Checkers.hay_movimientos_posibles(self.board, self.p1, [1, 2]))
        # Limpiar el tablero y crear una situación sin movimientos posibles
        for i in range(24):
            if self.p1.color() in self.board.get_points()[i]:
                self.board.get_points()[i] = []
        self.board.get_points()[0] = [self.p1.color()]
        self.board.get_points()[1] = [self.p2.color()] * 2
        self.assertFalse(Checkers.hay_movimientos_posibles(self.board, self.p1, [1]))
        
        # Caso donde solo es posible hacer bear off
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        self.board.get_points()[23] = [self.p1.color()]
        self.assertTrue(Checkers.hay_movimientos_posibles(self.board, self.p1, [1, 2]))

        # Pruebas para el jugador 2 (negro)
        self.board.setup(self.p1.color(), self.p2.color())
        self.assertTrue(Checkers.hay_movimientos_posibles(self.board, self.p2, [1, 2]))
        # Bloquear todos los movimientos posibles para el jugador 2 con un dado de 1
        # Fichas de p2 en: 23, 12, 7, 5. Destinos con dado 1: 22, 11, 6, 4
        self.board.get_points()[22] = [self.p1.color()] * 2 # Bloquea el movimiento desde 23
        self.board.get_points()[6] = [self.p1.color()] * 2  # Bloquea el movimiento desde 7
        self.board.get_points()[4] = [self.p1.color()] * 2  # Bloquea el movimiento desde 5
        # El punto 11 ya está bloqueado por la configuración inicial
        self.assertFalse(Checkers.hay_movimientos_posibles(self.board, self.p2, [1]))

        # Movimiento posible solo con bear off (jugador 2)
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        self.board.get_points()[0] = [self.p2.color()]
        self.board.get_points()[2] = [self.p1.color()] * 2 # Bloquea movimiento normal
        self.assertTrue(Checkers.hay_movimientos_posibles(self.board, self.p2, [3, 4]))

    def test_puede_reingresar(self):
        """
        Prueba la validación de reingreso desde la barra.
        """
        self.board.setup(self.p1.color(), self.p2.color())
        # Destino vacío
        self.assertEqual(Checkers.puede_reingresar(self.board, self.p1, 1), 0)
        # Destino con ficha propia
        self.board.get_points()[0] = [self.p1.color()]
        self.assertEqual(Checkers.puede_reingresar(self.board, self.p1, 1), 0)
        # Destino con una ficha rival
        self.board.get_points()[0] = [self.p2.color()]
        self.assertEqual(Checkers.puede_reingresar(self.board, self.p1, 1), 0)
        # Destino bloqueado
        self.board.get_points()[0] = [self.p2.color()] * 2
        self.assertIsNone(Checkers.puede_reingresar(self.board, self.p1, 1))

    def test_reingresar_desde_bar(self):
        """
        Prueba el reingreso de fichas desde la barra.
        """
        self.board.get_bar()[self.p1.color()].append(self.p1.color())
        # Reingreso simple
        Checkers.reingresar_desde_bar(self.board, self.p1, 1)
        self.assertFalse(self.board.get_bar()[self.p1.color()])
        self.assertEqual(self.board.get_points()[0], [self.p1.color()])
        # Reingreso con captura
        self.board.get_bar()[self.p1.color()].append(self.p1.color())
        self.board.get_points()[1] = [self.p2.color()]
        Checkers.reingresar_desde_bar(self.board, self.p1, 2)
        self.assertFalse(self.board.get_bar()[self.p1.color()])
        self.assertEqual(self.board.get_points()[1], [self.p1.color()])
        self.assertEqual(self.board.get_bar()[self.p2.color()], [self.p2.color()])
        # Reingreso bloqueado
        self.board.get_bar()[self.p1.color()].append(self.p1.color())
        self.board.get_points()[0] = [self.p2.color()] * 2
        with self.assertRaises(MovimientoInvalido):
            Checkers.reingresar_desde_bar(self.board, self.p1, 1)

    def test_todas_en_inicio(self):
        """
        Prueba la comprobación de si todas las fichas están en la casa.
        """
        # --- Pruebas para el Jugador 1 (blanco) ---
        # Limpiar el tablero
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        # Todas en casa
        for i in range(18, 24):
            self.board.get_points()[i] = [self.p1.color()]
        self.assertTrue(Checkers.todas_en_inicio(self.board, self.p1))
        # Una fuera de casa
        self.board.get_points()[0] = [self.p1.color()]
        self.assertFalse(Checkers.todas_en_inicio(self.board, self.p1))
        # Una en la barra
        self.board.get_points()[0] = []
        self.board.get_bar()[self.p1.color()].append(self.p1.color())
        self.assertFalse(Checkers.todas_en_inicio(self.board, self.p1))
        self.board.get_bar()[self.p1.color()] = []

        # --- Pruebas para el Jugador 2 (negro) ---
        # Limpiar el tablero
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        # Todas en casa (0-5)
        for i in range(6):
            self.board.get_points()[i] = [self.p2.color()]
        self.assertTrue(Checkers.todas_en_inicio(self.board, self.p2))
        # Una fuera de casa
        self.board.get_points()[10] = [self.p2.color()]
        self.assertFalse(Checkers.todas_en_inicio(self.board, self.p2))
        # Una en la barra
        self.board.get_points()[10] = []
        self.board.get_bar()[self.p2.color()].append(self.p2.color())
        self.assertFalse(Checkers.todas_en_inicio(self.board, self.p2))

    def test_distancia_desde_origen(self):
        """
        Prueba la comprobación de fichas más alejadas del final.
        """
        # --- Pruebas para el Jugador 1 (blanco) ---
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        self.board.get_points()[20] = [self.p1.color()]
        self.board.get_points()[18] = [self.p1.color()]
        # Hay ficha en 18, más alejada que 20
        self.assertTrue(Checkers.distancia_desde_origen(self.board, self.p1, 20))
        # No hay ficha más alejada que 18
        self.assertFalse(Checkers.distancia_desde_origen(self.board, self.p1, 18))

        # --- Pruebas para el Jugador 2 (negro) ---
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        self.board.get_points()[3] = [self.p2.color()]
        self.board.get_points()[5] = [self.p2.color()]
        # Hay ficha en 5, más alejada que 3
        self.assertTrue(Checkers.distancia_desde_origen(self.board, self.p2, 3))
        # No hay ficha más alejada que 5
        self.assertFalse(Checkers.distancia_desde_origen(self.board, self.p2, 5))

    def test_puede_bear_off(self):
        """
        Prueba la validación de movimientos de bear off.
        """
        # --- Pruebas para el Jugador 1 (blanco) ---
        # No todas en casa
        self.board.setup(self.p1.color(), self.p2.color())
        self.assertFalse(Checkers.puede_bear_off(self.board, self.p1, 23, 1))

        # Limpiar el tablero para pruebas específicas de bear_off
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        self.board.get_points()[23] = [self.p1.color()]
        self.board.get_points()[22] = [self.p1.color()]

        # Caso 1: Salida exacta es posible, pero se intenta desde otro punto
        self.assertTrue(Checkers.puede_bear_off(self.board, self.p1, 23, 1))
        self.assertFalse(Checkers.puede_bear_off(self.board, self.p1, 22, 1))

        # Ficha superior bloquea la salida
        self.board.get_points()[18] = [self.p1.color()]
        self.assertFalse(Checkers.puede_bear_off(self.board, self.p1, 23, 3))
        self.board.get_points()[18] = []

        # Salida no válida (IndexError)
        self.assertFalse(Checkers.puede_bear_off(self.board, self.p1, 23, 0))

        # --- Pruebas para el Jugador 2 (negro) ---
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        self.board.get_points()[0] = [self.p2.color()]
        self.board.get_points()[1] = [self.p2.color()]

        # Salida exacta es posible
        self.assertTrue(Checkers.puede_bear_off(self.board, self.p2, 0, 1))
        self.assertFalse(Checkers.puede_bear_off(self.board, self.p2, 1, 1))
        # Ficha superior bloquea
        self.board.get_points()[5] = [self.p2.color()]
        self.assertFalse(Checkers.puede_bear_off(self.board, self.p2, 0, 3))

        # Dado mayor permite sacar de punto inferior
        self.board.get_points()[5] = []
        self.assertTrue(Checkers.puede_bear_off(self.board, self.p2, 1, 3))
        
        # Punto más alto vacío
        self.board.get_points()[0] = []
        self.board.get_points()[1] = []
        self.assertFalse(Checkers.puede_bear_off(self.board, self.p2, 0, 1))


    def test_bear_off(self):
        """
        Prueba que se puede sacar una ficha del tablero (bear off).
        """
        # --- Pruebas para el Jugador 1 (blanco) ---
        # No todas en casa
        self.board.setup(self.p1.color(), self.p2.color())
        with self.assertRaises(MovimientoInvalido):
            Checkers.bear_off(self.board, self.p1, 23, 1)
        
        # Limpiar tablero
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        self.board.get_points()[23] = [self.p1.color()]
        self.board.get_points()[22] = [self.p1.color()]

        # Movimiento normal tiene prioridad
        self.board.get_points()[20] = [self.p1.color()]
        with self.assertRaises(MovimientoInvalido):
            Checkers.bear_off(self.board, self.p1, 23, 4)
        self.board.get_points()[20] = []
        
        # Debe sacar desde el punto exacto
        with self.assertRaises(MovimientoInvalido):
            Checkers.bear_off(self.board, self.p1, 22, 1)

        # Hay fichas en puntos más altos
        self.board.get_points()[18] = [self.p1.color()]
        with self.assertRaises(MovimientoInvalido):
            Checkers.bear_off(self.board, self.p1, 22, 5)
        self.board.get_points()[18] = []

        # El dado no es suficientemente grande
        with self.assertRaises(MovimientoInvalido):
             Checkers.bear_off(self.board, self.p1, 23, 0)

        # --- Pruebas para el Jugador 2 (negro) ---
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        self.board.get_points()[0] = [self.p2.color()]
        self.board.get_points()[5] = [self.p2.color()]

        # Fichas más altas bloquean
        with self.assertRaises(MovimientoInvalido):
            Checkers.bear_off(self.board, self.p2, 0, 6)

        # Salida correcta
        Checkers.bear_off(self.board, self.p2, 5, 6)
        self.assertEqual(self.board.get_final()[self.p2.color()], [self.p2.color()])

        # Movimiento normal tiene prioridad (jugador 2)
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        self.board.get_points()[1] = [self.p2.color()]
        self.board.get_points()[2] = [self.p2.color()]
        with self.assertRaises(MovimientoInvalido):
            Checkers.bear_off(self.board, self.p2, 2, 2)

        # Dado no es suficientemente grande
        with self.assertRaises(MovimientoInvalido):
            Checkers.bear_off(self.board, self.p2, 2, 1)


if __name__ == '__main__':
    unittest.main()
