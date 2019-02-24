import random

class Alien:

    def __init__(self, board, count):
        self.startTime = count
        self.endTime = [0]
        self.endTime[0] = count + 8
        while True:
            self.x = random.randint(1, 2)
            self.y = random.randint(1, 8)
            if board.matrix[self.x][self.y] == ' ':
                break
