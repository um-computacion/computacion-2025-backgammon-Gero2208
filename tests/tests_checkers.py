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

    def test_mover_y_consumir(self):
        """
        Prueba que el movimiento de una ficha consume el dado correcto.
        """
        self.board.setup(self.p1.color(), self.p2.color())
        dados = [1, 2]
        dados_restantes = Checkers.mover_y_consumir(self.board, self.p1, 0, 1, dados)
        self.assertEqual(dados_restantes, [2])

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

    def test_todas_en_inicio(self):
        """
        Prueba la comprobación de si todas las fichas están en la casa.
        """
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

    def test_puede_bear_off(self):
        """
        Prueba la validación de movimientos de bear off.
        """
        # Limpiar el tablero
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        # Poner todas las fichas en casa para la prueba inicial
        for i in range(18, 24):
            self.board.get_points()[i] = [self.p1.color()]
        self.assertTrue(Checkers.puede_bear_off(self.board, self.p1, 23, 1))

        # Probar el caso del dado mayor: solo una ficha en el punto más lejano
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        self.board.get_points()[23] = [self.p1.color()]
        self.assertTrue(Checkers.puede_bear_off(self.board, self.p1, 23, 2))

        # Probar el caso de ficha más lejana que bloquea
        self.board.get_points()[22] = [self.p1.color()]
        self.assertFalse(Checkers.puede_bear_off(self.board, self.p1, 23, 2))

    def test_bear_off(self):
        """
        Prueba que se puede sacar una ficha del tablero (bear off).
        """
        # Limpiar el tablero
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        for i in range(18, 24):
            self.board.get_points()[i] = [self.p1.color()]
        Checkers.bear_off(self.board, self.p1, 23, 1)
        self.assertFalse(self.board.get_points()[23])
        self.assertEqual(self.board.get_final()[self.p1.color()], [self.p1.color()])


if __name__ == '__main__':
    unittest.main()
