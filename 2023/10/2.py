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
        self.char = value

    def connected(self, other: Pipe) -> bool:
        position = self.row - other.row, self.col - other.col
        match position:
            case (-1, 0):
                # other is below
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

    def side_connected(self, position, other: Pipe) -> bool:
        match position:
            case (-1, 0):
                # other is below
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

    def __str__(self):
        return self.char


grid:list[list[Pipe]] = []
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
            p.char = 'S'
            snode = p
            all_row.append(p)
        else:
            all_row.append(Pipe(row, col, char))
    grid.append(all_row)

print('original row, col', len(grid), len(grid[0]))

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

def get_coords(grid, row, col) -> list[tuple[int, int]]:
    max_row = len(grid)
    max_col = len(grid[0])
    pipes = []


    for i in (1, -1):
        nrow = row + i
        ncol = col + i

        if 0 <= nrow < max_row:
            pipes.append((nrow, col))

        if 0 <= ncol < max_col:
            pipes.append((row, ncol))

    return pipes

visited = set()

pipes = [snode]
connected = {snode}


while pipes:
    #print('\t', pipes)
    new_pipes = []
    for node in pipes:
        if node in visited:
            continue
        around = get_nodes(grid, node.row, node.col)
        visited.add(node)

        for other in around:
            #print(other)
            if other not in visited and node.connected(other):
                new_pipes.append(other)
                connected.add(other)

    pipes = new_pipes




g2: list[list[Pipe|None]] = []
for row in grid:
    x = [p if p in connected else None for p in row]
    g2.append(x)

g3: list[list[Pipe|None]] = []
added_spots = 0

# add between each col
for row in g2:
    new_row = [None, row[0]]
    added_spots += 1
    for p in row[1:]:
        prev_p = new_row[-1]
        if p and prev_p and p.side_connected((0, 1),prev_p):
            new_row.append(Pipe(-1, -1, '-'))
        else:
            new_row.append(None)
        new_row.append(p)
        added_spots += 1


    new_row.append(None)
    added_spots += 1
    g3.append(new_row)

"""

for row in g3:
    print(
        ''.join(
            str(p) if p else '.' for p in row
        )
    )

print()
"""
g4: list[list[Pipe|None]] = [[None] * len(g3[0]), g3[0]]

# add rows in between each row
for row in g3[1:]:
    added_row = []
    for op, pp in zip(row, g4[-1]):
        if op and pp and op.side_connected((1, 0), pp):
            added_row.append(Pipe(0, 0, '|'))
        else:
            added_row.append(None)
    added_spots += len(added_row)
    g4.append(added_row)
    g4.append(row)

g4.append(g4[0])
"""
for row in g4:
    print(
        ''.join(
            str(p) if p else '.' for p in row
        )
    )
"""



# now do dfs around the edge
outside = set()

coords = [(0,0)]

while coords:
    newc = []
    for coord in coords:
        row, col = coord
        current = g4[row][col]
        if current or coord in outside:
            continue
        outside.add(coord)
        for new_coord in get_coords(g4, row, col):
            nr, nc = new_coord
            if new_coord in outside or g4[nr][nc]:
                continue
            newc.append(new_coord)
    coords = newc

print('new row,col', len(g4), len(g4[0]))
ahhh = 0

with open('test3.txt', 'w') as f:
    for rownum in range(1, len(g4)-1, 2):
        for colnum in range(1, len(g4[0])-2, 2):

            p = g4[rownum][colnum]
            if p:
                f.write(p.char)
            else:
                f.write('.')

            #print(rownum, colnum, p)
            ahhh += p is None and (rownum, colnum) not in outside
        f.write('\n')

print(ahhh)
