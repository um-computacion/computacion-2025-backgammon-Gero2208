class Player:
    """
    Representa a un jugador de Backgammon.

    Atributos:
        __nombre__ (str): Nombre del jugador.
        __color__ (str): Color asignado al jugador ('blanco' o 'negro').
        __direccion__ (int): Dirección de movimiento en el tablero (+1 o -1).
    """
    def __init__(self, color: str, nombre: str, direccion: int):
        """
        Inicializa un jugador con su color, nombre y dirección.

        Args:
            color (str): Color del jugador ('blanco' o 'negro').
            nombre (str): Nombre del jugador.
            direccion (int): Dirección de movimiento (+1 o -1).
        """
        self.__nombre__ = str(nombre)
        self.__color__ = str(color)
        self.__direccion__ = direccion


    def asignar_color_opuesto(self, color1: str):
        """
        Asigna automáticamente el color opuesto al jugador.

        Si el color recibido es 'blanco', asigna 'negro' y viceversa.
        Si el color recibido no es válido, asigna 'blanco' por defecto.

        Args:
            color1 (str): Color del otro jugador ('blanco' o 'negro').
        """
        color = color1.strip().lower()
        if color == "blanco":
            self.__color__ = "negro"
        else:
            self.__color__ = "blanco"