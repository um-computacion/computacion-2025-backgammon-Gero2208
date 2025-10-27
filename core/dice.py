import random

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
    
    def duplicar(self):
        if self.dobles():
            return [self.__valor__[0]] * 4 
        else:
            return self.__valor__
    
    def set_valor(self, valor):
        """Sets the dice values for testing purposes."""
        self.__valor__ = valor