# Justificación del Diseño del Proyecto Backgammon

## 1. Resumen del diseño general

El proyecto de Backgammon se ha diseñado siguiendo una arquitectura limpia y modular, separando claramente las responsabilidades en diferentes capas.

### Estructura del Proyecto

```
computacion-2025-backgammon-Gero2208/
├── core/                             # Lógica de negocio (SOLID, independiente)
│   ├── __init__.py
│   ├── board.py                     # Estado del tablero (~150 líneas)
│   ├── checkers.py                  # Validación de movimientos (~400 líneas)
│   ├── dice.py                      # Gestión de dados (~40 líneas)
│   ├── exceptions.py                # Excepciones personalizadas (~20 líneas)
│   ├── game.py                      # Orquestador principal (~300 líneas)
│   └── player.py                    # Entidad de jugador (~30 líneas)
├── cli/                              # Interfaz de línea de comandos
│   ├── __init__.py
│   └── cli.py                       # Interacción por terminal (~120 líneas)
├── pygame_ui/                        # Interfaz gráfica con Pygame
│   ├── __init__.py
│   └── ui.py                        # UI gráfica (~700 líneas)
└── tests/                            # Suite de pruebas (~760 líneas)
    ├── __init__.py
    ├── tests_board.py               # Tests del tablero (57 líneas)
    ├── tests_checkers.py            # Tests de movimientos (347 líneas)
    ├── tests_cli.py                 # Tests de CLI (146 líneas)
    ├── tests_dice.py                # Tests de dados (38 líneas)
    ├── tests_game.py                # Tests de orquestación (153 líneas)
    └── tests_player.py              # Tests de jugador (18 líneas)
```

### Flujo de Datos

```
┌─────────────────────────────────────────────────────────────┐
│                     Capa de Presentación                    │
│  ┌──────────────┐                    ┌──────────────┐       │
│  │     CLI      │                    │    Pygame    │       │
│  │  - Input     │                    │  - Eventos   │       │
│  │  - Display   │                    │  - Render    │       │
│  └──────┬───────┘                    └──────┬───────┘       │
│         │                                   │               │
│         └──────────────┬────────────────────┘               │
└────────────────────────┼────────────────────────────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │   Game (orquestador)          │
         │   - Gestiona turnos           │
         │   - Lanza dados                │
         │   - Valida estado del juego    │
         └───────────┬───────────────────┘
                     │
         ┌───────────┼───────────┐
         ▼           ▼           ▼
    ┌────────┐  ┌────────┐  ┌────────┐
    │ Board  │  │ Dice   │  │ Player │
    │ Estado │  │ Random │  │ Info   │
    └────┬───┘  └────────┘  └────────┘
         │
         ▼
    ┌──────────────────────┐
    │  Checkers            │
    │  Validación estática │
    │  - Movimientos       │
    │  - Capturas          │
    │  - Bear-off          │
    │  - Reingreso         │
    └──────────────────────┘
```

El núcleo de la lógica del juego reside en el directorio `core`, que es completamente independiente de cualquier interfaz de usuario. El diseño se centra en la clase `Game` como orquestador principal, que utiliza otras clases de `core` para gestionar el estado y las reglas del juego. La comunicación entre la interfaz de usuario y el núcleo se realiza exclusivamente a través de la interfaz pública de `Game`, garantizando bajo acoplamiento y alta cohesión.

## 2. Justificación de las clases elegidas

Las clases se han diseñado siguiendo el Principio de Responsabilidad Única (SRP) de SOLID. Cada clase tiene una responsabilidad claramente definida y una única razón para cambiar.

### 2.1 Clase `Game`
**Responsabilidad**: Orquestar la partida completa.
- Gestionar los turnos entre jugadores
- Controlar el lanzamiento de dados
- Validar el estado del juego (ganador, movimientos posibles)
- Coordinar las interacciones entre `Board`, `Checkers` y `Dice`

**Justificación**: `Game` actúa como fachada del sistema, exponiendo una API pública simple para las interfaces de usuario. No contiene lógica de movimiento de fichas (delegada a `Checkers`) ni de representación del tablero (delegada a `Board`).

