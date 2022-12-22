import random

def get_next_move(play_field):
    width = len(play_field[0])
    height = len(play_field)

    open = []

    for x in range(width):
        for y in range(height):
            space = play_field[y][x]

            if space == None: open.append((x, y))

            if isinstance(space, int) and space > 0:
                open_neighbours = []
                num_of_open = 0

                for x_offset in range(-1, 2):
                    for y_offset in range(-1, 2):
                        check_x = x + x_offset
                        check_y = y + y_offset

                        if 0 <= check_x < width and 0 <= check_y < height:
                            if play_field[check_y][check_x] == None:
                                open_neighbours.append((check_x, check_y))
                                num_of_open += 1
                            if play_field[check_y][check_x] == '%':
                                num_of_open += 1
                
                if space == num_of_open and len(open_neighbours) > 0:
                    return open_neighbours[0][0], open_neighbours[0][1], "MARK"
    
    i = random.randint(0, len(open) - 1)
    space = open[i]
    return space[0], space[1], "EXPLORE"
