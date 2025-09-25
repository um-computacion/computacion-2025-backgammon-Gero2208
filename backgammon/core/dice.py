import random

class Dice:

    def __init__(self):
        self.__valor__ = [0, 0]

    def roll(self):
        self.__valor__ = [random.radint(1, 6), random.radint(1, 6)]
        return self.__valor__