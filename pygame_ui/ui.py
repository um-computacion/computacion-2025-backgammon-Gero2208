import pygame
from core.game import Game
from core.player import Player

# --- Constantes ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

# --- Colores ---
COLOR_FONDO = (210, 180, 140)  # Un color madera claro
COLOR_PICO_1 = (139, 69, 19)   # Marrón oscuro
COLOR_PICO_2 = (245, 245, 220)  # Beige
COLOR_BARRA = (100, 100, 100)  # Gris para la barra
COLOR_FICHA_BLANCA = (255, 255, 255)
COLOR_FICHA_NEGRA = (0, 0, 0)
COLOR_TEXTO = (20, 20, 20)

# --- Dimensiones del tablero ---
MARGEN = 20
ANCHO_PICO = (ANCHO_VENTANA - 2 * MARGEN) // 13  # 12 picos + 1 para la barra
ALTO_PICO = ALTO_VENTANA // 2 - MARGEN
ANCHO_BARRA = ANCHO_PICO


# --- Funciones de Dibujado ---

def dibujar_tablero(pantalla):
    """
    Dibuja el tablero de Backgammon en la pantalla.

    Esto incluye el fondo, los picos triangulares y la barra central.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
    """
    pantalla.fill(COLOR_FONDO)

    # Dibujar los picos
    for i in range(12):
        color = COLOR_PICO_1 if i % 2 == 0 else COLOR_PICO_2
        
        # Picos superiores
        x_base = MARGEN + i * ANCHO_PICO
        if i >= 6:  # Añadir espacio para la barra
            x_base += ANCHO_BARRA
        
        puntos = [(x_base, MARGEN), 
                  (x_base + ANCHO_PICO, MARGEN), 
                  (x_base + ANCHO_PICO / 2, MARGEN + ALTO_PICO)]
        pygame.draw.polygon(pantalla, color, puntos)

        # Picos inferiores
        puntos = [(x_base, ALTO_VENTANA - MARGEN), 
                  (x_base + ANCHO_PICO, ALTO_VENTANA - MARGEN), 
                  (x_base + ANCHO_PICO / 2, ALTO_VENTANA - MARGEN - ALTO_PICO)]
        pygame.draw.polygon(pantalla, color, puntos)

    # Dibujar la barra central
    pygame.draw.rect(pantalla, COLOR_BARRA, 
                     (MARGEN + 6 * ANCHO_PICO, MARGEN, 
                      ANCHO_BARRA, ALTO_VENTANA - 2 * MARGEN))

def dibujar_fichas(pantalla, board):
    """
    Dibuja las fichas en sus posiciones actuales en el tablero.

    Esto incluye las fichas en los picos y en la barra.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
        board (Board): El objeto del tablero que contiene el estado de las fichas.
    """
    puntos = board.get_points()
    bar = board.get_bar()
    radio_ficha = ANCHO_PICO // 2 - 5

    # Dibujar fichas en la barra
    y_base_blanco = ALTO_VENTANA / 2 - radio_ficha
    y_base_negro = ALTO_VENTANA / 2 + radio_ficha
    x_bar = MARGEN + 6 * ANCHO_PICO + ANCHO_BARRA / 2

    for i, color in enumerate(["blanco", "negro"]):
        y_base = y_base_blanco if color == "blanco" else y_base_negro
        for j, ficha in enumerate(bar.get(color, [])):
            color_ficha = COLOR_FICHA_BLANCA if color == "blanco" else COLOR_FICHA_NEGRA
            pygame.draw.circle(pantalla, color_ficha, (int(x_bar), int(y_base - j * 2 * radio_ficha)), radio_ficha)
            pygame.draw.circle(pantalla, (0,0,0), (int(x_bar), int(y_base - j * 2 * radio_ficha)), radio_ficha, 2)

    # Dibujar fichas en los picos
    for i, punto in enumerate(puntos):
        if not punto:
            continue

        color_str = punto[0]
        color_ficha = COLOR_FICHA_BLANCA if color_str == "blanco" else COLOR_FICHA_NEGRA
        
        for j, _ in enumerate(punto):
            # Calcular la posición de la ficha
            if i < 12:  # Picos inferiores
                x = ANCHO_VENTANA - MARGEN - (i * ANCHO_PICO) - ANCHO_PICO / 2
                if i >= 6:
                    x -= ANCHO_BARRA
                y = ALTO_VENTANA - MARGEN - radio_ficha - (j * 2 * radio_ficha)
            else:  # Picos superiores
                x = MARGEN + ((i - 12) * ANCHO_PICO) + ANCHO_PICO / 2
                if (i - 12) >= 6:
                    x += ANCHO_BARRA
                y = MARGEN + radio_ficha + (j * 2 * radio_ficha)

            pygame.draw.circle(pantalla, color_ficha, (int(x), int(y)), radio_ficha)
            # Dibujar un borde para que se distingan
            pygame.draw.circle(pantalla, (0,0,0), (int(x), int(y)), radio_ficha, 2)