### 2.2 Clase `Board`
**Responsabilidad**: Representar el estado del tablero.
- Mantener la posición de las fichas en los 24 puntos
- Gestionar la barra (fichas capturadas)
- Gestionar la zona final (fichas sacadas)
- Proveer representación visual para CLI

**Justificación**: `Board` es una estructura de datos pura que no valida movimientos. Esta separación permite que el estado del tablero sea consultado y modificado sin mezclar lógica de negocio.

### 2.3 Clase `Checkers`
**Responsabilidad**: Contener toda la lógica de validación y ejecución de movimientos.
- Validación de movimientos normales
- Lógica de captura de fichas
- Reingreso desde la barra
- Bear-off (sacar fichas del tablero)
- Cálculo de movimientos posibles

**Justificación**: Al ser una clase con métodos estáticos, `Checkers` no mantiene estado, lo que la hace predecible y fácil de probar. Todas las reglas del backgammon están centralizadas aquí, facilitando el mantenimiento.

### 2.4 Clase `Dice`
**Responsabilidad**: Gestionar la lógica de los dados.
- Lanzar los dados
- Detectar dobles
- Duplicar valores en caso de dobles
- Permitir establecer valores predefinidos (para testing)

**Justificación**: Abstrae el comportamiento de los dados, facilitando las pruebas al permitir establecer valores predefinidos mediante `set_valor()`.

### 2.5 Clase `Player`
**Responsabilidad**: Representar a un jugador.
- Almacenar nombre
- Almacenar color de las fichas
- Almacenar dirección de movimiento en el tablero

**Justificación**: Es una entidad de datos simple que encapsula la información del jugador sin lógica de comportamiento compleja.

### 2.6 Módulo `exceptions`
**Responsabilidad**: Definir excepciones personalizadas del dominio.
- `BackgammonException`: Clase base
- `MovimientoInvalido`: Para movimientos no permitidos
- `DadoInvalido`: Para dados no disponibles
- `OrigenInvalido`: Para orígenes sin movimientos posibles

**Justificación**: Las excepciones personalizadas permiten un control de flujo más expresivo y facilitan el manejo de errores en las interfaces de usuario.

## 3. Justificación de atributos

Los atributos de las clases se han elegido para ser los mínimos necesarios para representar el estado de cada componente. Se utilizan atributos privados (con `__nombre__`) para encapsular el estado interno y se exponen métodos públicos para acceder a ellos de forma controlada, siguiendo el principio de Encapsulación.

### 3.1 Atributos de `Board`
```python
self.__points__ = [[] for _ in range(24)]  # 24 puntos del tablero
self.__bar__ = {"blanco": [], "negro": []}  # Fichas capturadas
self.__final__ = {"blanco": [], "negro": []}  # Fichas sacadas
```
**Justificación**: Estas tres estructuras son suficientes para representar cualquier estado válido de un tablero de Backgammon. Los puntos se implementan como lista para acceso O(1) por índice. La barra y zona final son diccionarios para acceso O(1) por color.

### 3.2 Atributos de `Game`
```python
self.__p1__ = p1  # Primer jugador
self.__p2__ = p2  # Segundo jugador
self.__turno__ = 0  # Índice del jugador actual (0 o 1)
self.__board__ = Board()  # Instancia del tablero
self.__dice__ = Dice()  # Instancia de los dados
self.movimientos_restantes = []  # Público: dados disponibles
```
**Justificación**: Estos atributos son los componentes mínimos necesarios para gestionar una partida. `movimientos_restantes` es público para que las UIs puedan consultarlo directamente sin necesidad de un getter.

### 3.3 Atributos de `Player`
```python
self.__nombre__ = str(nombre)  # Identificador del jugador
self.__color__ = str(color)  # Color de fichas ('blanco' o 'negro')
self.__direccion__ = direccion  # Dirección de movimiento (+1 o -1)
```
**Justificación**: Estos tres atributos definen de forma única a un jugador y su comportamiento en el tablero. La dirección determina cómo se calculan los destinos de movimiento.

