# Backgammon

## Información del Proyecto

**Alumno:** Geronimo Ortiz  
**Repositorio:** `computacion-2025-backgammon-Gero2208`  
**Curso:** Computación 2025

---

## Descripción

Este proyecto implementa el juego clásico de Backgammon con todas sus reglas oficiales, ofreciendo dos formas de jugar:

- **Interfaz Gráfica (Pygame):** Experiencia visual completa con ayudas interactivas.
- **Interfaz CLI:** Juego rápido y directo desde la terminal, compatible con Docker.

El diseño modular permite que ambas interfaces compartan la misma lógica de negocio (directorio `core`), garantizando consistencia y facilitando el mantenimiento.

---

## Ejecución con Docker (Recomendado para CLI, incompatible con interfaz gráfica)

La forma más sencilla de ejecutar el proyecto es a través de Docker, que gestiona todas las dependencias en un entorno aislado.

### Requisitos Previos

- **Docker y Docker Compose**: Asegúrate de tenerlos instalados y en ejecución.

### 1. Construir la imagen de Docker

Este comando crea el entorno de la aplicación, instalando todas las dependencias necesarias. Solo necesitas ejecutarlo la primera vez o si modificas `requirements.txt`.

```bash
docker-compose build
```

### 2. Jugar al CLI desde Docker

Una vez construida la imagen, puedes iniciar la interfaz de línea de comandos de forma interactiva.

```bash
docker-compose run --rm cli
```

### 3. Correr los tests + coverage desde Docker

Para ejecutar la suite completa de tests y ver el informe de cobertura de código:

```bash
docker-compose run --rm tests
```

---

## Ejecución Local (Alternativa para CLI, compatible con interfaz gráfica)

Si prefieres no usar Docker, puedes seguir estos pasos.

### Requisitos Previos

- **Python 3.8 o superior**
- **pip** (gestor de paquetes de Python)

### Pasos de Instalación

**1. Crear entorno virtual**

```bash
python -m venv .venv
```

**2. Activar el entorno virtual**

En **Windows (Git Bash)**:

```bash
source .venv/Scripts/activate
```

En **Windows (CMD/PowerShell)**:

```cmd
.venv\Scripts\activate
```

**3. Instalar dependencias**

```bash
pip install -r requirements.txt
```

### Cómo Ejecutar

#### Interfaz Gráfica (Pygame)

```bash
python -m pygame_ui.ui
```

#### Interfaz de Terminal (CLI)

```bash
python -m cli.cli
```

---

## Guía de Uso - Interfaz Gráfica

### Flujo del Juego

1. **Configuración Inicial**
   - Introduce el nombre del Jugador 1 (fichas blancas)
   - Introduce el nombre del Jugador 2 (fichas negras)

2. **Inicio de Partida**
   - El juego lanza automáticamente los dados para determinar quién comienza
   - Se muestra el tablero inicial configurado según las reglas oficiales

3. **Durante el Turno**
   - Los dados se lanzan automáticamente al inicio de cada turno
   - Selecciona y mueve tus fichas según los valores obtenidos

### Controles

| Acción | Control |
|--------|---------|
| Seleccionar ficha | **Clic izquierdo** sobre una ficha propia |
| Mover ficha | **Clic izquierdo** en destino válido (resaltado en verde) |
| Deseleccionar | **Clic derecho** en cualquier lugar |
| Sacar ficha (bear-off) | **Botón "Sacar"** en panel inferior (cuando esté habilitado) |

### Indicadores Visuales

- **Contorno amarillo:** Ficha seleccionada actualmente
- **Contornos verdes:** Destinos válidos para el movimiento
- **Panel inferior:** Muestra dados actuales y movimientos restantes
- **Barra central:** Fichas capturadas (grises)
- **Botón "Sacar":** Disponible solo cuando todas tus fichas están en casa

### Reglas Especiales

#### Fichas en la Barra

- Si tienes fichas capturadas, **debes reingresarlas** antes de hacer otros movimientos
- Haz clic en el punto de entrada correspondiente al valor del dado

#### Bear-off (Sacar Fichas)

- Solo disponible cuando **todas** tus fichas están en tu cuadrante final
  - Blancas: puntos 19-24
  - Negras: puntos 1-6
- Usa el botón "Sacar" después de seleccionar la ficha

#### Cambio Automático de Turno

- El turno cambia cuando:
  - Se han usado todos los dados
  - No hay movimientos posibles con los dados restantes

---

## Guía de Uso - Interfaz CLI

### Inicio del Juego

```bash
$ python -m cli.cli
Iniciando Backgammon
Nombre del Jugador 1: Ana
Color del Jugador 1 (Blanco/Negro): blanco
Nombre del Jugador 2: Juan

Tirada inicial:
Ana (blanco) tiró: 5
Juan (negro) tiró: 3
Ana (blanco) comienza con dados [5, 3]
```

### Comandos Disponibles

El formato de los comandos cambia según el contexto del juego:

#### 1. Movimiento Normal

```
mover <origen> <destino>
```

**Ejemplo:**

```
Movimientos restantes: [3, 5]
> mover 1 4
```

Mueve una ficha del punto 1 al punto 4 usando el dado de valor 3.

#### 2. Reingreso desde la Barra

Cuando tienes fichas capturadas:

```
reingresar <valor_dado>
```

**Ejemplo:**

```
Tienes fichas en la barra. Debes reingresarlas.
Movimientos restantes: [2, 5]
> reingresar 2
```

#### 3. Bear-off (Sacar Fichas)

Cuando todas tus fichas están en casa:

```
sacar <origen> <valor_dado>
```

**Ejemplo:**

```
Todas tus fichas están en casa. Puedes sacarlas.
Movimientos restantes: [4, 6]
> sacar 20 4
```

O hacer movimientos normales dentro de casa:

```
> mover 23 19
```

---

## Reglas Implementadas

El proyecto implementa **todas** las reglas oficiales del Backgammon:

- **Movimientos básicos** según resultado de dados
- **Dobles** (usar el mismo valor 4 veces)
- **Capturas** (enviar fichas rivales a la barra)
- **Reingresos** obligatorios desde la barra
- **Bloqueos** (puntos con 2+ fichas propias)
- **Bear-off** (sacar fichas del tablero)
- **Validación estricta** de movimientos legales
- **Tirada inicial** para determinar primer jugador
- **Detección automática** de fin de juego

---

## Documentación

- **CHANGELOG.md**: Historial completo de versiones y cambios del proyecto
- **JUSTIFICACION.md**: Justificación del diseño técnico, decisiones arquitectónicas y cumplimiento SOLID
- **UML.mermaid**: Diagrama de clases completo del core del sistema
- **prompts/**: Registro de todos los prompts de IA utilizados durante el desarrollo
  - **prompts-desarrollo.md**: Prompts de implementación de funcionalidades
  - **prompts-documentacion.md**: Prompts de generación de docstrings
  - **prompts-testing.md**: Prompts de creación de tests unitarios

---

## Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje de programación
- **Docker**: Plataforma de containerización
- **Pygame**: Biblioteca para interfaz gráfica
- **unittest**: Framework de testing integrado
- **GitHub Copilot / Jules**: Asistencia con IA durante el desarrollo

---