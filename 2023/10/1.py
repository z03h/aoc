from __future__ import annotations

from enum import IntFlag, auto

with open('input.txt' ,'r') as f:
    data = f.read()

LOOKUP = {
    '|': 1 + 4,
    '-': 2 + 8,
    'L': 1 + 2,
    'J': 1 + 8,
    '7': 4 + 8,
    'F': 4 + 2,
    '.': 0,
}

class Direction(IntFlag):
    up = auto()
    right = auto()
    down = auto()
    left = auto()


OPPOSITE = {
    Direction.up.value: Direction.down.value,
    Direction.left.value: Direction.right.value
}
for k, v in list(OPPOSITE.items()):
    OPPOSITE[v] = k


class Pipe:
    def __init__(self, row, col, value: str):
        self.row, self.col = row, col
        self.value = LOOKUP[value]
        self.pipes = Direction(self.value)
        self.dist = 0

    def connected(self, other: Pipe) -> bool:
        position = self.row - other.row, self.col - other.col
        match position:
            case (-1, 0):
                # other is above
                d = Direction.down.value
            case (1, 0):
                d = Direction.up.value
            case (0, -1):
                d = Direction.right.value
            case (0, 1):
                d = Direction.left.value
            case _:
                raise ValueError('Something went wrong', self.row, self.col, position, other.row, other.col)
        #print(self, other, bool(self.value & d),  bool(other.value & OPPOSITE[d]))
        return bool(self.value & d) and bool(other.value & OPPOSITE[d])

    def __repr__(self):
        return f'<{self.value} ({self.row},{self.col})>'


grid = []
start = [0, 0]
snode: Pipe = None  # type: ignore

for row, srow in enumerate(data.splitlines()):
    all_row = []
    for col, char in enumerate(srow):
        if char == 'S':
            # start
            start = (row, col)
            p = Pipe(row, col, '.')
            p.value = 1 + 2 + 4+ 8
            p.pipes = Direction(p.value)
            snode = p
            all_row.append(p)
        else:
            all_row.append(Pipe(row, col, char))
    grid.append(all_row)


def get_nodes(grid, row, col) -> list[Pipe]:
    max_row = len(grid)
    max_col = len(grid[0])
    pipes = []


    for i in (1, -1):
        nrow = row + i
        ncol = col + i

        if 0 <= nrow < max_row:
            pipes.append(grid[nrow][col])

        if 0 <= ncol < max_col:
            pipes.append(grid[row][ncol])

    return pipes

visited = set()

pipes = [snode]

max_dist = 0

while pipes:
    print('\t', pipes)
    new_pipes = []
    for node in pipes:
        around = get_nodes(grid, node.row, node.col)
        visited.add(node)

        for other in around:
            #print(other)
            if other not in visited and node.connected(other):
                other.dist = node.dist + 1
                if other.dist > max_dist:
                    max_dist = other.dist
                new_pipes.append(other)

    pipes = new_pipes




print(max_dist)