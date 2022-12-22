from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

head = Point(0, 0)
tail = Point(0, 0)

visited: set[tuple[int, int]] = set(((0, 0),))

filename = 'input.txt'

with open(filename) as f:
    data = f.read()

def get_distance(h: Point, t: Point):
    return h.x-t.x, h.y-t.y

def move_vertical(value):
    old_h = head.x, head.y

    head.y += value

    dx, dy = get_distance(head, tail)

    if abs(dy) > 1:
        # move
        tail.x, tail.y = old_h
        visited.add((tail.x, tail.y))

def move_horizontal(value):
    old_h = head.x, head.y

    head.x += value

    dx, dy = get_distance(head, tail)

    if abs(dx) > 1:
        # move
        tail.x, tail.y = old_h
        visited.add((tail.x, tail.y))

DIRECTION_LOOKUP = {
    'R': (1, move_horizontal),
    'L': (-1, move_horizontal),
    'U': (1, move_vertical),
    'D': (-1, move_vertical),
}

for instruction in data.split('\n'):
    direction, snumber = instruction.split()
    number = int(snumber)

    value, move_func = DIRECTION_LOOKUP[direction]
    for _ in range(number):
        move_func(value)

print(len(visited))
