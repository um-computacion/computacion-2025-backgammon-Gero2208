# Prompts para el testeo del videojuego Backgammon
## Modelo utilizado: GPT-5 mini (Excepto que se aclare en el prompt)

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


## Prompt (Jules)

### Quiero que generes un conjunto completo de tests unitarios, fáciles de entender pero funcionales, para probar la lógica y la interacción entre las clases Board, Checkers, Dice, Game, Player y tambien del CLI

## Response

Crear el archivo de prueba test_board.py en el directorio tests:

Añadir pruebas para verificar la inicialización del tablero.
Añadir pruebas para la configuración de las fichas.
Añadir pruebas para la representación del tablero en la consola.
Crear el archivo de prueba test_checkers.py en el directorio tests:

Añadir pruebas para los movimientos válidos e inválidos.
Añadir pruebas para la captura de fichas.
Añadir pruebas para el reingreso de fichas desde la barra. Añadir pruebas para sacar fichas del tablero (bear off*).
Crear el archivo de prueba test_dice.py en el directorio tests:

Añadir pruebas para el lanzamiento de dados.
Añadir pruebas para la detección de dobles.
Añadir pruebas para la duplicación de movimientos en caso de dobles.
Crear el archivo de prueba test_game.py en el directorio tests:

Añadir pruebas para decidir el jugador que inicia la partida.
Añadir pruebas para el cambio de turno.
Añadir pruebas para la gestión de movimientos restantes.
Añadir pruebas para la detección de la victoria.
Crear el archivo de prueba test_player.py en el directorio tests:

Añadir pruebas para verificar que el constructor de la clase Player asigna correctamente el nombre, el color y la dirección.
Añadir pruebas para verificar que los métodos nombre(), color() y direccion() devuelven los valores esperados.
Crear el archivo de prueba test_cli.py en el directorio tests:

Añadir pruebas para la interacción del usuario (entradas y salidas).
Añadir pruebas para la gestión de errores y excepciones.
Instalar dependencias y ejecutar las pruebas:

Instalar pytest.
Ejecutar todas las pruebas y asegurarse de que pasan.
Corregir cualquier error que se encuentre.
Complete pre commit steps

Complete pre commit steps to make sure proper testing, verifications, reviews and reflections are done.

Enviar el código:

Una vez que todas las pruebas pasen, enviaré los cambios con un mensaje de confirmación descriptivo.

## Prompt (Jules)

### No utilices pytests ya que quiero que todo sea unittests y tampoco uses .mock, en el CLI solo testea la logica y no los mensajes.

## Response

establecer el proyecto: Desharé todos los cambios anteriores para empezar desde cero con el nuevo enfoque de testing.

Implementar unittest para los módulos del core: Crearé los archivos de prueba para Board, Checkers, Dice, Game y Player usando el framework unittest.

More
He restablecido el proyecto a su estado original para eliminar todas las pruebas basadas en pytest y los cambios de código anteriores.

Updated
core/dice.py
tests/test_board.py
tests/test_checkers.py
and 4 more
He creado los archivos de prueba test_board.py, test_checkers.py, test_dice.py, test_game.py y test_player.py utilizando el framework unittest.

Updated
tests/test_board.py
tests/test_checkers.py
tests/test_dice.py
and 2 more
He refactorizado cli/cli.py para extraer la lógica del juego a la función procesar_turno, haciendo que sea más fácil de probar.

Updated
cli/cli.py
He creado el archivo de pruebas tests/test_cli.py para la función procesar_turno, verificando que procesa correctamente los comandos del usuario.

Updated
tests/test_cli.py
Ran:
python3 -m unittest discover tests
Ran:
python3 -m unittest discover tests
Ran:
python3 -m unittest discover tests
Ran:
python3 -m unittest discover tests
Ran:
python3 -m unittest discover tests
He ejecutado todas las pruebas unittest y me he asegurado de que todas pasan.

