# Prompts para el desarrollo del videojuego Backgammon

## Prompt

### Como puedo empezar a armar mi clase board para el videojuego backgammon? Haz docstrings en español

## Response

Ejecutaré cuatro acciones: 1) marcaré la tarea de revisión como completada y pondré la implementación de Board en progreso en la lista de tareas; 2) actualizaré board.py con una clase Board inicial y docstrings en español; 3) crearé backgammon/tests/test_board.py con dos pruebas unitarias; 4) ejecutaré los tests para validar. Resultado esperado: tests pasan (o fallan con errores descriptivos para corregir).

Voy a actualizar board.py con una implementación inicial de Board que incluye: estructura interna de 24 puntos, setup() para la posición inicial de backgammon, acceso a puntos, comprobación básica de movimiento y apply_move. La meta es que las pruebas unitarias puedan ejecutarse. Luego crearé la prueba.

## Prompt

### Como puedo hacer un método para la clase Board en la que se muestre un tablero en el CLI el cual podre usar a futuro para visualizar las fichas?

## Response

Perfecto! Aquí tienes un método para tu clase Board que muestra el tablero de Backgammon en el CLI de forma gráfica y compacta, usando dos filas (superior e inferior) y agrupando los puntos como en un tablero real.

Agrega este método a tu archivo board.py:

    def mostrar_tablero_cli(self):
        """
        Muestra el tablero de Backgammon en la consola de forma gráfica y compacta.
        Cada punto muestra la cantidad de fichas y el color/jugador.
        """
        # Encabezados de los puntos
        print("    13 14 15 16 17 18   |   19 20 21 22 23 24")
        print("  +---------------------+---------------------+")
        # Fila superior (puntos 12 a 23)
        fila_sup = "  |"
        for i in range(12, 24):
            punto = self.__points__[i]
            if punto:
                ficha = punto[0][0].upper()  # Primera letra del color/jugador
                cantidad = len(punto)
                fila_sup += f" {ficha}{cantidad:1}"
            else:
                fila_sup += " --"
            if i == 17:
                fila_sup += "   |"
        fila_sup += "   |"
        print(fila_sup)
        print("  +---------------------+---------------------+")

        # Fila inferior (puntos 11 a 0)
        print("    12 11 10  9  8  7   |    6  5  4  3  2  1")
        fila_inf = "  |"
        for i in range(11, -1, -1):
            punto = self.__points__[i]
            if punto:
                ficha = punto[0][0].upper()
                cantidad = len(punto)
                fila_inf += f" {ficha}{cantidad:1}"
            else:
                fila_inf += " --"
            if i == 6:
                fila_inf += "   |"
        fila_inf += "   |"
        print(fila_inf)
        print("  +---------------------+---------------------+")

        # Mostrar barra y borne-off (final)
        bar_blanco = len(self.__bar__.get("blanco", []))
        bar_negro = len(self.__bar__.get("negro", []))
        off_blanco = len(self.__final__.get("blanco", []))
        off_negro = len(self.__final__.get("negro", []))
        print(f"Barra: Blanco={bar_blanco}  Negro={bar_negro}   |   Final: Blanco={off_blanco}  Negro={off_negro}")
    
    Notas:

    Cada punto muestra la inicial del color/jugador y la cantidad de fichas (ej: B2 = 2 blancas, N3 = 3 negras).
    Puedes ajustar los nombres según cómo guardes los colores en tus listas internas.
    Si usas otros identificadores, cambia punto[0][0].upper() por lo que corresponda.

    Uso:
    Solo llama a board.mostrar_tablero_cli() en tu CLI y tendrás una visualización clara y ordenada del tablero en la terminal.

## Prompt

### Ademas hay un archivo checkers. Estoy dividiendo todo en clases, mi método mostrar_tablero tiene bien hechas las dependencias y esta utilizando los atributos adecuados? Ademas, quiero que representes con triangulos los 24 lugares y me expliques que signica la barra abajo donde pone 0 negro y 0 blanco

## Response

Tu método mostrar_tablero_cli está bien estructurado en cuanto a dependencias:

Utiliza solo los atributos internos de la clase Board (self.__points__, self.__bar__, self.__final__).
No depende de otras clases externas (como Player o Checkers) para mostrar el tablero, lo cual es correcto para una función de visualización del estado.
Sobre los atributos:

