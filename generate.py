import random

"""
Returns a 2D list with True marking mines
and False marking safe spaces
"""
def generate_field(mines=99, width=30, height=16):
    remaining_squares = width * height
    field = []
    for y in range(height):
        row = []
        for x in range(width):
            if random.randint(0, remaining_squares) < mines:
                mines -= 1
                row.append(True)
            else:
                row.append(False)
            remaining_squares -= 1
        field.append(row)
    return field
