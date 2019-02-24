class Board:

    def __init__(self):
        self.matrix = [[' '] * 10 for i in range(9)]
        for i in range(10):
            self.matrix[0][i] = '_'
            self.matrix[8][i] = '_'
        for i in range(9):
            self.matrix[i][0] = '|'
            self.matrix[i][9] = '|'
        self.matrix[0][0] = ' '
        self.matrix[0][9] = ' '
        self.matrix[8][5] = '^'

    def Print(self):
        for i in range(9):
            for j in range(10):
                print self.matrix[i][j],
            print
        print


class SpaceShip:

    def __init__(self):
        self.pos = 5