self.__points__: lista de 24 puntos, cada uno es una lista de fichas (identificadas por color o jugador).
self.__bar__: diccionario con las fichas capturadas de cada jugador (por ejemplo, "blanco" y "negro").
self.__final__: diccionario con las fichas que ya salieron del tablero (borne-off).
Sobre la barra:

La línea Barra: Blanco=0  Negro=0   |   Final: Blanco=0  Negro=0 muestra:
Cuántas fichas de cada color están en la barra (es decir, han sido capturadas y deben volver a entrar al tablero).
Cuántas fichas de cada color ya han salido del tablero (han llegado a la zona final, "borne-off").
¿Qué significa la barra?

En Backgammon, cuando una ficha es capturada, va a la barra y debe volver a entrar antes de que el jugador pueda mover otras fichas.
Si ves Barra: Blanco=2  Negro=0, significa que el jugador blanco tiene 2 fichas capturadas esperando para reingresar.
Final: Blanco=0  Negro=0 indica que ningún jugador ha sacado fichas del tablero aún.
Representación con triángulos
Puedes usar el carácter ▲ para la fila superior y ▼ para la fila inferior, representando los 24 triángulos del tablero. Aquí tienes una versión mejorada del método:

Representación con triángulos
Puedes usar el carácter ▲ para la fila superior y ▼ para la fila inferior, representando los 24 triángulos del tablero. Aquí tienes una versión mejorada del método:

    def mostrar_tablero_cli(self):
        """
        Muestra el tablero de Backgammon en la consola de forma gráfica con triángulos.
        Cada punto muestra la cantidad de fichas y el color/jugador.
        """
        # Encabezados de los puntos
        print("    13 14 15 16 17 18   |   19 20 21 22 23 24")
        print("  +---------------------+---------------------+")
        # Fila superior (puntos 12 a 23)
        fila_sup = "  |"
        for i in range(12, 24):
            punto = self.__points__[i]
            if punto:
                ficha = punto[0][0].upper()  # Primera letra del color/jugador
                cantidad = len(punto)
                fila_sup += f"▲{ficha}{cantidad}"
            else:
                fila_sup += "▲--"
            if i == 17:
                fila_sup += "   |"
        fila_sup += "   |"
        print(fila_sup)
        print("  +---------------------+---------------------+")

        # Fila inferior (puntos 11 a 0)
        print("    12 11 10  9  8  7   |    6  5  4  3  2  1")
        fila_inf = "  |"
        for i in range(11, -1, -1):
            punto = self.__points__[i]
            if punto:
                ficha = punto[0][0].upper()
                cantidad = len(punto)
                fila_inf += f"▼{ficha}{cantidad}"
            else:
                fila_inf += "▼--"
            if i == 6:
                fila_inf += "   |"
        fila_inf += "   |"
        print(fila_inf)
        print("  +---------------------+---------------------+")

        # Mostrar barra y borne-off (final)
        bar_blanco = len(self.__bar__.get("blanco", []))
        bar_negro = len(self.__bar__.get("negro", []))
        off_blanco = len(self.__final__.get("blanco", []))
        off_negro = len(self.__final__.get("negro", []))
        print(f"Barra: Blanco={bar_blanco}  Negro={bar_negro}   |   Final: Blanco={off_blanco}  Negro={off_negro}")

Explicación de la barra:

"Barra: Blanco=0  Negro=0": cuántas fichas de cada color están capturadas y deben volver a entrar.
"Final: Blanco=0  Negro=0": cuántas fichas de cada color ya han salido del tablero (han ganado).
Resumen:

Tu método usa bien las dependencias y atributos.
La barra muestra el estado de fichas capturadas y borne-off.
Ahora el tablero se ve con triángulos, haciendo más visual la experiencia en el CLI.

## Prompt

### Puedes quitar la numeracion al tablero? Ya que no hace falta y ahi mostrar la cantidad de fichas que hay y el color