### 3.4 Atributos de `Dice`
```python
self.__valor__ = [0, 0]  # Par de dados
```
**Justificación**: Una lista de dos enteros es suficiente para almacenar el resultado de una tirada. Se inicializa en `[0, 0]` para indicar que no se han lanzado.

## 4. Decisiones de diseño relevantes

### 4.1 Separación Lógica-UI
La decisión arquitectónica más importante fue separar completamente la lógica del juego (`core`) de su presentación (`cli`, `pygame_ui`).

**Beneficios**:
- Reutilización: La misma lógica sirve para CLI y GUI
- Testabilidad: Se puede probar el core sin simular interacciones de usuario
- Mantenibilidad: Cambios en la UI no afectan a la lógica
- Flexibilidad: Se pueden agregar nuevas interfaces sin modificar el core

**Implementación**: La interfaz de Pygame tiene más de 700 líneas de código para renderizado, eventos y animaciones, pero solo interactúa con `Game` a través de sus métodos públicos.

### 4.2 Clase `Checkers` Estática
Se decidió que `Checkers` fuera una clase de utilidad con métodos estáticos porque:
- Las reglas de movimiento son universales y no dependen del estado de una partida
- No necesita instanciarse, actuando como un namespace
- Facilita el testing al no requerir gestión de estado
- Simplifica el código al evitar dependencias innecesarias

```python
class Checkers:
    @staticmethod
    def es_movimiento_valido(board, jugador, origen, destino, dado):
        # Toda la lógica de validación centralizada
```

### 4.3 Inyección de Dependencias en `Game`
La clase `Game` recibe las instancias de `Player` en su constructor (Dependency Injection):

```python
# En cli.py o ui.py
p1 = Player("blanco", "Ana", 1)
p2 = Player("negro", "Juan", -1)
game = Game(p1, p2)  # Se inyectan las dependencias
```

**Ventajas**:
- Facilita el testing (se pueden inyectar jugadores mock)
- Aumenta la flexibilidad (permite diferentes tipos de jugadores)
- Cumple con el principio de Inversión de Dependencias (DIP)

### 4.4 Manejo de Errores con Excepciones
Se utilizan excepciones personalizadas para comunicar errores desde la lógica del juego a la interfaz de usuario:

```python
try:
    game.mover_ficha(origen, destino)
except MovimientoInvalido as e:
    print(f"Error: {e}")  # CLI
    # O mostrar mensaje en pantalla (Pygame)
```

**Ventajas**:
- Separa el flujo normal del flujo de error
- La lógica no se preocupa por cómo se muestran los errores
- Cada interfaz puede manejar los errores apropiadamente

### 4.5 API Pública de `Game`
`Game` expone una API completa y bien definida:
- `decidir_iniciador()`: Determina quién comienza
- `lanzar_dados()`: Inicia un nuevo turno
- `mover_ficha()`: Ejecuta un movimiento normal
- `reingresar_desde_barra()`: Reingresa desde la barra
- `sacar_ficha()`: Ejecuta un bear-off
- `hay_movimientos_posibles()`: Verifica si el jugador puede mover
- `ganador()`: Determina si hay un ganador

Esta API permite que las interfaces implementen el juego sin conocer detalles internos.

## 5. Excepciones y manejo de errores

Se han definido un conjunto de excepciones personalizadas que heredan de `BackgammonException` para manejar errores específicos del dominio de forma clara.

### 5.1 Jerarquía de Excepciones
```python
BackgammonException (Exception)
    ├── MovimientoInvalido
    ├── DadoInvalido
    └── OrigenInvalido
```

### 5.2 `BackgammonException`
**Definición**: Clase base para todas las excepciones del juego.

**Justificación**: Permite capturar cualquier error específico del dominio con un solo `except`, facilitando el manejo genérico de errores.

### 5.3 `MovimientoInvalido`
**Cuándo se lanza**:
- No hay ficha propia en el origen
- El destino está bloqueado por 2+ fichas rivales
- El movimiento no corresponde al dado disponible
- Se intenta bear-off sin cumplir las condiciones

**Justificación**: Agrupa todos los errores relacionados con movimientos que violan las reglas del backgammon.

