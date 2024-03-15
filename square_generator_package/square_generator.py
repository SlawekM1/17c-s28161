import math
from abc import ABC, abstractmethod

class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range cannot be less than start of range.")

        squares = [num ** 2 for num in range(start, end + 1)]
        return squares


    def calculate_square_roots(self, numbers):
        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots