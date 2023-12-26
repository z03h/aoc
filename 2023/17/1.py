from collections import defaultdict, deque
from heapq import heappush, heappop, heapify

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


DIRECTIONS = [
    LEFT,
    UP,
    RIGHT,
    DOWN,
]
TURN_LEFT = -1
TURN_RIGHT = 1

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

grid = {(i,j): int(c) for i,r in enumerate(data) for j,c in enumerate(r.strip())}

MAX_ROWS, MAX_COLS = max(grid)

def minimal(start: tuple[int, int], end):
    # loss, pos, prev direction
    q = [
        (*start, 0, 2),
        (*start, 0, 3),
    ]
    seen = set()

    while q:
        heat, row, col, prev_d = heappop(q)
        pos = row, col
        if pos == end:
            return heat
        key = (row, col, prev_d)
        if key in seen:
            continue
        seen.add(key)

        L_dir = (prev_d + TURN_LEFT) % 4
        R_dir = (prev_d + TURN_RIGHT) % 4

        for dd in (L_dir, R_dir):
            dr, dc = DIRECTIONS[dd]
            r, c, h = row, col, heat
            for i in range(3):
                r += dr
                c += dc

                if (r, c) not in grid:
                    break

                h += grid[r, c]
                heappush(q, (h, r, c, dd))

print(minimal((0,0), max(grid) ))