### 5.4 `DadoInvalido`
**Cuándo se lanza**:
- Se intenta usar un dado que no está en `movimientos_restantes`
- Se intenta una acción con un dado ya consumido

**Justificación**: Distingue errores de lógica de dados de otros tipos de errores, permitiendo mensajes más específicos.

### 5.5 `OrigenInvalido`
**Cuándo se lanza**:
- Se selecciona un punto sin movimientos posibles
- Se intenta mover desde un punto sin fichas propias

**Justificación**: Proporciona feedback temprano al usuario sobre selecciones inválidas antes de intentar el movimiento.

### 5.6 Propagación y Manejo

Las excepciones se propagan desde `Checkers` → `Game` → UI:

```python
# En Checkers
if destino_bloqueado:
    raise MovimientoInvalido("Destino bloqueado por fichas rivales")

# En Game
def mover_ficha(self, origen, destino):
    # Propaga la excepción sin atraparla
    self.movimientos_restantes = Checkers.mover_y_consumir(...)

# En CLI
try:
    game.mover_ficha(origen, destino)
except BackgammonException as e:
    print(f"Error: {e}")

# En Pygame
try:
    game.mover_ficha(origen, destino)
except BackgammonException as e:
    mensaje_info = f"Error: {e}"  # Se muestra en pantalla
```

## 6. Estrategias de testing y cobertura

### 6.1 Enfoque de Testing
La estrategia se centra en pruebas unitarias exhaustivas del directorio `core`, aprovechando el desacoplamiento con la UI. El objetivo es alcanzar una cobertura superior al 90% en la lógica de negocio.

### 6.2 Estructura de Tests
```
tests/ (~760 líneas totales)
├── tests_board.py (57 líneas)
│   ├── Inicialización del tablero
│   ├── Setup con disposición inicial
│   ├── Operaciones en zona final
│   └── Renderizado CLI
├── tests_checkers.py (347 líneas)
│   ├── Validación de movimientos
│   ├── Movimientos con captura
│   ├── Cálculo de destinos posibles
│   ├── Reingreso desde barra
│   ├── Bear-off (sacar fichas)
│   └── Consumo de dados
├── tests_dice.py (38 líneas)
│   ├── Lanzamiento de dados
│   ├── Detección de dobles
│   └── Duplicación de valores
├── tests_player.py (18 líneas)
│   └── Creación y atributos de jugador
├── tests_game.py (153 líneas)
│   ├── Decidir iniciador
│   ├── Cambio de turnos
│   ├── Lanzamiento de dados
│   ├── Movimientos posibles
│   ├── Reingreso desde barra
│   ├── Bear-off
│   └── Detección de ganador
└── tests_cli.py (146 líneas)
    ├── Procesamiento de comandos
    ├── Movimientos normales
    ├── Reingreso desde barra
    ├── Bear-off
    └── Manejo de errores con mocks
```

### 6.3 Técnicas Utilizadas

#### 6.3.1 Inyección de Valores Predefinidos
Para hacer tests deterministas de código con aleatoriedad:
```python
dice = Dice()
dice.set_valor([3, 3])  # Forzar dobles
assert dice.dobles() == True
assert dice.duplicar() == [3, 3, 3, 3]
```

#### 6.3.2 Simulación de Estados Complejos
Para probar flujos con múltiples tiradas:
```python
# Simular empate en decidir_iniciador
valores = [3, 3, 5, 2]  # Empate, luego desempate
def mock_roll_one():
    return valores.pop(0)
game.__dice__.roll_one = mock_roll_one
iniciador, t1, t2 = game.decidir_iniciador()
```

#### 6.3.3 Mocks para CLI
Para probar la interfaz sin interacción real:
```python
@patch('builtins.input', side_effect=['p1', 'blanco', 'p2'])
@patch('builtins.print')
def test_main(self, mock_print, mock_input):
    # Test del flujo completo sin I/O real
```

### 6.4 Qué se Probó y Por Qué

#### 6.4.1 `Board` (tests_board.py - 57 líneas)
**Qué**: Inicialización, setup, operaciones en zona final, renderizado CLI.

