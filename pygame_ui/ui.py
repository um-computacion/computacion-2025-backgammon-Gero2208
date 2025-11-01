"""
Este módulo implementa una interfaz gráfica de usuario (GUI) para el juego de
Backgammon utilizando la biblioteca Pygame.
"""
import pygame
from core.game import Game
from core.player import Player
from core.exceptions import BackgammonException

# --- Constantes ---
ANCHO_VENTANA = 1200
ALTO_VENTANA = 800

# --- Colores ---
COLOR_FONDO = (210, 180, 140)  # Un color madera claro
COLOR_PICO_1 = (139, 69, 19)  # Marrón oscuro
COLOR_PICO_2 = (245, 245, 220)  # Beige
COLOR_BARRA = (100, 100, 100)  # Gris para la barra
COLOR_FICHA_BLANCA = (255, 255, 255)
COLOR_FICHA_NEGRA = (0, 0, 0)
COLOR_TEXTO = (20, 20, 20)
COLOR_BORDE = (50, 30, 10)
COLOR_CONTADOR_BG = (255, 255, 200)
COLOR_CONTADOR_BORDE = (200, 0, 0)
COLOR_DESTINO = (30, 180, 30)  # Resaltado de destinos posibles
# NUEVO: colores botón bear-off
COLOR_BOTON = (40, 160, 40)
COLOR_BOTON_DIS = (140, 140, 140)
COLOR_BOTON_TEXTO = (255, 255, 255)

# --- Dimensiones del tablero ---
MARGEN = 50
ANCHO_PICO = 70
ALTO_PICO = 280
ANCHO_BARRA = 60
ESPACIO_FICHAS = 40  # Espacio entre fichas para que no se salgan del triángulo
PANEL_INFO_H = 120   # Altura del panel inferior

# Helper de layout dinámico (ajusta el tablero a la ventana)
def _calc_layout():
    # Área del tablero (excluye panel inferior)
    board_left = MARGEN
    board_right = ANCHO_VENTANA - MARGEN
    board_top = MARGEN
    board_bottom = ALTO_VENTANA - PANEL_INFO_H - MARGEN
    board_width = board_right - board_left
    board_height = board_bottom - board_top

    bar_w = ANCHO_BARRA
    col_w = (board_width - bar_w) / 12.0  # ancho de cada columna/pico
    tri_w = col_w
    tri_h = board_height / 2.0 - 8
    center_bar_x = board_left + 6 * col_w

    return {
        "board_left": board_left,
        "board_right": board_right,
        "board_top": board_top,
        "board_bottom": board_bottom,
        "board_width": board_width,
        "board_height": board_height,
        "bar_w": bar_w,
        "col_w": col_w,
        "tri_w": tri_w,
        "tri_h": tri_h,
        "center_bar_x": center_bar_x
    }

# --- Funciones auxiliares botón Bear-off ---
def _rect_boton_bearoff():
    # Botón en el panel inferior, derecha
    return pygame.Rect(ANCHO_VENTANA - 200, ALTO_VENTANA - PANEL_INFO_H + 25, 160, 60)

def dibujar_boton_bearoff(pantalla, habilitado):
    """
    Dibuja un botón para la acción de "bear off" (sacar fichas).

    Args:
        pantalla (pygame.Surface): La superficie donde dibujar.
        habilitado (bool): True si el botón debe aparecer como activo.
    """
    rect = _rect_boton_bearoff()
    color = COLOR_BOTON if habilitado else COLOR_BOTON_DIS
    pygame.draw.rect(pantalla, color, rect, border_radius=10)
    pygame.draw.rect(pantalla, COLOR_BORDE, rect, 3, border_radius=10)
    fuente = pygame.font.Font(None, 40)
    texto = fuente.render("Sacar", True, COLOR_BOTON_TEXTO)
    text_rect = texto.get_rect(center=rect.center)
    pantalla.blit(texto, text_rect)

# --- Funciones de Dibujado ---

