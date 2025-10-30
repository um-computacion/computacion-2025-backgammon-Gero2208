"""
Este módulo contiene la clase Dice, que representa los dados del juego.
"""
import random


class Dice:
    """
    Representa un par de dados para el juego de Backgammon.

    Esta clase gestiona el estado y el comportamiento de los dados,
    incluyendo su lanzamiento y la gestión de dobles.

    Atributos:
        __valor__ (list[int]): Una lista de dos enteros que representan
                               el valor de cada dado.
    """
    def __init__(self):
        """
        Inicializa los dados con un valor de [0, 0].
        """
        self.__valor__ = [0, 0]

    def roll(self):
        """
        Lanza los dados para obtener nuevos valores aleatorios.

        Asigna dos nuevos valores aleatorios entre 1 y 6 a los dados.

        Returns:
            list[int]: La lista con los dos nuevos valores de los dados.
        """
        self.__valor__ = [random.randint(1, 6), random.randint(1, 6)]
        return self.__valor__

    def dobles(self):
        """
        Comprueba si los dos dados tienen el mismo valor.

        Returns:
            bool: True si los valores de los dados son iguales, False en caso contrario.
        """
        return self.__valor__[0] == self.__valor__[1]

    def duplicar(self):
        """
        Devuelve los valores de los dados, duplicados si son dobles.

        Si los dados son dobles, devuelve una lista con cuatro veces el valor del dado.
        Si no, devuelve una lista con los dos valores de los dados.

        Returns:
            list[int]: Una lista de 4 elementos si son dobles, o 2 en caso contrario.
        """
        if self.dobles():
            return [self.__valor__[0]] * 4
        return self.__valor__

    def set_valor(self, valor):
        """
        Establece el valor de los dados con fines de prueba.

        Args:
            valor (list[int]): La lista de valores a establecer.
        """
        self.__valor__ = valor

    def roll_one(self):
        """
        Lanza un solo dado y devuelve su valor.
        """
        return random.randint(1, 6)