**Por qué**: `Board` es la estructura de datos central. Errores aquí afectan todo el juego. Se verifica que el estado inicial sea correcto y que las operaciones básicas funcionen.

#### 6.4.2 `Checkers` (tests_checkers.py - 347 líneas)
**Qué**: Todas las reglas de movimiento, capturas, bear-off, reingreso, cálculo de movimientos posibles.

**Por qué**: `Checkers` contiene el 90% de la complejidad del juego. Es crítico probar exhaustivamente todas las reglas para garantizar que el juego funciona correctamente.

#### 6.4.3 `Dice` (tests_dice.py - 38 líneas)
**Qué**: Lanzamiento, detección de dobles, duplicación.

**Por qué**: Aunque simple, el comportamiento de los dados es fundamental. Se prueba que `set_valor()` funciona correctamente para testing.

#### 6.4.4 `Player` (tests_player.py - 18 líneas)
**Qué**: Creación y acceso a atributos.

**Por qué**: `Player` es simple, pero se verifica que la encapsulación funciona correctamente.

#### 6.4.5 `Game` (tests_game.py - 153 líneas)
**Qué**: Orquestación de turnos, lanzamiento de dados, validación de estado, detección de ganador.

**Por qué**: `Game` coordina todos los componentes. Se prueba la integración entre `Board`, `Checkers`, `Dice` y `Player`.

#### 6.4.6 `CLI` (tests_cli.py - 146 líneas)
**Qué**: Procesamiento de comandos, manejo de errores, flujo completo.

**Por qué**: Verifica que la interfaz CLI interactúa correctamente con el core y maneja errores apropiadamente usando mocks.

### 6.5 Cobertura Esperada
- **`core/`**: >95% (lógica crítica)
- **`cli/`**: >95% (interfaz de usuario)
- **`pygame_ui/`**: No testeado unitariamente (testing manual/visual)

### 6.6 Beneficios del Diseño para Testing
- Core testeable sin UI: No se necesita simular clics o entrada de teclado
- Métodos estáticos: `Checkers` es fácilmente testeable sin setup complejo
- Inyección de dependencias: Permite mockear componentes
- Excepciones tipadas: Facilita verificar comportamiento de error

## 7. Referencias a requisitos SOLID

El diseño del `core` cumple con los cinco principios SOLID, asegurando un código mantenible, flexible y robusto.

### 7.1 S - Principio de Responsabilidad Única (SRP)
**Definición**: Cada clase debe tener una sola razón para cambiar.

**Cumplimiento en el proyecto**:

#### Ejemplo 1: `Dice`
```python
class Dice:
    def roll(self):
        self.__valor__ = [random.randint(1, 6), random.randint(1, 6)]
        return self.__valor__
    
    def dobles(self):
        return self.__valor__[0] == self.__valor__[1]
```
**Razón única de cambio**: Si cambian las reglas de los dados (ej: dados de 8 caras), solo esta clase se modifica.

#### Ejemplo 2: `Board`
```python
class Board:
    def get_points(self): ...
    def get_bar(self): ...
    def mostrar_tablero_cli(self): ...
```
**Razón única de cambio**: Si cambia la representación del tablero, solo `Board` se modifica. No valida movimientos ni gestiona turnos.

#### Ejemplo 3: `Checkers`
Toda la lógica de validación de movimientos está centralizada. Si cambian las reglas de movimiento, solo `Checkers` se modifica.

### 7.2 O - Principio de Abierto/Cerrado (OCP)
**Definición**: Las clases deben estar abiertas a extensión pero cerradas a modificación.

**Cumplimiento en el proyecto**:

#### Ejemplo 1: Extensibilidad de jugadores
```python
class Game:
    def __init__(self, p1, p2):
        self.__p1__ = p1  # Puede ser Player, AIPlayer, RemotePlayer
        self.__p2__ = p2

    def jugador_actual(self):
        return self.__p1__ if self.__turno__ == 0 else self.__p2__
```

