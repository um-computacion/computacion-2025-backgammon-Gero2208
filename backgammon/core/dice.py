import random

class Dice:

    def __init__(self):
        self.__valor__ = [0, 0]

    def roll(self):
        self.__valor__ = [random.randint(1, 6), random.randint(1, 6)]
        return self.__valor__
    
    def dobles(self):
        return self.__valor__ [0] == self.__valor__ [1]