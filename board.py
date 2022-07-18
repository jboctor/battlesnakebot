from snake import Snake
from coordinate import Coordinate

class Board:
    __wrapped = False
    def __init__(self, height: int, width: int, snakes: list[Snake], food: list[Coordinate], hazards: list[Coordinate]):
        self.height = height
        self.width = width
        self.snakes = snakes
        self.food = food
        self.hazards = hazards

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getSnakes(self):
        return self.snakes

    def getFood(self):
        return self.food

    def getHazards(self):
        return self.hazards

    def setWrapped(self, wrapped: bool):
        self.__wrapped = wrapped

    def isWrapped(self):
        return self.__wrapped