Se puede crear una clase `AIPlayer` sin modificar `Game`:
```python
class AIPlayer:
    def __init__(self, color, nombre, direccion):
        self.__color__ = color
        self.__nombre__ = nombre
        self.__direccion__ = direccion
    
    def color(self): return self.__color__
    def nombre(self): return self.__nombre__
    def direccion(self): return self.__direccion__
    
    def decidir_movimiento(self, game):
        # Lógica de IA
        pass

# Uso sin modificar Game
ai = AIPlayer("negro", "CPU", -1)
game = Game(p1, ai)
```

#### Ejemplo 2: Extensibilidad de interfaces
El core es completamente cerrado. Se agregó la interfaz Pygame sin modificar una línea de `core`:
- CLI: 120 líneas
- Pygame: 700+ líneas
- Core: Sin cambios

### 7.3 L - Principio de Sustitución de Liskov (LSP)
**Definición**: Los objetos de un tipo deben poder ser sustituidos por objetos de un subtipo sin alterar el comportamiento del programa.

**Cumplimiento en el proyecto**:

Aunque no hay herencia explícita, se respeta mediante "Duck Typing": cualquier objeto que cumpla el contrato de `Player` puede usarse indistintamente.

#### Contrato de Player:
```python
# Cualquier objeto con estos métodos es un Player válido
def color() -> str: ...
def nombre() -> str: ...
def direccion() -> int: ...
```

#### Uso en Game:
```python
class Game:
    def __init__(self, p1, p2):
        self.__board__.setup(p1.color(), p2.color())  # Confía en el contrato
    
    def jugador_actual(self):
        # Retorna cualquier objeto que cumpla el contrato
        return self.__p1__ if self.__turno__ == 0 else self.__p2__
```

Esto permite sustituir `Player` por cualquier clase compatible (ej: `AIPlayer`, `RemotePlayer`) sin romper `Game`.

### 7.4 I - Principio de Segregación de Interfaces (ISP)
**Definición**: Los clientes no deben depender de interfaces que no usan.

**Cumplimiento en el proyecto**:

#### Ejemplo 1: `Checkers` y `Board`
```python
class Checkers:
    @staticmethod
    def es_movimiento_valido(board, jugador, origen, destino, dado):
        puntos = board.get_points()  # Solo necesita esto
        # NO necesita board.mostrar_tablero_cli()
        # NO necesita board.get_final()
```

#### Ejemplo 2: Interfaz pública de `Game`
La CLI solo usa un subconjunto de métodos:
```python
# CLI usa:
game.lanzar_dados()
game.mover_ficha()
game.cambiar_turno()
game.ganador()

# Pygame además usa:
game.get_board_status()
game.hay_movimientos_posibles()
game.todas_fichas_en_casa()
game.posibles_entradas_desde_barra()
```

Cada cliente usa solo lo que necesita, sin depender de métodos irrelevantes.

### 7.5 D - Principio de Inversión de Dependencias (DIP)
**Definición**: Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.

**Cumplimiento en el proyecto**:

#### Ejemplo 1: Inyección en `Game`
```python
# Alto nivel (Game) no crea bajo nivel (Player)
class Game:
    def __init__(self, p1, p2):  # Recibe abstracciones
        self.__p1__ = p1
        self.__p2__ = p2
```

```python
# Bajo nivel creado externamente
# En cli.py
p1 = Player("blanco", "Ana", 1)
p2 = Player("negro", "Juan", -1)
game = Game(p1, p2)  # Se inyectan

# En ui.py
p1 = Player("blanco", nombre1, 1)
p2 = Player("negro", nombre2, -1)
game = Game(p1, p2)  # Misma inyección
```

#### Ejemplo 2: Dependencia de abstracciones
```python
# Game depende del "concepto" de jugador, no de una implementación
def jugador_actual(self):
    # No importa si es Player, AIPlayer, RemotePlayer
    # Solo importa que tenga .color(), .nombre(), .direccion()
    return self.__p1__ if self.__turno__ == 0 else self.__p2__
```

**Beneficios**:
- `Game` es testeable con jugadores mock
- Se pueden agregar nuevos tipos de jugadores sin modificar `Game`
- La lógica de alto nivel es independiente de detalles de implementación

## 8. Anexos

### 8.1 Diagrama de Clases UML

Se encuentra en el archivo `UML.mermaid`