def dibujar_tablero(pantalla):
    """
    Dibuja el tablero de Backgammon en la pantalla con diseño mejorado.

    Esto incluye el fondo, los picos triangulares y la barra central.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
    """
    # Fondo general
    pantalla.fill(COLOR_BORDE)

    lyt = _calc_layout()

    # Rectángulo del tablero principal (ocupa todo el área disponible)
    rect_tablero = pygame.Rect(
        int(lyt["board_left"] - 20),
        int(lyt["board_top"] - 20),
        int(lyt["board_width"] + 40),
        int(lyt["board_height"] + 40)
    )
    pygame.draw.rect(pantalla, COLOR_FONDO, rect_tablero, border_radius=8)
    pygame.draw.rect(pantalla, COLOR_BORDE, rect_tablero, 5, border_radius=8)

    # Dibujar la barra central
    x_barra = int(lyt["center_bar_x"])
    y_barra = int(lyt["board_top"])
    alto_barra = int(lyt["board_height"])
    pygame.draw.rect(pantalla, COLOR_BARRA,
                     (x_barra, y_barra, int(lyt["bar_w"]), alto_barra), border_radius=4)
    pygame.draw.rect(pantalla, COLOR_BORDE,
                     (x_barra, y_barra, int(lyt["bar_w"]), alto_barra), 3, border_radius=4)

    # Dibujar los picos superiores e inferiores a lo largo de todo el ancho
    for i in range(12):
        color = COLOR_PICO_1 if i % 2 == 0 else COLOR_PICO_2

        # X base del pico i contando desde la izquierda, con barra en el medio
        x_base = lyt["board_left"] + i * lyt["col_w"]
        if i >= 6:
            x_base += lyt["bar_w"]

        # Picos superiores (apuntan hacia abajo)
        puntos_sup = [
            (x_base, lyt["board_top"]),
            (x_base + lyt["tri_w"], lyt["board_top"]),
            (x_base + lyt["tri_w"] / 2.0, lyt["board_top"] + lyt["tri_h"])
        ]
        pygame.draw.polygon(pantalla, color, puntos_sup)
        pygame.draw.polygon(pantalla, COLOR_BORDE, puntos_sup, 2)

        # Picos inferiores (apuntan hacia arriba)
        y_base_inf = lyt["board_bottom"]
        puntos_inf = [
            (x_base, y_base_inf),
            (x_base + lyt["tri_w"], y_base_inf),
            (x_base + lyt["tri_w"] / 2.0, y_base_inf - lyt["tri_h"])
        ]
        pygame.draw.polygon(pantalla, color, puntos_inf)
        pygame.draw.polygon(pantalla, COLOR_BORDE, puntos_inf, 2)

def _dibujar_fichas_barra(pantalla, barra, lyt, radio_ficha, espacio):
    """Dibuja las fichas en la barra."""
    x_barra = int(lyt["center_bar_x"] + lyt["bar_w"] / 2.0)
    y_centro = (lyt["board_top"] + lyt["board_bottom"]) / 2.0
    y_base_blanco = y_centro - radio_ficha - 10
    y_base_negro = y_centro + radio_ficha + 10

    for color in ["blanco", "negro"]:
        y_base = y_base_blanco if color == "blanco" else y_base_negro
        fichas_barra = barra.get(color, [])
        direccion = -1 if color == "blanco" else 1
        for j in range(min(len(fichas_barra), 5)):
            color_ficha = COLOR_FICHA_BLANCA if color == "blanco" else COLOR_FICHA_NEGRA
            y_pos = y_base + j * espacio * direccion
            pygame.draw.circle(pantalla, color_ficha, (x_barra, int(y_pos)), radio_ficha)
            pygame.draw.circle(pantalla, COLOR_BORDE, (x_barra, int(y_pos)), radio_ficha, 3)

        if len(fichas_barra) > 5:
            fuente = pygame.font.Font(None, 30)
            texto_count = fuente.render(str(len(fichas_barra)), True, COLOR_CONTADOR_BORDE)
            y_count = y_base + 4.6 * espacio * direccion
            rect_count = pygame.Rect(x_barra - 20, int(y_count) - 14, 40, 28)
            pygame.draw.rect(pantalla, COLOR_CONTADOR_BG, rect_count)
            pygame.draw.rect(pantalla, COLOR_CONTADOR_BORDE, rect_count, 2)
            text_rect = texto_count.get_rect(center=rect_count.center)
            pantalla.blit(texto_count, text_rect)


