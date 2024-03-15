from square_generator import SquareGenerator

class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):

        if end < start:
            raise ValueError("End of range cannot be less than start of range.")

        cubes = [num ** 3 for num in range(start, end + 1)]
        return cubes
