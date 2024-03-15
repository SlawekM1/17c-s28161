import math


class SquareGenerator:
    def generate_squares(self, start, end):
        squares = []
        for num in range(start, end + 1):
            squares.append(num ** 2)
        return squares