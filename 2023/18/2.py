
from collections import defaultdict, deque
from PIL import Image, ImageDraw
import numpy as np

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


DIRECTIONS = {
    '2': LEFT,
    '3': UP,
    '0': RIGHT,
    '1': DOWN,
}

row, col = 0,0
edge = 0
points = []
rows = []
cols = []

for line in data:
    direction, num, color = line.split()

    direction = color[-2]
    num = int(color[2:-2], 16)
    dr, dc = DIRECTIONS[direction]
    dr *= num
    dc *= num

    # points.append((row, col, row+dr, col+dc))
    points.append((row, col))
    rows.append(row)
    cols.append(col)
    row += dr
    col += dc
    edge += num

# thanks stack overflow? i have no idea how this works
def PolyArea(x,y):
    # coordinate shift
    x_ = x - x.mean()
    y_ = y - y.mean()
    # everything else is the same as maxb's code
    correction = x_[-1] * y_[0] - y_[-1]* x_[0]
    main_area = np.dot(x_[:-1], y_[1:]) - np.dot(y_[:-1], x_[1:])
    return 0.5*np.abs(main_area + correction)


x = PolyArea(np.array(rows), np.array(cols))

# idk why i add the edge //2 + 1
# number of edge//2 for the outside that's not accounted for?
# +1 for the corner?
print(x ,len(rows), edge,  x+edge//2+1)

