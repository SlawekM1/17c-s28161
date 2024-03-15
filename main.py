squares = [x**2 for x in range(1, 11)]
squares

def generate_squares(start, end):
    return [x**2 for x in range(start, end + 1)]