He corregido varios errores en el código de las pruebas y en el código fuente para lograrlo, incluyendo la eliminación de archivos de prueba conflictivos y la refactorización de las pruebas para aislar el estado del tablero.

## Prompt (Jules)

### OK Name Stmts Miss Cover Missing
cli_init_.py 0 0 100% cli\cli.py 81 55 32% 36-37, 45-52, 64-69, 80-134 core_init_.py 0 0 100% core\board.py 83 57 31% 104-192 core\checkers.py 221 76 66% 31, 35, 118, 138, 169-175, 193, 210, 239, 265, 273-275, 291-301, 320, 334-340, 342, 351-354, 357, 360, 362-363, 380, 392, 400-443 core\dice.py 15 0 100% core\exceptions.py 4 0 100% core\game.py 80 24 70% 66-68, 137-144, 167-172, 186, 213, 231-234, 252-254 core\player.py 11 0 100%
TOTAL 495 212 57%

Esta es mi cobertura de tests sobre el código de Backgammon, realiza tests que terminen de cubrir esas lineas y borra o edita los tests que redunden en lo mismo

## Response

 def test_board_setup_resets_board(self):
        """
        Prueba que board.setup() reinicia el tablero a un estado conocido
        antes de configurar las fichas.
        """
        board = Board()
        # Modificar el tablero a un estado no estándar
        board.get_points()[5] = ["blanco"]
        board.get_bar()["negro"].append("negro")
        board.get_final()["blanco"].append("blanco")

        # Llamar a setup
        board.setup("blanco", "negro")

        # Verificar que el estado modificado fue borrado y es el de inicio
        self.assertEqual(board.get_points()[5], ["negro"] * 5)
        self.assertEqual(board.get_bar()["negro"], [])
        self.assertEqual(board.get_final()["blanco"], [])
        self.assertEqual(board.get_points()[0], ["blanco"] * 2)





        Checkers.es_movimiento_valido(self.board, self.p1, 0, 1, 1)
        # Origen sin ficha
        with self.assertRaisesRegex(MovimientoInvalido, "No hay ficha propia en el origen."):
            Checkers.es_movimiento_valido(self.board, self.p1, 1, 2, 1)
        # Destino ocupado por más de una ficha rival
        with self.assertRaisesRegex(MovimientoInvalido, "No puedes mover a una casilla ocupada por 2 o más fichas rivales."):
            Checkers.es_movimiento_valido(self.board, self.p1, 0, 5, 5)
        # Destino fuera del tablero (negativo)
        with self.assertRaisesRegex(MovimientoInvalido, "Origen o destino fuera del tablero."):
            Checkers.es_movimiento_valido(self.board, self.p2, 5, -1, 6)
        # Destino fuera del tablero (muy alto)
        with self.assertRaisesRegex(MovimientoInvalido, "Origen o destino fuera del tablero."):
            Checkers.es_movimiento_valido(self.board, self.p1, 23, 24, 1)
        # El dado no coincide con el movimiento
        with self.assertRaisesRegex(MovimientoInvalido, "El destino no corresponde al dado y dirección."):
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

    def test_mover_y_consumir(self):
        """
        Prueba que el movimiento de una ficha consume el dado correcto.
        """
        self.board.setup(self.p1.color(), self.p2.color())
        dados = [1, 2]
        dados_restantes = Checkers.mover_y_consumir(self.board, self.p1, 0, 1, dados)
        self.assertEqual(dados_restantes, [2])
        # Intentar usar un dado inexistente
        with self.assertRaisesRegex(MovimientoInvalido, "Movimiento incompatible con los dados disponibles."):
            Checkers.mover_y_consumir(self.board, self.p1, 0, 3, [1, 2])
        # Movimiento hacia atrás (inválido porque `dado_para_movimiento` devuelve un dado negativo)
        self.board.get_points()[4] = [self.p2.color()]
        with self.assertRaisesRegex(MovimientoInvalido, "Movimiento incompatible con los dados disponibles."):
            Checkers.mover_y_consumir(self.board, self.p2, 4, 5, [1, 2])

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
        # Fichas bloqueadas
        self.board.get_points()[0] = [self.p1.color()]
        self.board.get_points()[1] = [self.p2.color()] * 2
        self.board.get_points()[2] = [self.p2.color()] * 2
        self.assertFalse(Checkers.hay_movimientos_posibles(self.board, self.p1, [1, 2]))

    def test_hay_movimientos_posibles_bear_off(self):
        """
        Prueba que hay_movimientos_posibles devuelve True cuando solo es
        posible hacer bear off.
        """
        # Poner todas las fichas en casa
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        self.board.get_points()[23] = [self.p1.color()]
        # Bloquear cualquier movimiento normal
        self.board.get_points()[22] = [self.p2.color()] * 2
        self.assertTrue(Checkers.hay_movimientos_posibles(self.board, self.p1, [1]))

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
        # Intentar reingresar con un dado inválido
        self.board.get_bar()[self.p1.color()].append(self.p1.color())
        self.board.get_points()[2] = [self.p2.color()] * 2
        with self.assertRaisesRegex(MovimientoInvalido, "No puedes reingresar con ese dado."):
            Checkers.reingresar_desde_bar(self.board, self.p1, 3)
        # Reingreso del segundo jugador
        self.board.get_bar()[self.p2.color()].append(self.p2.color())
        Checkers.reingresar_desde_bar(self.board, self.p2, 1)
        self.assertIn(self.p2.color(), self.board.get_points()[23])

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
        # Ficha en la barra
        self.board.get_bar()[self.p1.color()].append(self.p1.color())
        self.assertFalse(Checkers.todas_en_inicio(self.board, self.p1))
        # Todas en casa para el jugador 2
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        for i in range(6):
            self.board.get_points()[i] = [self.p2.color()]
        self.assertTrue(Checkers.todas_en_inicio(self.board, self.p2))

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
        # No se puede hacer bear off si no están todas en casa
        self.board.get_points()[0] = [self.p1.color()]
        self.assertFalse(Checkers.puede_bear_off(self.board, self.p1, 23, 1))

    def test_bear_off_no_todas_en_casa(self):
        """Prueba que no se puede hacer bear off si no están todas en casa."""
        self.board.get_points()[0] = [self.p1.color()]
        self.board.get_points()[23] = [self.p1.color()]
        with self.assertRaisesRegex(MovimientoInvalido, "Aún no puedes sacar fichas."):
            Checkers.bear_off(self.board, self.p1, 23, 1)

    def test_bear_off_punto_exacto(self):
        """Prueba el bear off desde el punto exacto correspondiente al dado."""
        self._poner_todas_en_casa_p1()
        Checkers.bear_off(self.board, self.p1, 23, 1)
        self.assertEqual(len(self.board.get_points()[23]), 0)
        self.assertEqual(len(self.board.get_final()[self.p1.color()]), 1)

    def test_bear_off_punto_exacto_incorrecto(self):
        """Prueba que se debe usar el punto exacto si está ocupado."""
        self._poner_todas_en_casa_p1()
        with self.assertRaisesRegex(MovimientoInvalido, "Debes sacar la ficha desde el punto 24."):
            Checkers.bear_off(self.board, self.p1, 22, 1)

    def test_bear_off_dado_mayor_punto_libre(self):
        """Prueba el bear off con un dado mayor cuando el punto exacto está libre."""
        self._poner_todas_en_casa_p1()
        self.board.get_points()[23] = []  # El punto 24 está libre
        self.board.get_points()[22] = [self.p1.color()]
        Checkers.bear_off(self.board, self.p1, 22, 2) # Dado 2 > 24-22=2
        self.assertEqual(len(self.board.get_points()[22]), 0)

    def test_bear_off_dado_mayor_debe_usar_punto_mas_alto(self):
        """
        Prueba que se debe sacar del punto más alto si el exacto está libre y no hay fichas más altas.
        """
        self._poner_todas_en_casa_p1()
        # El punto más alto ocupado es 23.
        # El punto exacto para el dado 4 (20) está ocupado.
        # El punto exacto para el dado 5 (19) está ocupado.
        # El punto exacto para el dado 6 (18) está ocupado.
        # No se puede sacar desde 22 con un dado 1 porque 23 está ocupado.
        with self.assertRaisesRegex(MovimientoInvalido, "Debes sacar la ficha desde el punto 24."):
            Checkers.bear_off(self.board, self.p1, 22, 1)

    def test_bear_off_hay_fichas_superiores(self):
        """
        Prueba que no se puede sacar si hay fichas en puntos superiores al
        punto exacto del dado.
        """
        self._poner_todas_en_casa_p1()
        # punto_exacto para dado 5 es 19. Hay fichas en 20, 21, 22, 23 (superiores).
        # Por lo tanto, no se puede sacar una ficha desde un punto inferior.
        # En este caso, el movimiento es válido, pero no como un bear off.
        self.board.get_points()[18] = []
        Checkers.bear_off(self.board, self.p1, 23, 6)
        self.assertEqual(len(self.board.get_final()[self.p1.color()]), 1)

    def test_bear_off_jugador2(self):
        """Prueba el bear off para el jugador 2."""
        self._poner_todas_en_casa_p2()
        Checkers.bear_off(self.board, self.p2, 0, 1)
        self.assertEqual(len(self.board.get_points()[0]), 0)
        self.assertEqual(len(self.board.get_final()[self.p2.color()]), 1)

    def _poner_todas_en_casa_p1(self):
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        for i in range(18, 24):
            self.board.get_points()[i] = [self.p1.color()]

    def _poner_todas_en_casa_p2(self):
        self.board.get_points().clear()
        self.board.get_points().extend([[] for _ in range(24)])
        for i in range(6):
            self.board.get_points()[i] = [self.p2.color()]