def dibujar_fichas(pantalla, board):
    """
    Dibuja las fichas centradas en cada casilla con contador para más de 5.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
        board (Board): El objeto del tablero que contiene el estado de las fichas.
    """
    lyt = _calc_layout()

    puntos = board.get_points()
    barra = board.get_bar()

    # Radio en función del ancho de columna para encajar visualmente
    radio_ficha = int(min(28, lyt["col_w"] * 0.45))
    espacio = min(ESPACIO_FICHAS, max(2 * radio_ficha - 4, 28))

    _dibujar_fichas_barra(pantalla, barra, lyt, radio_ficha, espacio)
    _dibujar_fichas_picos(pantalla, puntos, lyt, radio_ficha, espacio)


def _dibujar_fichas_picos(pantalla, puntos, lyt, radio_ficha, espacio):
    """Dibuja las fichas en los picos."""
    for i, punto in enumerate(puntos):
        if not punto:
            continue

        color_str = punto[0]
        color_ficha = COLOR_FICHA_BLANCA if color_str == "blanco" else COLOR_FICHA_NEGRA
        num_fichas = len(punto)

        # Centro X del pico i (respeta orientación inferior 0..11
        # derecha a izquierda y superior 12..23 izquierda a derecha)
        if i < 12:  # Picos inferiores
            # desde la derecha hacia la izquierda
            col_idx = i
            x_center = lyt["board_right"] - (col_idx * lyt["col_w"]) - (lyt["col_w"] / 2.0)
            if col_idx >= 6:
                x_center -= lyt["bar_w"]
            y_base = lyt["board_bottom"] - radio_ficha - 8
            direccion = -1
        else:  # Picos superiores
            col_idx = i - 12
            x_center = lyt["board_left"] + (col_idx * lyt["col_w"]) + (lyt["col_w"] / 2.0)
            if col_idx >= 6:
                x_center += lyt["bar_w"]
            y_base = lyt["board_top"] + radio_ficha + 8
            direccion = 1

        # Dibujar hasta 5 fichas centradas
        for j in range(min(num_fichas, 5)):
            y = y_base + (j * espacio * direccion)
            pygame.draw.circle(pantalla, color_ficha, (int(x_center), int(y)), radio_ficha)
            pygame.draw.circle(pantalla, COLOR_BORDE, (int(x_center), int(y)), radio_ficha, 3)

        # Contador si hay más de 5
        if num_fichas > 5:
            fuente = pygame.font.Font(None, 34)
            texto_count = fuente.render(str(num_fichas), True, COLOR_CONTADOR_BORDE)
            y_count = y_base + (4.7 * espacio * direccion)
            rect_count = pygame.Rect(int(x_center) - 20, int(y_count) - 14, 40, 28)
            pygame.draw.rect(pantalla, COLOR_CONTADOR_BG, rect_count)
            pygame.draw.rect(pantalla, COLOR_CONTADOR_BORDE, rect_count, 2)
            text_rect = texto_count.get_rect(center=rect_count.center)
            pantalla.blit(texto_count, text_rect)

