import random

def get_next_move(play_field):
    width = len(play_field[0])
    height = len(play_field)

    # Placeholder: picks a random position
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)

    return x, y, "EXPLORE"