def get_pico_desde_pos(pos):
    """
    Convierte las coordenadas de la pantalla (x, y) al índice del pico correspondiente.

    Args:
        pos (tuple[int, int]): Una tupla con las coordenadas x e y del clic.

    Returns:
        int or None: El índice del pico (0-23) si el clic está en un pico,
                     o None en caso contrario.
    """
    x, y = pos
    
    # Fuera de los márgenes verticales
    if not (MARGEN < y < ALTO_VENTANA - MARGEN):
        return None

    # Ajustar x por la barra central
    x_ajustado = x - MARGEN
    if x_ajustado > 6 * ANCHO_PICO:
        x_ajustado -= ANCHO_BARRA

    # Calcular el índice de la columna (0-11)
    col = x_ajustado // ANCHO_PICO
    if not (0 <= col < 12):
        return None

    # Determinar si es un pico superior o inferior
    if y < ALTO_VENTANA / 2:
        # Picos superiores (12-23)
        return int(12 + col)
    else:
        # Picos inferiores (11-0)
        return int(11 - col)

def dibujar_seleccion(pantalla, pico):
    """
    Resalta un pico seleccionado en el tablero.

    Dibuja un borde alrededor del pico para indicar que está seleccionado.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
        pico (int or None): El índice del pico a resaltar.
    """
    if pico is None:
        return

    # Calcular la geometría del pico
    if pico < 12:  # Picos inferiores
        x_base = ANCHO_VENTANA - MARGEN - ((pico + 1) * ANCHO_PICO)
        if pico >= 6:
            x_base -= ANCHO_BARRA
        
        puntos = [(x_base, ALTO_VENTANA - MARGEN), 
                  (x_base + ANCHO_PICO, ALTO_VENTANA - MARGEN), 
                  (x_base + ANCHO_PICO / 2, ALTO_VENTANA - MARGEN - ALTO_PICO)]
    else:  # Picos superiores
        x_base = MARGEN + ((pico - 12) * ANCHO_PICO)
        if (pico - 12) >= 6:
            x_base += ANCHO_BARRA
            
        puntos = [(x_base, MARGEN), 
                  (x_base + ANCHO_PICO, MARGEN), 
                  (x_base + ANCHO_PICO / 2, MARGEN + ALTO_PICO)]

    pygame.draw.polygon(pantalla, (255, 255, 0, 100), puntos, 5)  # Resaltado amarillo semitransparente

def dibujar_pantalla_inicio(pantalla):
    """
    Muestra una pantalla de inicio simple.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
    """
    fuente = pygame.font.Font(None, 50)
    pantalla.fill(COLOR_FONDO)
    texto = fuente.render("Clic para empezar", True, COLOR_TEXTO)
    rect = texto.get_rect(center=(ANCHO_VENTANA / 2, ALTO_VENTANA / 2))
    pantalla.blit(texto, rect)

def dibujar_pantalla_fin(pantalla, ganador):
    """
    Muestra la pantalla de fin de juego con el nombre del ganador.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
        ganador (Player): El jugador que ha ganado la partida.
    """
    fuente_grande = pygame.font.Font(None, 72)
    fuente_pequeña = pygame.font.Font(None, 36)

    pantalla.fill(COLOR_FONDO)

    texto_ganador = f"¡Ganador: {ganador.nombre()}!"
    sup_ganador = fuente_grande.render(texto_ganador, True, COLOR_TEXTO)
    rect_ganador = sup_ganador.get_rect(center=(ANCHO_VENTANA / 2, ALTO_VENTANA / 2 - 50))
    pantalla.blit(sup_ganador, rect_ganador)

    texto_continuar = "Clic para salir"
    sup_continuar = fuente_pequeña.render(texto_continuar, True, COLOR_TEXTO)
    rect_continuar = sup_continuar.get_rect(center=(ANCHO_VENTANA / 2, ALTO_VENTANA / 2 + 100))
    pantalla.blit(sup_continuar, rect_continuar)


# --- Funciones de Manejo de Eventos ---

