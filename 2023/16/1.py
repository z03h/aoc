from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.read().splitlines()


grid = data

# pos = (row, col)
# direction = (vertical, horizontal)
# up = -1, down = 1
# left = -1, right = 1


class Light:
    def __init__(self, row, col, direction: tuple[int, int]):
        self.row = row
        self.col = col
        self.direction = direction


    def copy(self):
        return Light(self.row, self.col, self.direction)


max_rows = len(grid)
max_cols = len(grid[0])

charged = defaultdict(set)

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

lights = [Light(0,-1, RIGHT)]

while lights:
    new_lights = []
    for light in lights:
        row, col = light.row, light.col
        row_move, col_move = light.direction

        new_row = row + row_move
        new_col = col + col_move
        if (0 <= new_row < max_rows) and (0 <= new_col < max_cols):
            if light.direction in charged[(new_row, new_col)]:
                print('exit')
                continue
            new_lights.append(light)
            light.row, light.col = new_row, new_col
            charged[(new_row, new_col)].add(light.direction)
            new_char = grid[new_row][new_col]

            if row_move:
                # vertical movement
                match new_char, row_move:
                    case '-', _:
                        # split into 2 horizontal
                        light.direction = RIGHT
                        new_light = light.copy()
                        new_light.direction = LEFT
                        new_lights.append(new_light)
                    case '\\', 1:
                        # down
                        light.direction = RIGHT
                    case '\\', -1:
                        # up
                        light.direction = LEFT
                    case '/', 1:
                        # down
                        light.direction = LEFT
                    case '/', -1:
                        # up
                        light.direction = RIGHT
                    case _, _:
                        # continue same direction
                        pass

            elif col_move:
                # horizontal movement
                match new_char, col_move:
                    case '|', _:
                        # split into 2 vertical
                        light.direction = UP
                        new_light = light.copy()
                        new_light.direction = DOWN
                        new_lights.append(new_light)
                    case '\\', 1:
                        # right
                        light.direction = DOWN
                    case '\\', -1:
                        # left
                        light.direction = UP
                    case '/', 1:
                        # right
                        light.direction = UP
                    case '/', -1:
                        # left
                        light.direction = DOWN
                    case _, _:
                        # continue same direction
                        pass

        else:
            print('exit')

    lights = new_lights



print(len(charged))