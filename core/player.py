class Player:
    """
    Representa a un jugador en el juego de Backgammon.

    Esta clase almacena la información esencial de un jugador, incluyendo su
    nombre, color y la dirección en la que se mueven sus fichas en el tablero.

    Atributos:
        __nombre__ (str): El nombre del jugador.
        __color__ (str): El color de las fichas del jugador ('blanco' o 'negro').
        __direccion__ (int): La dirección de movimiento del jugador en el
                             tablero (+1 para los blancos, -1 para los negros).
    """
    def __init__(self, color: str, nombre: str, direccion: int):
        """
        Inicializa una nueva instancia de Jugador.

        Args:
            color (str): El color de las fichas del jugador.
            nombre (str): El nombre del jugador.
            direccion (int): La dirección de movimiento en el tablero.
        """
        self.__nombre__ = str(nombre)
        self.__color__ = str(color)
        self.__direccion__ = direccion

    def nombre(self):
        """
        Devuelve el nombre del jugador.

        Returns:
            str: El nombre del jugador.
        """
        return self.__nombre__
    
    def color(self):
        """
        Devuelve el color de las fichas del jugador.

        Returns:
            str: El color del jugador ('blanco' o 'negro').
        """
        return self.__color__
    
    def direccion(self):
        """
        Devuelve la dirección de movimiento del jugador en el tablero.

        Returns:
            int: La dirección de movimiento (+1 o -1).
        """
        return self.__direccion__
