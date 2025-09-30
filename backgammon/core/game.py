class Game:

    def __init__(self, p1, p2):
        self.__p1__ = p1
        self.__p2__ = p2
        self.__turno__ = 0  # 0 para p1, 1 para p2

    def jugador_actual(self):

        return self.__p1__ if self.__turno__ == 0 else self.__p2__

    def cambiar_turno(self):
        
        self.__turno__ = 1 - self.__turno__