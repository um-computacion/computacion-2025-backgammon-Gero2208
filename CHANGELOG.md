# Changelog

Todas las modificaciones notables de este proyecto serán documentadas en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/),
y este proyecto sigue [Semantic Versioning](https://semver.org/lang/es/).

## [0.6.1] 29-10-2025

### Added

- Implementación de tests unitarios para todas las clases y CLI para llegar a un Cover de 96%

## [0.6.1] 29-10-2025

### Added

- Corrección de bear_off que no funcionaba correctamente la regla de "Sacar una ficha de un punto más alto (el caso especial)"

## [0.6.0] 28-10-2025

### Added

- Implementación de la interfaz gráfica mediante la biblioteca Pygame
- Se actualizan los métodos del bear_off para una funcionalidad correcta
- Corrección de bugs para la lógica de bear_off junto con el método hay_movimientos_posibles
- Corrección de bugs para la interfaz gráfica donde no dejaba cambiar de turno
- Mejoras en la explicación de movimientos del CLI

## [0.5.1] 27-10-2025

### Added

-Implementación de tests unitarios para la clase Board
-Implementación de tests unitarios para la clase Checkers
-Implementación de tests unitarios para el CLI
-Implementación de tests unitarios para la clase Dice
-Implementación de tests unitarios para la clase Game
-Implementación de tests unitarios para la clase Player
-Cambios en el CLI para facilitar los tests unitarios para este

## [0.5.0] 25-10-2025

### Added

- Implementación lógica para el sistema de bear_off, sacar fichas del tablero una vez llegado a la zona de home para ganar
- Implementación de los métodos todas_en_inicio, distancia_desde_origen, puede_bear_off y bear_off para la clase Checkers
- Implementación del método ganador para la clase Game
- Implementación de cambios en CLI para gestionar el bear off y declarar ganador
- Corrección de bug, crashea el CLI al intentar sacar fichas del tablero para bear off
- Implementación de la Single Responsability Principle de los principios SOLID para la clase Game

## [0.4.2] 21-10-2025

### Added

- Implementación lógica para el sistema de comer fichas, ingreso y reingreso desde la barra
- Implementación del método destino_entrada_por_dado para la clase Checkers
- Implementación del método puede_reingresar para la clase Checkers
- Implementación del método reingresar_desde_bar para la clase Checkers
- Cambios en CLI para implementar todos estos métodos
- Se corrigio un bug en el cual al tener dados dobles se multiplicaban el destino posible una vez seleccionada una casilla

## [0.4.1] 20-10-2025

### Added

- Implementación de lógica para el sistema de movimientos
- Implementación del método dado_para_movimiento para la clase Checkers
- Implementación del método mover_y_consumir para la clase Checkers
- Implementación del método hay_movimientos_posibles para la clase Checkers
- Correción de bugs y avance en CLI para gestión de turnos con movimientos
- Implementación de método para la clase Game para elegir quien inicia la partida

## [0.4.0] 07-10-2025

### Added

- Implementación de la clase Checkers
- Implementación del método es_movimiento_valido para la clase Checkers
- Implementación del método mover para la clase Checkers
- Implementación del método destinos_posibles para la clase Checkers
- Implementación de movimientos para el CLI

## [0.3.2] 30-09-2025

### Added

- Implementación de atributos para la clase Game
- Implementación del método jugador_actual para la clase Game
- Implementación del método cambiar_turno para la clase Game
- Implementación de dos métodos en Player para obtener nombre y color
- Implementación de Dice en CLI para realizar tiradas y duplicar tiradas del mismo valor

## [0.3.1] 28-09-2025

### Added

- Mejora gráfica del tablero para el CLI
- Implementación de atributos para la clase Dice
- Implementación del método roll para la clase Dice
- Implementación del método dobles para la clase Dice
- Tests para la clase Dice

## [0.3.0] 24-09-2025

### Added

- Implementación del método mostrar_tablero_cli en la clase Board para representar el tablero de Backgammon en la consola con triángulos y detalles de fichas.

## [0.2.2] 17-09-2025

### Added

- Implementación de atributos básicos de la clase Player.
- Implementación del método asignar_color_opuesto a la clase Player.

## [0.2.1] 16-09-2025

### Added

- Implementación del inicio del CLI.

## [0.2.0] 15-09-2025

### Added

- Implementación del método setup a la clase Board para inicializar el tablero con la disposición estándar de Backgammon.

## [0.1.0] 4-09-2025

### Added

- Implementación del esqueleto del proyecto
- Implementación de archivo requeriments.txt
