# Changelog

Todas las modificaciones notables de este proyecto serán documentadas en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/),
y este proyecto sigue [Semantic Versioning](https://semver.org/lang/es/).

## [1.0.0] - 2025-11-01

### Added

- Soporte completo para ejecutar el juego mediante Docker
- Servicio CLI containerizado para jugar desde Docker
- Servicio de tests containerizado con reporte de cobertura

### Changed

- Reorganización de la documentación del proyecto
- Actualización del README con instrucciones de Docker

## [0.8.1] - 2025-10-31

### Fixed

- Corrección de bugs críticos en la interfaz gráfica de Pygame
- Arreglo de comportamiento inesperado en selección de fichas
- Mejora en la gestión de eventos de mouse

## [0.8.0] - 2025-10-30

### Added

- Suite completa de tests unitarios para todas las clases del core
- Tests unitarios para CLI con cobertura del 96%
- Archivo CHANGELOG.md siguiendo convenciones estándar
- Archivo JUSTIFICACION.md con decisiones de diseño y arquitectura
- Diagrama UML completo del sistema

### Changed

- Refactorización general del código para mejorar calidad
- Mejora de la puntuación de código a 9.59/10

### Fixed

- Corrección de la implementación de bear-off en Pygame
- Arreglo de bugs en el sistema de sacado de fichas

## [0.7.1] - 2025-10-29

### Fixed

- Corrección de la regla especial de bear-off para sacar fichas desde puntos más altos
- Arreglo del caso especial cuando no hay punto exacto disponible para el dado

## [0.7.0] - 2025-10-28

### Added

- Implementación completa de la interfaz gráfica con Pygame
- Sistema de renderizado visual del tablero
- Interacción con mouse para seleccionar y mover fichas
- Panel de información con datos del turno y dados
- Pantallas de inicio, juego y fin de partida

### Changed

- Actualización de métodos de bear-off para mejor funcionalidad
- Mejoras en las explicaciones de movimientos del CLI

### Fixed

- Corrección de bugs en la lógica de bear-off
- Arreglo del método `hay_movimientos_posibles` para detectar bear-off
- Corrección de bug que impedía el cambio automático de turno en Pygame

## [0.6.0] - 2025-10-27

### Added

- Tests unitarios para la clase `Board`
- Tests unitarios para la clase `Checkers`
- Tests unitarios para el CLI
- Tests unitarios para la clase `Dice`
- Tests unitarios para la clase `Game`
- Tests unitarios para la clase `Player`

### Changed

- Modificación del CLI para facilitar la creación de tests unitarios
- Refactorización de métodos para mejor testabilidad

## [0.5.0] - 2025-10-25

### Added

- Implementación completa del sistema de bear-off (sacar fichas del tablero)
- Método `todas_en_inicio` en la clase `Checkers`
- Método `distancia_desde_origen` en la clase `Checkers`
- Método `puede_bear_off` en la clase `Checkers`
- Método `bear_off` en la clase `Checkers`
- Método `ganador` en la clase `Game` para detectar fin de partida
- Gestión de bear-off en el CLI
- Sistema de declaración de ganador en el CLI

### Changed

- Aplicación del principio de Responsabilidad Única (SRP) en la clase `Game`

### Fixed

- Corrección de crash en CLI al intentar sacar fichas del tablero

## [0.4.2] - 2025-10-21

### Added

- Sistema completo de captura de fichas
- Lógica de ingreso y reingreso desde la barra
- Método `destino_entrada_por_dado` en la clase `Checkers`
- Método `puede_reingresar` en la clase `Checkers`
- Método `reingresar_desde_bar` en la clase `Checkers`
- Comandos en CLI para gestionar fichas en la barra

### Fixed

- Corrección de bug en destinos posibles con dados dobles (duplicación incorrecta)

## [0.4.1] - 2025-10-20

### Added

- Lógica completa del sistema de movimientos
- Método `dado_para_movimiento` en la clase `Checkers`
- Método `mover_y_consumir` en la clase `Checkers`
- Método `hay_movimientos_posibles` en la clase `Checkers`
- Método `decidir_iniciador` en la clase `Game`
- Gestión de turnos con movimientos en el CLI

### Fixed

- Corrección de múltiples bugs en la gestión de turnos

## [0.4.0] - 2025-10-07

### Added

- Clase `Checkers` con lógica estática de movimientos
- Método `es_movimiento_valido` en la clase `Checkers`
- Método `mover` en la clase `Checkers`
- Método `destinos_posibles` en la clase `Checkers`
- Sistema de movimientos en el CLI

## [0.3.2] - 2025-09-30

### Added

- Atributos principales de la clase `Game`
- Método `jugador_actual` en la clase `Game`
- Método `cambiar_turno` en la clase `Game`
- Método `nombre` en la clase `Player`
- Método `color` en la clase `Player`
- Sistema de tiradas de dados en el CLI
- Lógica para duplicar dados cuando son iguales

## [0.3.1] - 2025-09-28

### Added

- Atributos de la clase `Dice`
- Método `roll` en la clase `Dice`
- Método `dobles` en la clase `Dice`
- Tests unitarios para la clase `Dice`

### Changed

- Mejora gráfica significativa del tablero en CLI
- Rediseño de la representación visual de fichas

## [0.3.0] - 2025-09-24

### Added

- Método `mostrar_tablero_cli` en la clase `Board`
- Representación ASCII del tablero con triángulos
- Visualización detallada de fichas en consola
- Indicadores de barra y zona final

## [0.2.2] - 2025-09-17

### Added

- Atributos básicos de la clase `Player`
- Método `asignar_color_opuesto` en la clase `Player`

## [0.2.1] - 2025-09-16

### Added

- Implementación inicial del CLI (Command Line Interface)
- Estructura básica para interacción por consola

## [0.2.0] - 2025-09-15

### Added

- Método `setup` en la clase `Board`
- Configuración inicial estándar del tablero de Backgammon
- Disposición automática de las 15 fichas por jugador

## [0.1.0] - 2025-09-04

### Added

- Estructura inicial del proyecto
- Clases base: `Board`, `Player`, `Game`, `Dice`, `Checkers`
- Archivo `requirements.txt` con dependencias
- Configuración básica del repositorio