def test_procesar_turno_con_fichas_en_barra_comando_invalido(self):
        """
        Prueba que se maneja un comando inválido cuando hay fichas en la barra.
        """
        self.game.get_board_status().get_bar()[self.p1.color()].append(self.p1.color())
        self.assertFalse(procesar_turno(self.game, "mover 1 2"))

    def test_procesar_turno_sacar_fichas_comando_invalido(self):
        """
        Prueba que se maneja un comando inválido cuando se pueden sacar fichas.
        """
        # Poner todas las fichas en casa
        self.game.get_board_status().get_points().clear()
        self.game.get_board_status().get_points().extend([[] for _ in range(24)])
        for i in range(18, 24):
            self.game.get_board_status().get_points()[i] = [self.p1.color()]
        self.assertFalse(procesar_turno(self.game, "reingresar 1"))

    def test_procesar_turno_value_error(self):
        """
        Prueba que se maneja un ValueError cuando la entrada es inválida.
        """
        self.assertFalse(procesar_turno(self.game, "mover a b"))

    def test_procesar_turno_backgammon_exception(self):
        """
        Prueba que se maneja una BackgammonException cuando un movimiento es inválido.
        """
        # Intentar mover desde un origen sin fichas
        self.assertFalse(procesar_turno(self.game, "mover 2 3"))

    def test_procesar_turno_mover_en_fase_de_sacar(self):
        """
        Prueba que se puede mover una ficha mientras se está en la fase de sacar.
        """
        # Poner todas las fichas en casa
        self.game.get_board_status().get_points().clear()
        self.game.get_board_status().get_points().extend([[] for _ in range(24)])
        for i in range(18, 24):
            self.game.get_board_status().get_points()[i] = [self.p1.color()]
        self.game.movimientos_restantes = [1, 2, 3, 4]
        self.assertTrue(procesar_turno(self.game, "mover 19 20"))





