from board import Board
from coordinate import Coordinate
from snake import Snake
from crashdetection import CrashDetection
from math import sqrt

class Strategy:
    def __init__(self, snake: Snake, board: Board):
        self.snake = snake
        self.board = board
        self.crash_detection = CrashDetection(self.board)

    def getWeightedMoves(self, moves: dict):
        weighted_moves = {}
        closest_food = self.__getClosestFood()
        for move, coordinate in moves.items():
            weight = 0
            weight += self.__addWeightForCrash(coordinate, move)
            weight += self.__addWeightForClosestFood(coordinate, move, closest_food)
            #weight += self.__addWeightForGoingTowardsBiggerSpace(coordinate, move)
            weight += self.__addWeightForTrappedPaths(coordinate, 32)#len(self.snake.getBody()))
            weight += self.__addWeightForAvoidingHeadCollision(coordinate)
            #weight += self.__addWeightForEdgeCrawling(coordinate, move)
            weighted_moves[move] = weight
        print(weighted_moves)
        return weighted_moves

    def __addWeightForCrash(self, move: Coordinate, direction: str):
        weight = 0
        current = move
        if self.crash_detection.willCrash(current):
            weight -= 100
        #while True:
        #    if crash_detection.willCrash(current):
        #        break;
        #    else:
        #        if direction == "up":
        #            current.setY(current.getY() + 1)
        #        elif direction == "down":
        #            current.setY(current.getY() - 1)
        #        elif direction == "left":
        #            current.setX(current.getX() - 1)
        #        elif direction == "right":
        #            current.setX(current.getX() + 1)
        #        weight += 1
        return weight

    def __addWeightForClosestFood(self, move: Coordinate, direction: str, closest_food: Coordinate):
        if closest_food is None:
            return 0
        return -1 * self.__getDistance(move, closest_food)

    def __getClosestFood(self):
        closest = None
        closest_distance = 10000000
        for food in self.board.getFood():
            food_distance = self.__getDistance(self.snake.getHead(), food)
            if food_distance < closest_distance:
                closest = food
                closest_distance = food_distance
        return closest


    def __getDistance(self, location: Coordinate, food: Coordinate):
        difference_x = location.getX() - food.getX()
        difference_y = location.getY() - food.getY()
        return sqrt(pow(difference_x, 2) + pow(difference_y, 2))

    def __addWeightForGoingTowardsBiggerSpace(self, move: Coordinate, direction: str):
        if not self.__isTurning(direction):
            return 0
        if not self.__isTurningBecauseWillCrash():
            return 0
        if direction == "left":
            return abs(0 - self.snake.getHead().getX())
        if direction == "right":
            return abs(self.board.getWidth() - 1 - self.snake.getHead().getX())
        if direction == "down":
            return abs(0 - self.snake.getHead().getY())
        if direction == "up":
            return abs(self.board.getHeight() - 1 - self.snake.getHead().getY())
        return 0

    def __isTurning(self, direction: str):
        return direction != self.__getLastDirection()

    def __isTurningBecauseWillCrash(self):
        last_direction = self.__getLastDirection()
        if last_direction == "left" and self.snake.getHead().getX() - 1 < 0:
            return True
        if last_direction == "right" and self.snake.getHead().getX() + 1 >= self.board.getWidth():
            return True
        if last_direction == "down" and self.snake.getHead().getY() - 1 < 0:
            return True
        if last_direction == "up" and self.snake.getHead().getY() + 1 >= self.board.getHeight():
            return True
        return False

    def __getLastDirection(self):
        head_x = self.snake.getHead().getX()
        head_y = self.snake.getHead().getY()
        last_x = self.snake.getBody()[1].getX()
        last_y = self.snake.getBody()[1].getY()

        if head_x - last_x == -1:
            return "left"
        if head_x - last_x == 1:
            return "right"
        if head_y - last_y == -1:
            return "down"
        if head_y - last_y == 1:
            return "up"

    def __getEnclosedSpaces(self):
        enclosed_space = []
        area = []
        area.append(Coordinate(0, 0))
        while area:
            current = area.pop(0)
            if not self.crash_detection.willCrash(current) and current not in enclosed_space:
                enclosed_space.append(current)
                area.append(Coordinate(current.getX() - 1, current.getY()))
                area.append(Coordinate(current.getX() + 1, current.getY()))
                area.append(Coordinate(current.getX(), current.getY() + 1))
                area.append(Coordinate(current.getX(), current.getY() - 1))
        print(enclosed_space)

    def __addWeightForTrappedPaths(self, move: Coordinate, depth: int):
        queue = [move]
        visited = []
        count = 0
        while queue and count < depth:
            current = queue.pop(0)
            count += 1
            if (not self.crash_detection.willCrash(current)) and current not in visited:
                visited.append(current)
                queue.append(Coordinate(current.getX() + 1, current.getY()))
                queue.append(Coordinate(current.getX() - 1, current.getY()))
                queue.append(Coordinate(current.getX(), current.getY() + 1))
                queue.append(Coordinate(current.getX(), current.getY() - 1))
        if not queue:
            print("trapped")
            return -100 + len(visited)
        return 0

    def __addWeightForAvoidingHeadCollision(self, move: Coordinate):
        possible_moves = []
        for snake in self.board.getSnakes():
            if snake.getId() != self.snake.getId() and len(snake.getBody()) >= len(self.snake.getBody()):
                possible_moves.extend(snake.getPossibleMoves().values())
        if move in possible_moves:
            return -75
        return 0

    def __addWeightForEdgeCrawling(self, move: Coordinate, direction: str):
        if direction == "left" or direction == "right":
            if abs(move.getY() - self.board.getHeight()) < 3 or move.getY() < 3:
                return 1
        if direction == "up" or direction == "down":
            if abs(move.getX() - self.board.getWidth()) < 3 or move.getX() < 3:
                return 1
        return 0
