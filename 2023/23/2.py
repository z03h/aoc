from heapq import heappop, heappush
from functools import cache
from collections import deque
import time


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

INVALID: dict[tuple[int, int], str] = {
    (-1, 0): 'v',
    (1, 0): '^',
    (0, -1): '>',
    (0, 1): '<',
}

start = time.time()
def around(rc: tuple[int, int], last: tuple[int, int]):
    points = []
    row, col = rc
    for i in (1, -1):
        nr = row + i
        nc = col + i
        if 0 <= nr < len(grid) and grid[nr][col] != '#' and (nr, col) != last:
            points.append((nr, col))

        if 0 <= nc < len(grid[0]) and grid[row][nc] != '#' and (row, nc) != last:
            points.append((row, nc))

    return points


grid = [list(x) for x in data]

START = 0, 1
END = len(grid)-1, len(grid[0])-2
print(END)
nodes = {}

seen_nodes = set()

def find_connected_nodes(start_point: tuple[int, int], point: tuple[int, int]):
    connected_nodes = nodes.setdefault(start_point, {})
    if (start_point, point) in seen_nodes:
        return None, None
    seen_nodes.add((start_point, point))
    last = start_point
    current = point
    moves = start_point != point

    while True:
        adjacent = around(current, last)
        if len(adjacent) == 1:
            last = current
            current = adjacent[0]
            moves += 1
            continue

        if len(adjacent) > 1 or current == END:
            # found a node
            connected_nodes[current] = moves
            return adjacent, current
        elif not adjacent:
            # we broke something?
            # went in a circle adandon the path?
            return None, None



states = deque()
states.append(((0,1), START))
i = 0
while states:
    i+= 1
    ns, s = states.popleft()
    adjacent, next_start = find_connected_nodes(ns, s)
    if adjacent is None or next_start is None:
        continue

    for n in adjacent:
        states.appendleft((next_start, n))


for k, v in nodes.items():
    print(k, v)



paths = deque()
paths.append((0, [START]))
potenial = (0, 0)
while paths:
    moves, path = paths.pop()
    last = path[-1]
    if last == END:
        if moves < potenial[0]:
            # lucky this printed the longest path before needing to fully finish
            print('FOUND', moves, time.time()-start)
            potenial = (moves, path)
        continue

    splits = nodes[last]

    for next_node, cost in splits.items():
        if next_node in path:
            continue
        pp = path.copy()
        pp.append(next_node)
        paths.append((moves - cost, pp))

x, path = potenial
print(x, path, time.time()-start)
"""
for i,p in enumerate(path):
    r,c = p
    grid[r][c] = str(i)

for row in grid:
    print(''.join(row))

cost = 0
for i in range(1, len(path)):
    prev = path[i-1]
    curr = path[i]
    x = nodes[prev][curr]
    cost += x
    print(prev, '>', curr, x, cost)

"""