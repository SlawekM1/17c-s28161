import math


class SquareGenerator:
    def generate_squares(self, start, end):

        if end < start:
            raise ValueError("End of range cannot be less than start of range.")
        squares = []
        for num in range(start, end + 1):
            squares.append(num ** 2)
        return squares


    def calculate_square_roots(self, numbers):
        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots