from board import Board
from coordinate import Coordinate
from snake import Snake
from crashdetection import CrashDetection
from strategy import Strategy
import random

class Move:
    def __init__(self, snake: Snake, board: Board):
        self.snake = snake
        self.board = board

    def getMove(self):
        crash_detection = CrashDetection(self.board)
        strategy = Strategy(self.snake, self.board)
        weighted_moves = strategy.getWeightedMoves(self.snake.getPossibleMoves())
        return max(weighted_moves, key=weighted_moves.get)
