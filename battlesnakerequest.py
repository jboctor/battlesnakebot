from coordinate import Coordinate
from snake import Snake
from board import Board

class BattleSnakeRequest:
    def __init__(self, body):
        self.body = body

    def getBoard(self):
        snakes = []
        for snake in self.body['board']['snakes']:
            snakes.append(self.__makeSnake(snake))

        board = Board(
            self.body['board']['height'],
            self.body['board']['width'],
            snakes,
            self.__makeCoordinateList(self.body['board']['food']),
            self.__makeCoordinateList(self.body['board']['hazards'])
        )

        if self.body['game']['ruleset']['name'] == "wrapped":
            board.setWrapped(True)

        return board
            

    def getSnake(self):
        return self.__makeSnake(self.body['you'])
            
    def __makeSnake(self, snake_request):
        coordinates = []
        for coordinate in snake_request['body']:
            coordinates.append(Coordinate(coordinate['x'], coordinate['y']))

        return Snake(
            snake_request['id'],
            Coordinate(snake_request['head']['x'], snake_request['head']['y']),
            coordinates,
            snake_request['health']
        )

    def __makeCoordinateList(self, coordinate_request):
        coordinates = []
        for coordinate in coordinate_request:
            coordinates.append(Coordinate(coordinate['x'], coordinate['y']))

        return coordinates
