import brain
import generate
import random


# Pretty prints a minefield
def output(field):
    for row in field:
        for space in row:
            if space == 0: print(' ', end='')
            elif space == None: print('.', end='')
            else: print(space, end='')
        print()


# Equivalent to "tapping" on a square
# Returns true if a mine exploded, and false if not
def play_move(play_field, minefield, x, y, action):
    width = len(play_field[0])
    height = len(play_field)

    if action == "MARK":
        play_field[y][x] = '%'
    elif action == "EXPLORE":
        if minefield[y][x]:
            for mine_x in range(width):
                for mine_y in range(height):
                    if minefield[mine_y][mine_x]:
                        if mine_x == x and mine_y == y:
                            play_field[mine_y][mine_x] = 'X'
                        elif play_field[mine_y][mine_x] == '%':
                            play_field[mine_y][mine_x] = '!'
                        else:
                            play_field[mine_y][mine_x] = '*'

            return True

        to_explore = [(x, y)]
        
        while len(to_explore) > 0:
            num_of_mines = 0
            explore_pos = to_explore.pop()

            for x_offset in range(-1, 2):
                for y_offset in range(-1, 2):
                    check_x = explore_pos[0] + x_offset
                    check_y = explore_pos[1] + y_offset

                    if 0 <= check_x < width and 0 <= check_y < height:
                        if minefield[check_y][check_x]:
                            num_of_mines += 1

            play_field[explore_pos[1]][explore_pos[0]] = num_of_mines

            if num_of_mines == 0:
                for x_offset in range(-1, 2):
                    for y_offset in range(-1, 2):
                        explore_x = explore_pos[0] + x_offset
                        explore_y = explore_pos[1] + y_offset

                        if 0 <= explore_x < width and 0 <= explore_y < height:
                            if play_field[explore_y][explore_x] == None:
                                to_explore.append((explore_x, explore_y))
    
    return False


def play_game(mines=99, width=30, height=16):
    minefield = generate.generate_field(mines, width, height)
    play_field = [[None] * width for y in range(height)]

    ai = brain.Brain(play_field)
    mines_left = mines

    while mines_left > 0:
        x, y, action = ai.get_next_move(play_field)
        if action == "MARK":
            mines_left -= 1
        
        hit_mine = play_move(play_field, minefield, x, y, action)
        if hit_mine:
            print(f'Oops! Hit a mine at {x}, {y}')
            print()
            output(play_field)
            return
    
    print('Solved the puzzle!')
    print()
    output(play_field)


if __name__ == "__main__":
    play_game()
