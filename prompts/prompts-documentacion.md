## Prompt

### Documenta la clase Dice y los actuales métodos que tiene

## Response

class Dice:
    """
    Clase que representa los dados utilizados en el juego de Backgammon.

    Atributos:
        __valor__ (list[int]): Lista con los valores actuales de los dos dados. 
                               Inicialmente [0, 0]. Se actualiza con cada tirada.

    Métodos:
        roll(): Lanza los dos dados y actualiza el atributo __valor__ con valores aleatorios entre 1 y 6.
        dobles(): Devuelve True si ambos dados tienen el mismo valor, False en caso contrario.
    """
    def __init__(self):
        self.__valor__ = [0, 0]

    def roll(self):
        """
        Lanza los dos dados y actualiza el atributo __valor__ con valores aleatorios entre 1 y 6.

        Returns:
            list[int]: Lista con los dos valores obtenidos.
        """
        self.__valor__ = [random.randint(1, 6), random.randint(1, 6)]
        return self.__valor__
    
    def dobles(self):
        """
        Verifica si ambos dados tienen el mismo valor.

        Returns:
            bool: True si los dos valores son iguales, False en caso contrario.
        """
        return self.__valor__[0] == self.__valor__[1]

## Prompt

### Documenta la clase Game y los actuales métodos que tiene

## Response

class Game:
    """
    Clase que gestiona los turnos de una partida de Backgammon.

    Atributos:
        __p1__ (Player): Primer jugador.
        __p2__ (Player): Segundo jugador.
        __turno__ (int): 0 si es el turno de __p1__, 1 si es el turno de __p2__.

    Métodos:
        __init__(p1, p2): Inicializa la partida con dos jugadores y establece el turno inicial.
        jugador_actual(): Devuelve el jugador cuyo turno es actualmente.
        cambiar_turno(): Alterna el turno entre los dos jugadores.
    """

    def __init__(self, p1, p2):
        self.__p1__ = p1
        self.__p2__ = p2
        self.__turno__ = 0  # 0 para p1, 1 para p2

    def jugador_actual(self):
        """
        Devuelve el jugador cuyo turno es actualmente.

        Returns:
            Player: El jugador que debe jugar en este turno.
        """
        return self.__p1__ if self.__turno__ == 0 else self.__p2__

    def cambiar_turno(self):
        """
        Alterna el turno entre los dos jugadores.
        """
        self.__turno__ = 1 - self.__turno__