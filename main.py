import random

class Matrix:

    def __init__(self, row, col):
        self.n = row
        self.matrix = [[(random.randrange(0, 10))%2 for a in range(col)] for b in range(row)]

    def print(self):
        matrix = self.matrix
        for im in range(len(matrix)):
            print(matrix[im])


Matrix(6, 5).print()