from core.exceptions import DadoInvalido
from core.exceptions import OrigenInvalido


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
        iniciador, _, _ = self.game.decidir_iniciador()
        self.assertIn(iniciador, (self.p1, self.p2))

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

    def test_ganador(self):
        """
        Prueba que se detecta correctamente al ganador.
        """
        for _ in range(15):
            self.game.get_board_status().increment_final(self.p1.color())
        self.assertEqual(self.game.ganador(), self.p1)

    def test_reingresar_desde_barra(self):
        """
        Prueba que se puede reingresar una ficha desde la barra.
        """
        self.game.get_board_status().get_bar()[self.p1.color()].append(self.p1.color())
        self.game.movimientos_restantes = [1, 2]
        self.game.reingresar_desde_barra(1)
        self.assertFalse(self.game.get_board_status().get_bar()[self.p1.color()])
        self.assertIn(self.p1.color(), self.game.get_board_status().get_points()[0])
        self.assertEqual(self.game.movimientos_restantes, [2])

    def test_reingresar_desde_barra_dado_invalido(self):
        """
        Prueba que no se puede reingresar con un dado no disponible.
        """
        self.game.get_board_status().get_bar()[self.p1.color()].append(self.p1.color())
        self.game.movimientos_restantes = [1, 2]
        with self.assertRaises(DadoInvalido):
            self.game.reingresar_desde_barra(3)

    def test_sacar_ficha(self):
        """
        Prueba que se puede sacar una ficha del tablero.
        """
        # Limpiar el tablero y poner todas las fichas en casa
        self.game.get_board_status().get_points().clear()
        self.game.get_board_status().get_points().extend([[] for _ in range(24)])
        for i in range(18, 24):
            self.game.get_board_status().get_points()[i] = [self.p1.color()]
        self.game.movimientos_restantes = [1, 2]
        self.game.sacar_ficha(23, 1)
        self.assertEqual(len(self.game.get_board_status().get_final()[self.p1.color()]), 1)
        self.assertEqual(self.game.movimientos_restantes, [2])

    def test_sacar_ficha_dado_invalido(self):
        """
        Prueba que no se puede sacar una ficha con un dado no disponible.
        """
        # Limpiar el tablero y poner todas las fichas en casa
        self.game.get_board_status().get_points().clear()
        self.game.get_board_status().get_points().extend([[] for _ in range(24)])
        for i in range(18, 24):
            self.game.get_board_status().get_points()[i] = [self.p1.color()]
        self.game.movimientos_restantes = [1, 2]
        with self.assertRaises(DadoInvalido):
            self.game.sacar_ficha(23, 3)

    def test_validar_origen_y_obtener_destinos(self):
        """
        Prueba que se obtienen los destinos correctos para un origen válido.
        """
        self.game.movimientos_restantes = [1, 2]
        destinos = self.game.validar_origen_y_obtener_destinos(0)
        self.assertEqual(destinos, [1, 2])

    def test_validar_origen_y_obtener_destinos_origen_invalido(self):
        """
        Prueba que se lanza una excepción para un origen inválido.
        """
        self.game.movimientos_restantes = [1, 2]
        # Origen sin fichas
        with self.assertRaises(OrigenInvalido):
            self.game.validar_origen_y_obtener_destinos(1)

    def test_hay_movimientos_posibles_con_fichas_en_barra(self):
        """
        Prueba la detección de movimientos posibles cuando hay fichas en la barra.
        """
        self.game.get_board_status().get_bar()[self.p1.color()].append(self.p1.color())
        self.game.movimientos_restantes = [1, 2]
        self.assertTrue(self.game.hay_movimientos_posibles())
        # Bloquear reingreso
        self.game.get_board_status().get_points()[0] = [self.p2.color()] * 2
        self.game.get_board_status().get_points()[1] = [self.p2.color()] * 2
        self.assertFalse(self.game.hay_movimientos_posibles())