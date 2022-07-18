from coordinate import Coordinate

class Snake:
    def __init__(self, snake_id: str, head: Coordinate, body: list[Coordinate], health: int):
        self.snake_id = snake_id
        self.head = head
        self.body = body
        self.health = health

    def getId(self):
        return self.snake_id

    def getHead(self):
        return self.head

    def getBody(self):
        return self.body

    def getHealth(self):
        return self.health

    def getPossibleMoves(self):
        return {
            "right": Coordinate(self.head.getX() + 1, self.head.getY()),
            "left": Coordinate(self.head.getX() - 1, self.head.getY()),
            "up": Coordinate(self.head.getX(), self.head.getY() + 1),
            "down": Coordinate(self.head.getX(), self.head.getY() - 1)
        }