## Response

    def mostrar_tablero_cli(self):
        """
        Muestra el tablero de Backgammon en la consola de forma gráfica,
        sin numeración, solo triángulos y fichas por color.
        """
        simbolos = {"blanco": "⚪", "negro": "⚫", "jugador1": "A", "jugador2": "B"}

        print("  +---------------------+---------------------+")
        # Fila superior (puntos 12 a 23)
        fila_sup = "  |"
        for i in range(12, 24):
            punto = self.__points__[i]
            if punto:
                color = punto[0]
                ficha = simbolos.get(color, "?")
                cantidad = len(punto)
                if cantidad <= 5:
                    fila_sup += f"▲{ficha * cantidad: <2}"
                else:
                    fila_sup += f"▲{ficha}x{cantidad}"
            else:
                fila_sup += "▲  "
            if i == 17:
                fila_sup += "   |"
        fila_sup += "   |"
        print(fila_sup)
        print("  +---------------------+---------------------+")

        # Fila inferior (puntos 11 a 0)
        fila_inf = "  |"
        for i in range(11, -1, -1):
            punto = self.__points__[i]
            if punto:
                color = punto[0]
                ficha = simbolos.get(color, "?")
                cantidad = len(punto)
                if cantidad <= 5:
                    fila_inf += f"▼{ficha * cantidad: <2}"
                else:
                    fila_inf += f"▼{ficha}x{cantidad}"
            else:
                fila_inf += "▼  "
            if i == 6:
                fila_inf += "   |"
        fila_inf += "   |"
        print(fila_inf)
        print("  +---------------------+---------------------+")

        bar_blanco = len(self.__bar__.get("blanco", []))
        bar_negro = len(self.__bar__.get("negro", []))
        off_blanco = len(self.__final__.get("blanco", []))
        off_negro = len(self.__final__.get("negro", []))
        print(f"Barra: Blanco={bar_blanco}  Negro={bar_negro}   |   Final: Blanco={off_blanco}  Negro={off_negro}")

## Prompt

### Puedes hacer que en el tablero las fichas aparezcan en columna encima del triangulo en vez de horizontalmente? Ademas, respeta espacios para que se vea correctamente horizontal toda la estructura y las fichas

## Response

    def mostrar_tablero_cli(self):
        """
        Muestra el tablero de Backgammon en la consola de forma gráfica,
        con las fichas apiladas en columna sobre cada triángulo.
        """
        simbolos = {"blanco": "⚪", "negro": "⚫"}

        # Prepara las columnas de fichas para la fila superior (12 a 23)
        columnas_sup = []
        for i in range(12, 24):
            punto = self.__points__[i]
            color = punto[0] if punto else None
            ficha = simbolos.get(color, " ") if color else " "
            cantidad = len(punto)
            if cantidad == 0:
                columnas_sup.append(["  "] * 5)
            elif cantidad <= 5:
                col = [f" {ficha}" for _ in range(cantidad)]
                col += ["  "] * (5 - cantidad)
                columnas_sup.append(col)
            else:
                col = [f" {ficha}" for _ in range(4)] + [f"x{cantidad}"]
                columnas_sup.append(col)

        # Prepara las columnas de fichas para la fila inferior (11 a 0)
        columnas_inf = []
        for i in range(11, -1, -1):
            punto = self.__points__[i]
            color = punto[0] if punto else None
            ficha = simbolos.get(color, " ") if color else " "
            cantidad = len(punto)
            if cantidad == 0:
                columnas_inf.append(["  "] * 5)
            elif cantidad <= 5:
                col = [f" {ficha}" for _ in range(cantidad)]
                col += ["  "] * (5 - cantidad)
                columnas_inf.append(col)
            else:
                col = [f" {ficha}" for _ in range(4)] + [f"x{cantidad}"]
                columnas_inf.append(col)

        print("  +---------------------+---------------------+")
        # Imprime las filas de fichas (de arriba hacia abajo)
        for fila in range(4, -1, -1):
            linea = "  |"
            for idx, col in enumerate(columnas_sup):
                linea += col[fila]
                if idx == 5 or idx == 11:
                    linea += "   |"
            print(linea)
        # Imprime los triángulos superiores
        linea = "  |"
        for idx in range(12, 24):
            linea += " ▲"
            if idx == 17:
                linea += "   |"
        print(linea + "   |")
        print("  +---------------------+---------------------+")

        # Imprime los triángulos inferiores
        linea = "  |"
        for idx in range(11, -1, -1):
            linea += " ▼"
            if idx == 6:
                linea += "   |"
        print(linea + "   |")
        # Imprime las filas de fichas (de abajo hacia arriba)
        for fila in range(5):
            linea = "  |"
            for idx, col in enumerate(columnas_inf):
                linea += col[fila]
                if idx == 5 or idx == 11:
                    linea += "   |"
            print(linea)
        print("  +---------------------+---------------------+")

        bar_blanco = len(self.__bar__.get("blanco", []))
        bar_negro = len(self.__bar__.get("negro", []))
        off_blanco = len(self.__final__.get("blanco", []))
        off_negro = len(self.__final__.get("negro", []))
        print(f"Barra: Blanco={bar_blanco}  Negro={bar_negro}   |   Final: Blanco={off_blanco}  Negro={off_negro}")

