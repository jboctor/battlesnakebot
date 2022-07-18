class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.getX() and self.y == other.getY()

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return self.__str__()

    def setX(self, x: int):
        self.x = x

    def setY(self, y: int):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
