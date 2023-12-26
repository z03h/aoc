from heapq import heappop, heappush
from functools import cache
from collections import deque
import time

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

start= time.time()
INVALID: dict[tuple[int, int], str] = {
    (-1, 0): 'v',
    (1, 0): '^',
    (0, -1): '>',
    (0, 1): '<',
}


def around(rc: tuple[int, int], seen: set[tuple[int, int]]):
    points = []
    row, col = rc
    for i in (1, -1):
        nr = row + i
        nc = col + i
        if 0 <= nr < len(grid) and grid[nr][col] != '#' and grid[nr][col] != INVALID[(i, 0)] and (nr, col) not in seen:
            points.append((nr, col))

        if 0 <= nc < len(grid[0]) and grid[row][nc] != '#' and grid[row][nc] != INVALID[(0, i)] and (row, nc) not in seen:
            points.append((row, nc))

    return points


grid = [list(x) for x in data]

START = 0, 1
END = len(grid)-1, len(grid[0])-2

nodes = {}

def find_connected_nodes(start_point: tuple[int, int], point: tuple[int, int], seen: set[tuple[int, int]]):
    connected_nodes = nodes.setdefault(start_point, {})

    current = point
    moves = start_point != point

    while True:
        seen.add(current)
        adjacent = around(current, seen)
        if len(adjacent) == 1:
            current = adjacent[0]
            moves += 1
            continue

        if len(adjacent) > 1 or current == END:
            # found a node
            connected_nodes[current] = moves
            return adjacent, current, seen
        elif not adjacent:
            # we broke something?
            # went in a circle adandon the path?
            print(current)
            return None, None, None



states = deque()
states.append((START, START, set()))

while states:
    ns, s, ss = states.popleft()
    adjacent, next_start, seen = find_connected_nodes(ns, s, ss)
    if adjacent is None or seen is None:
        raise ValueError

    for n in adjacent:
        states.append((next_start, n, seen.copy()))


for k, v in nodes.items():
    print(k, v)
print('----------')

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