## Prompt

### Tengo este método para mostrar el tablero del juego Backgammon en el CLI, el problema es que el tablero y las fichas no estan alineadas y quedan totalmente movidas, necesito que lo rehagas para que se vea correctamente alineado.

## Response

def mostrar_tablero_cli(self, alto_col=5, ancho_col=3, simbolos=None):
    """
    Muestra el tablero de Backgammon en la consola de forma alineada.
    - alto_col: alto visible de cada columna de fichas (5 por defecto).
    - ancho_col: ancho fijo de cada celda/columna (3 por defecto).
    - simbolos: dict opcional {"blanco": "○", "negro": "●"}.
      Si tu terminal no respeta el ancho, usa {"blanco": "O", "negro": "X"}.
    """
    # --- Config ---
    if simbolos is None:
        simbolos = {"blanco": "○", "negro": "●"}  # Usa ASCII si tu terminal no los muestra bien.
    VACIO = " "

    def celda(txt):
        return f"{txt:^{ancho_col}}"

    def columna_para_pila(pila, orientacion="top"):
        """
        Devuelve una lista de largo alto_col, con las fichas 'pegadas'
        hacia 'top' (para fila superior) o 'bottom' (para fila inferior).
        Si hay más de alto_col fichas, se muestran (alto_col-1) y un '×N'.
        """
        if not pila:
            return [celda(VACIO)] * alto_col

        color = pila[0]
        ficha = simbolos.get(color, VACIO)
        n = len(pila)

        if n <= alto_col:
            fichas = [celda(ficha)] * n
            vacios = [celda(VACIO)] * (alto_col - n)
            if orientacion == "top":
                # Pegadas arriba
                return fichas + vacios
            else:
                # Pegadas abajo
                return vacios + fichas
        else:
            # (alto_col-1) fichas + contador
            visibles = alto_col - 1
            contador = celda(f"×{n}")
            fichas = [celda(ficha)] * visibles
            if orientacion == "top":
                return fichas + [contador]
            else:
                return [contador] + fichas

    # --- Construcción de columnas visibles ---
    # Top visual: índices internos 12..23 (que el usuario ve como 13..24 izquierda->derecha)
    columnas_sup = [columna_para_pila(self.__points__[i], "top") for i in range(12, 24)]
    # Bottom visual: índices internos 11..0 (que el usuario ve como 12..1 izquierda->derecha)
    columnas_inf = [columna_para_pila(self.__points__[i], "bottom") for i in range(11, -1, -1)]

    # --- Helpers de impresión ---
    def separador():
        # Dos cuadrantes de 6 columnas cada uno
        return "  +" + "-" * (ancho_col * 6) + "+" + "-" * (ancho_col * 6) + "+"

    def linea_con_divisiones(celdas):
        # Inserta una barra vertical entre las columnas 6 y 7 (bar central)
        partes = ["  |"]
        for idx, c in enumerate(celdas, 1):
            partes.append(c)
            if idx == 6:
                partes.append("|")
        partes.append("|")
        return "".join(partes)

    # --- Encabezados (números de puntos) ---
    cab_sup = []
    for p in range(13, 25):  # 13..24
        cab_sup.append(celda(str(p if p >= 10 else f" {p}")))
    cab_inf = []
    for p in range(12, 0, -1):  # 12..1
        cab_inf.append(celda(str(p if p >= 10 else f" {p}")))

    # --- Impresión ---
    print()
    print("   " + "".join(cab_sup[:6]) + " " + "".join(cab_sup[6:]))
    print(separador())

    # Fila superior: se imprime de arriba (índice alto) hacia abajo (índice 0)
    for fila in range(alto_col - 1, -1, -1):
        fila_sup = [col[fila] for col in columnas_sup]
        print(linea_con_divisiones(fila_sup))

    # Triángulos superiores
    triangles_up = [celda("▲")] * 12
    print(linea_con_divisiones(triangles_up))
    print(separador())

    # Triángulos inferiores
    triangles_down = [celda("▼")] * 12
    print(linea_con_divisiones(triangles_down))

    # Fila inferior: se imprime de abajo (índice 0) hacia arriba (índice alto)
    for fila in range(0, alto_col):
        fila_inf = [col[fila] for col in columnas_inf]
        print(linea_con_divisiones(fila_inf))

    print(separador())
    print("   " + "".join(cab_inf[:6]) + " " + "".join(cab_inf[6:]))

    # --- Barra y fuera ---
    bar_blanco = len(self.__bar__.get("blanco", []))
    bar_negro = len(self.__bar__.get("negro", []))
    off_blanco = len(self.__final__.get("blanco", []))
    off_negro = len(self.__final__.get("negro", []))
    print(f"\nBarra: Blanco={bar_blanco}  Negro={bar_negro}   |   Final: Blanco={off_blanco}  Negro={off_negro}")

