
from functools import cache
from scipy.interpolate import lagrange


with open('input.txt', 'r') as f:
    data = f.read().splitlines()
data = [d * 15 for d in data] * 15
ISTEPS = 26501365


grid = {}
start = (-1, -1)
for rownum, row in enumerate(data):
    for colnum, char in enumerate(row):
        grid[rownum, colnum] = char

#print(len(grid), max(grid), start, 131*131)
MAX_ROW, MAX_COL = max(grid)
start = MAX_ROW//2, MAX_COL//2

assert(grid[start] == 'S')

MAX_COL += 1
MAX_ROW += 1

max_grids, rem = divmod(ISTEPS-65, 131)
#print(max_grids, rem)

def find_len(start: tuple[int, int], avail_steps: int):
    even = set()
    odd = set()

    valid = [start]

    for step in range(avail_steps+1):
        if not valid:
            print(start, 'max steps', step)
            break

        seen = odd if (step ) % 2 else even

        new_valid = []

        for coord in valid:
            if coord in seen:
                continue
            seen.add(coord)

            # add 4 around it
            row, col = coord
            for i in (1, -1):
                nr = row + i
                nc = col + i
                n1 = (nr, col)
                n2 = (row, nc)
                if n1 in grid and grid[n1] != '#' and n1 not in seen:
                    new_valid.append(n1)
                if n2 in grid and grid[n2] != '#' and n2 not in seen:
                    new_valid.append(n2)
        valid = new_valid

    return len(odd if avail_steps % 2 else even)

xs = []
ys = []
for i in range(3):
    x = 65 + i * 131
    xs.append(x)
    gar = find_len(start,x)
    ys.append(gar)
print(xs, ys)
print(round(lagrange(xs, ys)(ISTEPS)))
