from board import Board
from coordinate import Coordinate

class CrashDetection:
    def __init__(self, board: Board):
        self.board = board

    def willCrash(self, spot: Coordinate):
        if self.__willGoOutOfBounds(spot):
            return True
        if self.__willCrashIntoSnake(spot):
            return True
        if self.__willCrashIntoHazard(spot):
            return True
        return False

    def __willGoOutOfBounds(self, spot: Coordinate):
        if self.board.isWrapped():
            return False
        if spot.getX() < 0:
            return True
        if spot.getX() >= self.board.getWidth():
            return True
        if spot.getY() < 0:
            return True
        if spot.getY() >= self.board.getHeight():
            return True
        return False

    def __willCrashIntoSnake(self, spot: Coordinate):
        for snake in self.board.getSnakes():
            for segment in snake.getBody():
                if spot.getX() == segment.getX() and spot.getY() == segment.getY():
                    return True
        return False

    def __willCrashIntoHazard(self, spot: Coordinate):
        for hazard in self.board.getHazards():
            if spot.getX() == hazard.getX() and spot.getY() == hazard.getY():
                return True
        return False
