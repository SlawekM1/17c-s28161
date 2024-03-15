from square_generator import SquareGenerator

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):

        if end < start:
            raise ValueError("End of range cannot be less than start of range.")

        squares = [num ** 2 for num in range(start, end + 1)]
        return squares
