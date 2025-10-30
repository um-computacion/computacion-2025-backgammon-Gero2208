"""
Este módulo contiene las pruebas unitarias para la interfaz de línea de
comandos (CLI).
"""
import unittest
from unittest.mock import patch
from cli.cli import procesar_turno, main
from core.game import Game
from core.player import Player
from core.exceptions import BackgammonException


class TestCli(unittest.TestCase):
    """
    Pruebas para la interfaz de línea de comandos (CLI).
    """

    def setUp(self):
        """
        Configura un nuevo juego para cada prueba.
        """
        self.p1 = Player("blanco", "p1", +1)
        self.p2 = Player("negro", "p2", -1)
        self.game = Game(self.p1, self.p2)
        self.game.movimientos_restantes = [1, 2, 3, 4]

    def test_procesar_turno_movimiento_normal(self):
        """
        Prueba que un movimiento normal se procesa correctamente.
        """
        # Configurar el tablero para un movimiento simple
        self.game.get_board_status().get_points()[0] = [self.p1.color()]
        self.assertTrue(procesar_turno(self.game, "mover 1 2"))
        self.assertEqual(len(self.game.get_board_status().get_points()[0]), 0)
        self.assertIn(self.p1.color(), self.game.get_board_status().get_points()[1])

    def test_procesar_turno_reingresar(self):
        """
        Prueba que el reingreso de una ficha desde la barra se procesa
        correctamente.
        """
        # Poner una ficha en la barra
        self.game.get_board_status().get_bar()[self.p1.color()].append(self.p1.color())
        self.assertTrue(procesar_turno(self.game, "reingresar 1"))
        self.assertFalse(self.game.get_board_status().get_bar()[self.p1.color()])
        self.assertIn(self.p1.color(), self.game.get_board_status().get_points()[0])

    def test_procesar_turno_sacar_ficha(self):
        """
        Prueba que sacar una ficha del tablero se procesa correctamente.
        """
        # Limpiar el tablero y poner todas las fichas del p1 en casa
        self.game.get_board_status().get_points().clear()
        self.game.get_board_status().get_points().extend([[] for _ in range(24)])
        for i in range(18, 24):
            self.game.get_board_status().get_points()[i] = [self.p1.color()]

        self.game.movimientos_restantes = [1]
        self.assertTrue(procesar_turno(self.game, "sacar 24 1"))

        # Verificar que la ficha fue sacada
        self.assertEqual(len(self.game.get_board_status().get_points()[23]), 0)
        self.assertEqual(len(self.game.get_board_status().get_final()[self.p1.color()]), 1)

    def test_procesar_turno_comando_invalido(self):
        """
        Prueba que los comandos inválidos se manejan correctamente.
        """
        self.assertFalse(procesar_turno(self.game, "comando_invalido"))
        self.assertFalse(procesar_turno(self.game, "mover 1"))
        self.assertFalse(procesar_turno(self.game, "mover 1 2 3"))

    def test_procesar_turno_comando_invalido_con_fichas_en_barra(self):
        """
        Prueba que se devuelve False si se introduce un comando inválido
        mientras hay fichas en la barra.
        """
        self.game.get_board_status().get_bar()[self.p1.color()].append(self.p1.color())
        self.assertFalse(procesar_turno(self.game, "mover 1 2"))

    def test_procesar_turno_mover_en_casa(self):
        """
        Prueba que un movimiento normal se procesa correctamente cuando el
        jugador está en casa.
        """
        # Poner todas las fichas en casa
        self.game.get_board_status().get_points().clear()
        self.game.get_board_status().get_points().extend([[] for _ in range(24)])
        self.game.get_board_status().get_points()[18] = [self.p1.color()]

        self.assertTrue(procesar_turno(self.game, "mover 19 20"))
        self.assertEqual(len(self.game.get_board_status().get_points()[18]), 0)
        self.assertIn(self.p1.color(), self.game.get_board_status().get_points()[19])

    def test_procesar_turno_comando_invalido_en_casa(self):
        """
        Prueba que se devuelve False si se introduce un comando inválido
        mientras el jugador está en casa.
        """
        # Poner todas las fichas en casa
        self.game.get_board_status().get_points().clear()
        self.game.get_board_status().get_points().extend([[] for _ in range(24)])
        self.game.get_board_status().get_points()[18] = [self.p1.color()]

        self.assertFalse(procesar_turno(self.game, "reingresar 1"))

    def test_procesar_turno_value_error(self):
        """
        Prueba el manejo de ValueError para entradas no numéricas.
        """
        self.assertFalse(procesar_turno(self.game, "mover a b"))

    @patch('core.game.Game.mover_ficha', side_effect=BackgammonException("Error simulado"))
    def test_procesar_turno_backgammon_exception(self, mock_mover_ficha):
        """
        Prueba el manejo de BackgammonException durante el procesamiento del
        turno.
        """
        self.assertFalse(procesar_turno(self.game, "mover 1 2"))
        mock_mover_ficha.assert_called_once()


if __name__ == '__main__':
    unittest.main()


class TestMainFunction(unittest.TestCase):

    @patch('cli.cli.procesar_turno')
    @patch('cli.cli.Game')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=[
        'Jugador1',  # nombre1
        'blanco',    # color1
        'Jugador2',  # nombre2
        'mover 1 2',  # jugada turno 1
    ])
    def test_main_flujo_basico(self, mock_input, mock_print, mock_game_class, mock_procesar_turno):
        """
        Prueba el flujo básico de la función main: inicio, un turno y victoria.
        """
        # Configurar la instancia mock de Game que será devuelta por el constructor
        mock_game_instance = mock_game_class.return_value
        p1_mock = Player("blanco", "Jugador1", +1)
        mock_game_instance.decidir_iniciador.return_value = (p1_mock, 6, 1)

        # Simular un turno y luego un ganador
        mock_game_instance.ganador.side_effect = [None, p1_mock]
        mock_game_instance.jugador_actual.return_value = p1_mock

        # Simular el bucle de movimientos
        mock_game_instance.movimientos_restantes = [1]
        def procesar_turno_side_effect(game, entrada):
            game.movimientos_restantes = []
        mock_procesar_turno.side_effect = procesar_turno_side_effect

        mock_game_instance.hay_movimientos_posibles.return_value = True

        main()

        mock_procesar_turno.assert_called_once_with(mock_game_instance, 'mover 1 2')
        mock_print.assert_any_call("¡Felicidades, Jugador1! Has ganado la partida.")
        mock_game_instance.cambiar_turno.assert_not_called()

    @patch('cli.cli.Game')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['p1', 'azul', 'blanco', 'p2'])
    def test_main_color_invalido(self, mock_input, mock_print, mock_game_class):
        """
        Prueba que el bucle de validación de color en main funciona.
        """
        mock_game_instance = mock_game_class.return_value
        p1_mock = Player("blanco", "p1", +1)
        mock_game_instance.decidir_iniciador.return_value = (p1_mock, 1, 1)
        mock_game_instance.ganador.return_value = p1_mock  # Termina inmediatamente

        main()

        mock_print.assert_any_call("Color inválido. Debe ser 'Blanco' o 'Negro'")
        args, kwargs = mock_game_class.call_args
        created_p1 = args[0]
        self.assertEqual(created_p1.color(), "blanco")

    @patch('cli.cli.Game')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['p1', 'blanco', 'p2'])
    def test_main_sin_movimientos_posibles(self, mock_input, mock_print, mock_game_class):
        """
        Prueba la rama de no tener movimientos posibles en main.
        """
        mock_game_instance = mock_game_class.return_value
        p1_mock = Player("blanco", "p1", +1)
        p2_mock = Player("negro", "p2", -1)

        mock_game_instance.decidir_iniciador.return_value = (p1_mock, 1, 1)
        mock_game_instance.ganador.side_effect = [None, None, p1_mock]
        mock_game_instance.jugador_actual.side_effect = [p1_mock, p2_mock]
        type(mock_game_instance).movimientos_restantes = [1, 2]
        mock_game_instance.hay_movimientos_posibles.return_value = False

        main()

        mock_print.assert_any_call("No tienes movimientos posibles con los dados restantes.")
        self.assertEqual(mock_input.call_count, 3)
        mock_game_instance.cambiar_turno.assert_called_once()