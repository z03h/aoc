from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

tails = [Point(0,0) for _ in range(10)]

visited: set[tuple[int, int]] = set(((0, 0),))

filename = 'input.txt'

with open(filename) as f:
    data = f.read()

def get_distance(h: Point, t: Point):
    return h.x-t.x, h.y-t.y

def move_vertical(h: Point, t: Point, value: int):
    h.y += value

    dx, dy = get_distance(h, t)

    if abs(dy) > 1:
        # move
        t.x += dx
        t.y += value

def move_horizontal(h: Point, t: Point, value: int):
    h.x += value

    dx, dy = get_distance(h, t)

    if abs(dx) > 1:
        # move
        t.x += value
        t.y += dy

def move_tail(prev: Point, current: Point):
    dx, dy = get_distance(prev, current)

    if abs(dx) > 1:
        if dx:
            current.x += dx//abs(dx)
        if dy:
            current.y += dy//abs(dy)
    elif abs(dy) > 1:
        if dx:
            current.x += dx//abs(dx)
        if dy:
            current.y += dy//abs(dy)


DIRECTION_LOOKUP: dict[str, tuple[int, Callable[[Point, Point, int], None]]] = {
    'R': (1, move_horizontal),
    'L': (-1, move_horizontal),
    'U': (1, move_vertical),
    'D': (-1, move_vertical),
}

end = tails[-1]
for line_no, instruction in enumerate(data.split('\n')):
    direction, snumber = instruction.split()
    number = int(snumber)

    value, move_func = DIRECTION_LOOKUP[direction]
    for _ in range(number):
        move_func(tails[0], tails[1], value)
        for i in range(0, len(tails)-1):
            move_tail(tails[i], tails[i+1])

        visited.add((end.x, end.y))

    #for num, n in enumerate(tails):
    #    print(num, n.x, n.y)
    #print()
    #if line_no == 1:
    #    exit()

print(len(visited))
