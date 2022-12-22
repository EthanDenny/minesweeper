from generate import *


def get_next_move(play_field):
    width = len(play_field[0])
    height = len(play_field)

    # Placeholder: picks a random position
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)

    return x, y


# Equivalent to "tapping" on a square
def play_move(play_field, minefield, x, y):
    # Add behaviour
    return


def play(mines=99, width=30, height=16):
    minefield = generate(mines, width, height)
    play_field = [[None] * width for y in range(height)]

    mines_left = mines

    while mines_left > 0:
        x, y = get_next_move(play_field)
        result = play_move(play_field, minefield, x, y)
        if result == "HIT MINE":
            print(f'Oops! Hit a mine at {x}, {y}')
            return
        elif result == "MARKED MINE":
            mines_left -= 1
    
    print('Solved the puzzle!')

if __name__ == "__main__":
    play()
