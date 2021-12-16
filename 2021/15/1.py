with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

from dataclasses import dataclass
import functools

@dataclass
class Node:
    row: int
    col: int
    distance: int

    shortest_dist: int = 99999999999999999999999999999999999999999999999999999999999999999
    previous = None
    visited: bool = False

    def __repr__(self):
        return f'<{self.row},{self.col}>'

    @property
    def xy(self):
        return self.row, self.col

lines = [[Node(row, col, int(i)) for col, i in enumerate(_)] for row, _ in enumerate(lines)]
ROWS = len(lines)
COLS = len(lines[0])


def get_adjacent(row, col):
    for r, c in ((row, col-1), (row, col+1), (row+1, col), (row-1, col)):
        if r >= 0 and r < ROWS and c >= 0 and c < COLS:
            yield r, c


lines[0][0].shortest_dist = lines[0][0].distance = 0

def dijkstra(current_node):

    unvisited = set()
    while True:
        row = current_node.row
        col = current_node.col
        for r, c in get_adjacent(row, col):
            node = lines[r][c]
            distance = current_node.shortest_dist + node.distance
            if distance < node.shortest_dist:
                node.shortest_dist = distance
                node.previous = current_node

        current_node.visited = True

        for r, c in get_adjacent(row, col):
            adj_node = lines[r][c]
            if adj_node.visited:
                continue
            unvisited.add(adj_node.xy)

        unvisited.discard(current_node.xy)

        if not unvisited:
            break
        r, c = min(unvisited, key=lambda n: (lines[n[0]][n[1]].visited, lines[n[0]][n[1]].shortest_dist))
        current_node = lines[r][c]
        print(current_node)


dijkstra(lines[0][0])

print(lines[-1][-1].shortest_dist)

def unwrap():
    path = []
    c = lines[-1][-1]
    if c.previous is None:
        print('bad')
        return
    while (c.row, c.col) != (0, 0):
        path.append((c.row, c.col, c.distance, c.shortest_dist))
        c = c.previous
    print('\n'.join(str(_) for _ in reversed(path)))

