import random


class Brain():
    __open = []
    __width = 0
    __height = 0

    def __init__(self, play_field):
        self.__width = len(play_field[0])
        self.__height = len(play_field)

        for x in range(self.__width):
            for y in range(self.__height):
                space = play_field[y][x]
                if space == None:
                    self.__open.append((x, y))


    def get_next_move(self, play_field):
        for pos in self.__open:
            x = pos[0]
            y = pos[1]
            space = play_field[y][x]

            if isinstance(space, int) and space > 0:
                open_neighbours = []
                num_of_open = 0

                for x_offset in range(-1, 2):
                    for y_offset in range(-1, 2):
                        check_x = x + x_offset
                        check_y = y + y_offset

                        if 0 <= check_x < self.__width and 0 <= check_y < self.__height:
                            if play_field[check_y][check_x] == None:
                                open_neighbours.append((check_x, check_y))
                                num_of_open += 1
                            if play_field[check_y][check_x] == '%':
                                num_of_open += 1
                
                if space == num_of_open and len(open_neighbours) > 0:
                    return open_neighbours[0][0], open_neighbours[0][1], "MARK"
        
        i = random.randint(0, len(self.__open) - 1)
        space = self.__open.pop(i)
        return space[0], space[1], "EXPLORE"