## Prompt

### Hace falta implementar que cuando sean dos valores iguales se dupliquen y tengas 4 valores en el dado, debo implementar este método en la clase Dice

## Response

    def movimientos(self):
        """
        Devuelve la lista de movimientos disponibles según la tirada actual.
        Si es doble, devuelve cuatro veces ese valor.
        Si no, devuelve los dos valores.
        """
        if self.dobles():
            return [self.__valor__[0]] * 4
        else:
            return self.__valor__[:]

## Prompt

### Debo hacer los movimientos para cada jugador, en que clase deberia hacerlo? Debo hacer que en el cli muestre los movimientos posibles, ej, puedes mover a la casilla 13, 16, y asi. Ademas debo implementar el sistema de movimientos con excepciones para los errores

## Response

¡Muy buenas preguntas!

1. ¿En qué clase implementar los movimientos?
La lógica de los movimientos (validar, calcular posibles movimientos, mover fichas) debe estar principalmente en la clase Board.

El tablero sabe dónde están las fichas y puede validar si un movimiento es legal.
Puedes tener métodos como:
mover_ficha(origen, destino, color)
movimientos_posibles(posicion, dados, color)
es_movimiento_valido(origen, destino, color)
La clase Game puede coordinar el flujo (turnos, dados, ganador), pero la lógica de mover fichas y validar va en Board.

2. ¿Cómo mostrar los movimientos posibles en el CLI?
En el CLI, llama a un método de Board que te devuelva una lista de movimientos posibles para el jugador actual y los dados lanzados.
Ejemplo:
3. ¿Cómo implementar el sistema de movimientos con excepciones?
En Board, cuando intentes mover una ficha, si el movimiento es inválido, lanza una excepción personalizada (por ejemplo, MovimientoInvalido(Exception)).
En el CLI, usa un bloque try/except para capturar el error y mostrar un mensaje amigable al usuario.
Ejemplo:

Resumen de responsabilidades
Board: Lógica de movimientos, validaciones, estado del tablero.
Game: Turnos, flujo general, interacción entre jugadores, tablero y dados.
CLI: Interfaz con el usuario, muestra los movimientos posibles y gestiona la entrada/salida.
¿Quieres que te ayude a definir la estructura de los métodos en Board o a crear la excepción personalizada?

## Prompt

### Ayudame a comenzar con los metodos para mi clase checkers para poder realizar movimientos en el tablero, ademas hay que utilizar try para los errores

## Response

class MovimientoInvalido(Exception):
    """Excepción para movimientos inválidos en Backgammon."""
    pass

class Checkers:
    @staticmethod
    def es_movimiento_valido(board, jugador, origen, destino, dado):
        """
        Verifica si un movimiento es válido según las reglas básicas.
        Lanza MovimientoInvalido si no lo es.
        """
        color = jugador.color()
        puntos = board._Board__points__
        # Ejemplo de validación básica:
        if origen < 0 or origen > 23 or destino < 0 or destino > 23:
            raise MovimientoInvalido("Origen o destino fuera del tablero.")
        if not puntos[origen] or puntos[origen][0] != color:
            raise MovimientoInvalido("No hay ficha propia en el origen.")
        if abs(destino - origen) != dado * jugador._Player__direccion__:
            raise MovimientoInvalido("El destino no corresponde al dado y dirección.")
        # Puedes agregar más validaciones aquí (ocupación, capturas, etc.)

    @staticmethod
    def mover(board, jugador, origen, destino, dado):
        """
        Intenta mover una ficha. Lanza MovimientoInvalido si no es posible.
        """
        Checkers.es_movimiento_valido(board, jugador, origen, destino, dado)
        color = jugador.color()
        puntos = board._Board__points__
        # Realiza el movimiento
        puntos[origen].pop()
        puntos[destino].append(color)
        # Aquí puedes agregar lógica para capturas, barra, borne-off, etc.
    