def get_pico_desde_pos(pos):
    """
    Convierte (x, y) a índice de pico (0-23) usando el layout dinámico.

    Args:
        pos (tuple[int, int]): Una tupla con las coordenadas x e y del clic.

    Returns:
        int or None: El índice del pico (0-23) si el clic está en un pico,
                     o None en caso contrario.
    """
    x, y = pos
    lyt = _calc_layout()

    # Fuera del área vertical del tablero
    if y < lyt["board_top"] or y > lyt["board_bottom"]:
        return None

    # Ajuste X al sistema de columnas con barra
    x_rel = x - lyt["board_left"]
    # FIX: usar ancho relativo del tablero en vez de comparar con coordenada absoluta
    if x_rel < 0 or x_rel > lyt["board_width"]:
        return None

    # En la barra central
    if 6 * lyt["col_w"] < x_rel < 6 * lyt["col_w"] + lyt["bar_w"]:
        return None

    # Ajustar por la barra si está a la derecha
    if x_rel > 6 * lyt["col_w"]:
        x_rel -= lyt["bar_w"]

    # Índice de columna
    col = int(x_rel // lyt["col_w"])
    if not 0 <= col < 12:
        return None

    # Superior o inferior
    if y < (lyt["board_top"] + lyt["board_bottom"]) / 2.0:
        return 12 + col  # 12..23
    return 11 - col     # 11..0

def dibujar_seleccion(pantalla, pico):
    """
    Resalta un pico seleccionado con borde amarillo usando layout dinámico.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
        pico (int or None): El índice del pico a resaltar.
    """
    if pico is None:
        return

    lyt = _calc_layout()

    if pico < 12:  # Picos inferiores
        col_idx = pico
        x_base = lyt["board_right"] - (col_idx + 1) * lyt["col_w"]
        if col_idx >= 6:
            x_base -= lyt["bar_w"]
        puntos = [
            (x_base, lyt["board_bottom"]),
            (x_base + lyt["col_w"], lyt["board_bottom"]),
            (x_base + lyt["col_w"] / 2.0, lyt["board_bottom"] - lyt["tri_h"])
        ]
    else:  # Picos superiores
        col_idx = pico - 12
        x_base = lyt["board_left"] + col_idx * lyt["col_w"]
        if col_idx >= 6:
            x_base += lyt["bar_w"]
        puntos = [
            (x_base, lyt["board_top"]),
            (x_base + lyt["col_w"], lyt["board_top"]),
            (x_base + lyt["col_w"] / 2.0, lyt["board_top"] + lyt["tri_h"])
        ]

    pygame.draw.polygon(pantalla, (255, 255, 0), puntos, 5)

def dibujar_pantalla_nombres(pantalla, nombre1, nombre2, jugador_actual):
    """
    Dibuja la pantalla para ingresar los nombres de los jugadores.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
        nombre1 (str): El nombre del jugador 1.
        nombre2 (str): El nombre del jugador 2.
        jugador_actual (int): El jugador que está ingresando su nombre (1 o 2).
    """
    pantalla.fill(COLOR_FONDO)
    fuente_titulo = pygame.font.Font(None, 72)
    fuente_texto = pygame.font.Font(None, 40)
    fuente_input = pygame.font.Font(None, 36)
    # Título
    titulo = fuente_titulo.render("BACKGAMMON", True, COLOR_BORDE)
    pantalla.blit(titulo, (ANCHO_VENTANA//2 - titulo.get_width()//2, 80))
    # Instrucciones
    if jugador_actual == 1:
        prompt = "Nombre del Jugador 1 (Blanco):"
        nombre_actual = nombre1
    else:
        prompt = "Nombre del Jugador 2 (Negro):"
        nombre_actual = nombre2
    texto_prompt = fuente_texto.render(prompt, True, COLOR_BORDE)
    pantalla.blit(texto_prompt, (ANCHO_VENTANA//2 - texto_prompt.get_width()//2, 250))
    # Caja de input
    input_rect = pygame.Rect(ANCHO_VENTANA//2 - 250, 320, 500, 60)
    pygame.draw.rect(pantalla, COLOR_FICHA_BLANCA, input_rect)
    pygame.draw.rect(pantalla, COLOR_BORDE, input_rect, 4)
    texto_nombre = fuente_input.render(nombre_actual, True, COLOR_BORDE)
    pantalla.blit(texto_nombre, (input_rect.x + 15, input_rect.y + 15))
    # Instrucción
    instruccion = fuente_texto.render("Presiona ENTER para continuar", True, COLOR_TEXTO)
    pantalla.blit(instruccion, (ANCHO_VENTANA//2 - instruccion.get_width()//2, 450))


def dibujar_pantalla_inicio(pantalla):
    """
    Muestra una pantalla de inicio mejorada.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
    """
    fuente_titulo = pygame.font.Font(None, 80)
    fuente_subtitulo = pygame.font.Font(None, 40)
    pantalla.fill(COLOR_FONDO)
    titulo = fuente_titulo.render("BACKGAMMON", True, COLOR_BORDE)
    rect_titulo = titulo.get_rect(center=(ANCHO_VENTANA / 2, ALTO_VENTANA / 2 - 50))
    pantalla.blit(titulo, rect_titulo)
    subtitulo = fuente_subtitulo.render("Clic para empezar", True, COLOR_TEXTO)
    rect_subtitulo = subtitulo.get_rect(center=(ANCHO_VENTANA / 2, ALTO_VENTANA / 2 + 50))
    pantalla.blit(subtitulo, rect_subtitulo)


def dibujar_pantalla_fin(pantalla, ganador):
    """
    Muestra la pantalla de fin de juego con diseño mejorado.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
        ganador (Player): El jugador que ha ganado la partida.
    """
    fuente_grande = pygame.font.Font(None, 72)
    fuente_pequena = pygame.font.Font(None, 40)

    pantalla.fill(COLOR_FONDO)

    texto_ganador = f"¡Ganador: {ganador.nombre()}!"
    sup_ganador = fuente_grande.render(texto_ganador, True, COLOR_BORDE)
    rect_ganador = sup_ganador.get_rect(center=(ANCHO_VENTANA / 2, ALTO_VENTANA / 2 - 50))
    pantalla.blit(sup_ganador, rect_ganador)
    color_text = f"({ganador.color().capitalize()})"
    sup_color = fuente_pequena.render(color_text, True, COLOR_TEXTO)
    rect_color = sup_color.get_rect(center=(ANCHO_VENTANA / 2, ALTO_VENTANA / 2 + 20))
    pantalla.blit(sup_color, rect_color)

    texto_continuar = "Clic para salir"
    sup_continuar = fuente_pequena.render(texto_continuar, True, COLOR_TEXTO)
    rect_continuar = sup_continuar.get_rect(center=(ANCHO_VENTANA / 2, ALTO_VENTANA / 2 + 100))
    pantalla.blit(sup_continuar, rect_continuar)


# --- Ayudas para destinos posibles ---

def _point_is_open(points, idx, color):
    """
    Devuelve True si el punto idx está abierto para color:
    - vacío
    - mismo color
    - una ficha rival (comible)
    """
    punto = points[idx]
    if not punto:
        return True
    top_color = punto[0]
    count = len(punto)
    if top_color == color:
        return True
    return count == 1


def calcular_destinos_posibles(game, board, origen):
    """
    Calcula destinos posibles desde 'origen' con los dados actuales.
    No simula el juego; aplica reglas básicas de ocupación.
    """
    if origen is None:
        return []

    color = game.jugador_actual().color()
    points = board.get_points()
    destinos = set()

    # Dirección según color (basado en mapeo de reingreso existente)
    # blanco: índices aumentan; negro: índices disminuyen
    for d in set(game.movimientos_restantes):
        if color == "blanco":
            dest = origen + d
        else:
            dest = origen - d

        if 0 <= dest <= 23 and _point_is_open(points, dest, color):
            destinos.add(dest)

    return sorted(destinos)


def dibujar_destinos_posibles(pantalla, destinos):
    """
    Resalta múltiples picos destino con un borde verde.
    """
    if not destinos:
        return

    lyt = _calc_layout()
    for pico in destinos:
        if pico < 12:  # Inferiores
            col_idx = pico
            x_base = lyt["board_right"] - (col_idx + 1) * lyt["col_w"]
            if col_idx >= 6:
                x_base -= lyt["bar_w"]
            puntos = [
                (x_base, lyt["board_bottom"]),
                (x_base + lyt["col_w"], lyt["board_bottom"]),
                (x_base + lyt["col_w"] / 2.0, lyt["board_bottom"] - lyt["tri_h"])
            ]
        else:  # Superiores
            col_idx = pico - 12
            x_base = lyt["board_left"] + col_idx * lyt["col_w"]
            if col_idx >= 6:
                x_base += lyt["bar_w"]
            puntos = [
                (x_base, lyt["board_top"]),
                (x_base + lyt["col_w"], lyt["board_top"]),
                (x_base + lyt["col_w"] / 2.0, lyt["board_top"] + lyt["tri_h"])
            ]
        pygame.draw.polygon(pantalla, COLOR_DESTINO, puntos, 6)


# --- Funciones de Manejo de Eventos ---

def _buscar_punto_mas_alto_blanco(board):
    """
    Encuentra el punto más alto (índice más bajo en casa) ocupado por
    el jugador blanco. Exclusivo para la lógica de la UI.
    """
    puntos = board.get_points()
    for i in range(18, 24):
        if puntos[i] and puntos[i][0] == "blanco":
            return i
    return None  # No debería ocurrir si se llama correctamente


def _manejar_clic_bear_off(game, pico_seleccionado):
    """Maneja el clic en el botón de bear off."""
    if game.todas_fichas_en_casa() and pico_seleccionado is not None:
        origen = pico_seleccionado
        for dado in list(game.movimientos_restantes):
            try:
                game.sacar_ficha(origen, dado)
                return None, [], f"Sacaste desde {origen + 1} con dado {dado}"
            except BackgammonException:
                continue
        return pico_seleccionado, [], "No puedes sacar con los dados actuales."
    return pico_seleccionado, [], ""


def _manejar_reingreso_barra(game, pico, pico_seleccionado):
    """Maneja el reingreso de fichas desde la barra."""
    if pico is not None:
        dado = abs(pico - 24) if game.jugador_actual().color() == "negro" else pico + 1
        try:
            game.reingresar_desde_barra(dado)
            return None, [], ""
        except BackgammonException as e:
            return pico_seleccionado, [], f"Error: {e}"
    return pico_seleccionado, [], ""


def _manejar_todas_en_casa(game, board, pico, pico_seleccionado):
    """Maneja los eventos cuando todas las fichas están en casa."""
    if pico_seleccionado is None and pico is not None:
        if board.get_points()[pico] and board.get_points()[pico][0] == game.jugador_actual().color():
            return pico, calcular_destinos_posibles(game, board, pico), ""
    elif pico_seleccionado is not None:
        origen = pico_seleccionado
        destino = pico
        if destino is None:
            # Intento de bear off al hacer clic fuera del tablero
            for dado in list(game.movimientos_restantes):
                try:
                    game.sacar_ficha(origen, dado)
                    return None, [], f"Sacaste desde {origen + 1} con dado {dado}"
                except BackgammonException:
                    # Si falla y es el jugador blanco, podría ser por la regla del punto más alto
                    if game.jugador_actual().color() == "blanco":
                        punto_alto = _buscar_punto_mas_alto_blanco(board)
                        if punto_alto is not None and punto_alto != origen:
                            try:
                                # Reintentar con el punto correcto
                                game.sacar_ficha(punto_alto, dado)
                                return None, [], f"Movimiento corregido a {punto_alto + 1}"
                            except BackgammonException:
                                continue
                    continue
            return pico_seleccionado, [], "No puedes sacar con los dados actuales."

        if destino == origen:
            return origen, calcular_destinos_posibles(game, board, origen), \
                "Clic en un destino válido o fuera del tablero para sacar."
        try:
            game.mover_ficha(origen, destino)
            return None, [], ""
        except BackgammonException:
            return origen, calcular_destinos_posibles(game, board, origen), "Movimiento inválido."
    return pico_seleccionado, [], ""


def _manejar_juego_normal(game, board, pico, pico_seleccionado, mensaje_info):
    """Maneja los eventos del juego normal."""
    if pico is not None:
        if pico_seleccionado is None:
            if (board.get_points()[pico] and
                    board.get_points()[pico][0] == game.jugador_actual().color()):
                return pico, calcular_destinos_posibles(game, board, pico), ""
        else:
            origen = pico_seleccionado
            destino = pico
            if destino == origen:
                return origen, calcular_destinos_posibles(game, board, origen), mensaje_info
            try:
                game.mover_ficha(origen, destino)
            except BackgammonException as e:
                mensaje_info = f"Error: {e}"
            return None, [], mensaje_info
    return pico_seleccionado, [], mensaje_info


def manejar_eventos_jugando(evento, game, board, pico_seleccionado,
                            destinos_posibles, mensaje_info):
    """
    Gestiona los eventos y retorna (nuevo_pico_seleccionado,
    nuevos_destinos_posibles, nuevo_mensaje_info).
    """
    # Solo actuar con botón izquierdo; botón derecho cancela selección
    if evento.type != pygame.MOUSEBUTTONDOWN:
        return pico_seleccionado, destinos_posibles, mensaje_info
    if getattr(evento, "button", 1) == 3:  # clic derecho: deseleccionar y limpiar
        return None, [], mensaje_info
    if getattr(evento, "button", 1) != 1:
        return pico_seleccionado, destinos_posibles, mensaje_info

    pos_clic = pygame.mouse.get_pos()
    pico = get_pico_desde_pos(pos_clic)

    # Click en botón Bear-off (solo con botón izquierdo)
    if _rect_boton_bearoff().collidepoint(pos_clic):
        return _manejar_clic_bear_off(game, pico_seleccionado)

    # Si hay fichas en barra, reingresar directo (sin selección)
    if game.jugador_tiene_fichas_en_barra():
        return _manejar_reingreso_barra(game, pico, pico_seleccionado)

    # Si todas en casa: permitir selección y mover (sacar solo por botón)
    if game.todas_fichas_en_casa():
        return _manejar_todas_en_casa(game, board, pico, pico_seleccionado)

    # Juego normal
    return _manejar_juego_normal(game, board, pico, pico_seleccionado, mensaje_info)


def _dibujar_panel_info(pantalla, game, nombre1, nombre2, mensaje_info):
    """Dibuja el panel de información inferior."""
    fuente = pygame.font.Font(None, 38)
    fuente_info = pygame.font.Font(None, 30)

    jugador_actual = game.jugador_actual()
    nombre_actual = nombre1 if jugador_actual.color() == "blanco" else nombre2

    panel_rect = pygame.Rect(20, ALTO_VENTANA - PANEL_INFO_H + 10,
                             ANCHO_VENTANA - 40, PANEL_INFO_H - 20)
    pygame.draw.rect(pantalla, COLOR_FONDO, panel_rect, border_radius=8)
    pygame.draw.rect(pantalla, COLOR_BORDE, panel_rect, 5, border_radius=8)

    texto_turno = f"Turno: {nombre_actual} ({jugador_actual.color().capitalize()})"
    superficie_turno = fuente.render(texto_turno, True, COLOR_BORDE)
    pantalla.blit(superficie_turno, (50, ALTO_VENTANA - PANEL_INFO_H + 20))

    dados = game.movimientos_restantes
    texto_dados = f"Dados: {dados}"
    superficie_dados = fuente.render(texto_dados, True, COLOR_BORDE)
    pantalla.blit(superficie_dados, (50, ALTO_VENTANA - PANEL_INFO_H + 60))

    if mensaje_info:
        superficie_info = fuente_info.render(mensaje_info, True, (200, 0, 0))
        pantalla.blit(
            superficie_info,
            (ANCHO_VENTANA // 2 - superficie_info.get_width() // 2, ALTO_VENTANA - PANEL_INFO_H + 60)
        )


def dibujar_info_turno(pantalla, game, mensaje_info, nombre1,
                       nombre2, pico_seleccionado, board):
    """
    Muestra información del turno con los nombres y
    dibuja botón de 'Sacar' (bear-off).
    """
    _dibujar_panel_info(pantalla, game, nombre1, nombre2, mensaje_info)

    habilitado = False
    if game.todas_fichas_en_casa():
        if pico_seleccionado is not None:
            puntos = board.get_points()
            jugador_actual = game.jugador_actual()
            if puntos[pico_seleccionado] and puntos[pico_seleccionado][0] == jugador_actual.color():
                habilitado = True
    dibujar_boton_bearoff(pantalla, habilitado)


def _manejar_estado_nombres(evento, estado, nombre1, nombre2, jugador_nombre_actual):
    """Maneja los eventos en el estado de ingreso de nombres."""
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RETURN:
            if jugador_nombre_actual == 1 and nombre1.strip():
                jugador_nombre_actual = 2
            elif jugador_nombre_actual == 2 and nombre2.strip():
                p1 = Player("blanco", nombre1, 1)
                p2 = Player("negro", nombre2, -1)
                game = Game(p1, p2)
                board = game.get_board_status()
                game.decidir_iniciador()
                game.lanzar_dados()
                return "JUGANDO", nombre1, nombre2, jugador_nombre_actual, game, board
        elif evento.key == pygame.K_BACKSPACE:
            if jugador_nombre_actual == 1:
                nombre1 = nombre1[:-1]
            else:
                nombre2 = nombre2[:-1]
        else:
            if len(evento.unicode) > 0 and evento.unicode.isprintable():
                if jugador_nombre_actual == 1 and len(nombre1) < 20:
                    nombre1 += evento.unicode
                elif jugador_nombre_actual == 2 and len(nombre2) < 20:
                    nombre2 += evento.unicode
    return estado, nombre1, nombre2, jugador_nombre_actual, None, None


def _manejar_estado_jugando(pantalla, game, board, destinos_posibles,
                            pico_seleccionado, nombre1, nombre2, mensaje_info):
    """Maneja la lógica y el dibujo en el estado de juego."""
    if game and not game.ganador():
        if not game.movimientos_restantes:
            game.cambiar_turno()
            game.lanzar_dados()
            mensaje_info = ""
            if not game.hay_movimientos_posibles():
                mensaje_info = "No tienes movimientos. Turno cedido."
                game.movimientos_restantes = []

        dibujar_tablero(pantalla)
        dibujar_fichas(pantalla, board)
        dibujar_destinos_posibles(pantalla, destinos_posibles)
        dibujar_seleccion(pantalla, pico_seleccionado)
        dibujar_info_turno(pantalla, game, mensaje_info, nombre1,
                           nombre2, pico_seleccionado, board)
        return "JUGANDO", mensaje_info
    return "FIN", mensaje_info


def main():
    """
    Función principal mejorada con entrada de nombres.

    Utiliza una máquina de estados simple para controlar el flujo del juego:
    - NOMBRES: Pantalla para ingresar los nombres de los jugadores.
    - JUGANDO: Bucle principal del juego donde se interactúa con el tablero.
    - FIN: Pantalla que muestra al ganador.
    """
    pygame.init()

    # --- Configuración de la ventana ---
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Backgammon")

    # --- Estado del juego ---
    estado = "NOMBRES"  # NOMBRES, JUGANDO, FIN
    nombre1 = ""
    nombre2 = ""
    jugador_nombre_actual = 1  # 1 o 2
    mensaje_info = ""
    pico_seleccionado = None
    destinos_posibles = []  # NUEVO: destinos resaltados
    game = None
    board = None

    # --- Bucle principal del juego ---
    ejecutando = True
    while ejecutando:
        # --- Gestión de eventos ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            if estado == "NOMBRES":
                estado, nombre1, nombre2, jugador_nombre_actual, game, board = \
                    _manejar_estado_nombres(
                        evento, estado, nombre1, nombre2, jugador_nombre_actual
                    )
            elif estado == "JUGANDO":
                pico_seleccionado, destinos_posibles, mensaje_info = \
                    manejar_eventos_jugando(
                        evento, game, board, pico_seleccionado,
                        destinos_posibles, mensaje_info
                    )
            elif estado == "FIN":
                # Solo salir con clic izquierdo
                if evento.type == pygame.MOUSEBUTTONDOWN and getattr(evento, "button", 1) == 1:
                    ejecutando = False

        # --- Lógica y Dibujo por estado ---
        if estado == "NOMBRES":
            dibujar_pantalla_nombres(pantalla, nombre1, nombre2, jugador_nombre_actual)

        elif estado == "JUGANDO":
            estado, mensaje_info = _manejar_estado_jugando(
                pantalla, game, board, destinos_posibles,
                pico_seleccionado, nombre1, nombre2, mensaje_info
            )

        elif estado == "FIN":
            if game:
                dibujar_pantalla_fin(pantalla, game.ganador())

        # --- Actualización de la pantalla ---
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
