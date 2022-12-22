import random

def get_next_move(play_field):
    width = len(play_field[0])
    height = len(play_field)

    x = 0
    y = 0

    for space_x in range(width):
        for space_y in range(height):
            space = play_field[space_y][space_x]
            if isinstance(space, int) and space > 0:
                open = []
                num_of_open = 0

                for x_offset in range(-1, 2):
                    for y_offset in range(-1, 2):
                        check_x = space_x + x_offset
                        check_y = space_y + y_offset

                        if 0 <= check_x < width and 0 <= check_y < height:
                            if play_field[check_y][check_x] == None:
                                open.append((check_x, check_y))
                                num_of_open += 1
                            if play_field[check_y][check_x] == '%':
                                num_of_open += 1
                
                if space == num_of_open and len(open) > 0:
                    return open[0][0], open[0][1], "MARK"
    
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)

    return x, y, "EXPLORE"