## Prompt

### Como hago para que muestre los posibles movimientos a hacer desde la casilla que selecciones al principio para mover

## Response

    @staticmethod
    def destinos_posibles(board, jugador, origen, dados):
        color = jugador.color() if callable(jugador.color) else jugador.color
        direccion = jugador.direccion() if callable(jugador.direccion) else jugador.direccion
        puntos = board.__points__
        destinos = []
        for dado in dados:
            destino = origen + direccion * dado
            if 0 <= destino <= 23:
                try:
                    Checkers.es_movimiento_valido(board, jugador, origen, destino, dado)
                    destinos.append(destino)
                except MovimientoInvalido:
                    continue
        return destinos

## Prompt

### No funciona lo de si hay movimientos disponibles ya que elegi una casilla en la cual si podia mover y me decia que no hay movimientos disponibles

## Response

Cambia la validación por:

    if destino != origen + direccion * dado:
        raise MovimientoInvalido("El destino no corresponde al dado y dirección.")

## Prompt

### Al ejecutar el primer turno y hacer el primer movimiento, no deja hacer el segundo movimiento con el otro dado restante y pasa al otro turno, ademas, al pasar de turno sigue siendo el mismo jugador cuando deberia pasar al otro jugador

## Response

 
    while True:
        print(f"Turno de: {game.jugador_actual().nombre()} ({game.jugador_actual().color()})")

        resultado = dado.roll()
        print(f"Dados: {resultado}")
        dados_disponibles = dado.duplicar()
        movimientos_restantes = dados_disponibles.copy()

        # Bucle para usar todos los dados del turno
        while movimientos_restantes:
            board.mostrar_tablero_cli()
            print(f"Dados restantes: {movimientos_restantes}")
            try:
                origen = int(input("Desde qué punto quieres mover? ")) - 1

                # destinos válidos para cualquiera de los dados restantes
                destinos = Checkers.destinos_posibles(board, game.jugador_actual(), origen, movimientos_restantes)
                if not destinos:
                    print(f"No hay movimientos posibles desde la casilla {origen+1} con los dados actuales.")
                    # Si no hay movimientos desde este origen, permite elegir otro origen
                    # pero si no hay movimientos en absoluto con los dados restantes, corta el turno
                    hay_algun_mov = False
                    for i in range(24):
                        if board.__points__[i] and board.__points__[i][0] == game.jugador_actual().color():
                            if Checkers.destinos_posibles(board, game.jugador_actual(), i, movimientos_restantes):
                                hay_algun_mov = True
                                break
                    if not hay_algun_mov:
                        print("No quedan movimientos posibles con los dados restantes.")
                        break
                    continue

                print(f"Puedes mover desde {origen+1} a las casillas: {[d+1 for d in destinos]}")
                destino = int(input("A qué punto quieres mover? ")) - 1

                # Detectar qué dado corresponde al movimiento elegido
                dado_usado = None
                dirj = game.jugador_actual().direccion()
                for d in movimientos_restantes:
                    if destino == origen + dirj * d:
                        dado_usado = d
                        break
                if dado_usado is None:
                    print("Movimiento inválido para los dados disponibles.")
                    continue

                Checkers.mover(board, game.jugador_actual(), origen, destino, dado_usado)
                movimientos_restantes.remove(dado_usado)
                board.mostrar_tablero_cli()

            except MovimientoInvalido as e:
                print(f"Error: {e}")
            except ValueError:
                print("Entrada inválida.")
            except Exception as e:
                print(f"Error inesperado: {e}")

            # Si no quedan movimientos posibles con los dados restantes, termina el turno
            if movimientos_restantes:
                hay_algun_mov = False
                for i in range(24):
                    if board.__points__[i] and board.__points__[i][0] == game.jugador_actual().color():
                        if Checkers.destinos_posibles(board, game.jugador_actual(), i, movimientos_restantes):
                            hay_algun_mov = True
                            break
                if not hay_algun_mov:
                    print("No quedan movimientos posibles con los dados restantes.")
                    break

        game.cambiar_turno()