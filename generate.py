import random

"""
Returns a 2D list with 1's marking mines
and 0's marking safe spaces
"""
def generate(mines=99, width=30, height=16):
    remaining_squares = width * height
    field = []
    for y in range(height):
        row = []
        for x in range(width):
            if random.randint(0, remaining_squares) < mines:
                mines -= 1
                row.append(1)
            else:
                row.append(0)
            remaining_squares -= 1
        field.append(row)
    return field