def manejar_eventos_jugando(evento, game, board, pico_seleccionado):
    """
    Gestiona los eventos de entrada del usuario durante el estado de juego.

    Procesa los clics del ratón para seleccionar y mover fichas, reingresar
    desde la barra y sacar fichas del tablero.

    Args:
        evento (pygame.event.Event): El evento actual de Pygame.
        game (Game): La instancia actual del juego.
        board (Board): El objeto del tablero.
        pico_seleccionado (int or None): El índice del pico actualmente
                                         seleccionado.

    Returns:
        int or None: El nuevo pico seleccionado, o None si no hay selección.
    """
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if game.jugador_tiene_fichas_en_barra():
            pos_clic = pygame.mouse.get_pos()
            pico = get_pico_desde_pos(pos_clic)
            if pico is not None:
                dado = abs(pico - 24) if game.jugador_actual().color() == "negro" else pico + 1
                try: game.reingresar_desde_barra(dado)
                except Exception as e: print(f"Error: {e}")
        
        elif game.todas_fichas_en_casa():
            pos_clic = pygame.mouse.get_pos()
            pico = get_pico_desde_pos(pos_clic)
            if pico_seleccionado is None and pico is not None:
                if board.get_points()[pico] and board.get_points()[pico][0] == game.jugador_actual().color():
                    return pico # Devuelve el nuevo pico seleccionado
            elif pico_seleccionado is not None:
                origen = pico_seleccionado
                destino = pico
                try: game.mover_ficha(origen, destino)
                except Exception:
                    for dado in game.movimientos_restantes:
                        try:
                            game.sacar_ficha(origen, dado)
                            break
                        except Exception: continue
                return None # Deselecciona el pico
        else:
            pos_clic = pygame.mouse.get_pos()
            pico = get_pico_desde_pos(pos_clic)
            if pico is not None:
                if pico_seleccionado is None:
                    if board.get_points()[pico] and board.get_points()[pico][0] == game.jugador_actual().color():
                        return pico # Devuelve el nuevo pico seleccionado
                else:
                    origen = pico_seleccionado
                    destino = pico
                    try: game.mover_ficha(origen, destino)
                    except Exception as e: print(f"Error: {e}")
                    return None # Deselecciona el pico
    return pico_seleccionado

def dibujar_info_turno(pantalla, game, mensaje_info):
    """
    Muestra información sobre el turno actual, como el jugador y los dados.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde dibujar.
        game (Game): La instancia actual del juego.
        mensaje_info (str): Un mensaje de información adicional para mostrar.
    """
    fuente = pygame.font.Font(None, 36)
    
    # Turno del jugador
    jugador_actual = game.jugador_actual()
    texto_turno = f"Turno de: {jugador_actual.color()}"
    superficie_turno = fuente.render(texto_turno, True, COLOR_TEXTO)
    pantalla.blit(superficie_turno, (MARGEN, ALTO_VENTANA + MARGEN))

    # Dados restantes
    dados = game.movimientos_restantes
    texto_dados = f"Dados: {dados}"
    superficie_dados = fuente.render(texto_dados, True, COLOR_TEXTO)
    pantalla.blit(superficie_dados, (MARGEN, ALTO_VENTANA + MARGEN + 40))

    # Mensaje de información
    if mensaje_info:
        fuente_info = pygame.font.Font(None, 28)
        superficie_info = fuente_info.render(mensaje_info, True, (200, 0, 0)) # Rojo
        pantalla.blit(superficie_info, (ANCHO_VENTANA / 2, ALTO_VENTANA + MARGEN + 60))

def main():
    """
    Función principal que inicia y gestiona el bucle del juego.
    
    Utiliza una máquina de estados simple para controlar el flujo del juego:
    - INICIO: Pantalla inicial, un clic para empezar.
    - JUGANDO: Bucle principal del juego donde se interactúa con el tablero.
    - FIN: Pantalla que muestra al ganador.
    """
    pygame.init()

    # --- Configuración de la ventana ---
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA + 100))
    pygame.display.set_caption("Backgammon")

    # --- Inicialización del juego ---
    p1 = Player("blanco", "Jugador 1", 1)
    p2 = Player("negro", "Jugador 2", -1)
    game = Game(p1, p2)
    board = game.get_board_status()

    # --- Estado del juego ---
    ESTADO = "INICIO"  # INICIO, JUGANDO, FIN
    mensaje_info = ""

    pico_seleccionado = None

    # --- Bucle principal del juego ---
    ejecutando = True
    while ejecutando:
        # --- Gestión de eventos ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            if ESTADO == "INICIO":
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    game.decidir_iniciador()
                    game.lanzar_dados()
                    ESTADO = "JUGANDO"
            
            elif ESTADO == "JUGANDO":
                pico_seleccionado = manejar_eventos_jugando(evento, game, board, pico_seleccionado)

            elif ESTADO == "FIN":
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    ejecutando = False

        # --- Lógica y Dibujo por estado ---
        if ESTADO == "INICIO":
            dibujar_pantalla_inicio(pantalla)
        
        elif ESTADO == "JUGANDO":
            if game and not game.ganador():
                # Lógica de cambio de turno
                if not game.movimientos_restantes:
                    game.cambiar_turno()
                    game.lanzar_dados()
                    mensaje_info = "" # Limpiar mensaje anterior
                    if not game.hay_movimientos_posibles():
                        mensaje_info = "No tienes movimientos. Turno cedido."
                        game.movimientos_restantes = [] # Forzar el cambio en el próximo fotograma
                
                # Dibujo
                dibujar_tablero(pantalla)
                dibujar_fichas(pantalla, board)
                dibujar_seleccion(pantalla, pico_seleccionado)
                dibujar_info_turno(pantalla, game, mensaje_info)
            else:
                ESTADO = "FIN"
        
        elif ESTADO == "FIN":
            if game:
                dibujar_pantalla_fin(pantalla, game.ganador())

        # --- Actualización de la pantalla ---
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
